"""Convenience authentication layer over the generated client.

Hand-written (kept in .openapi-generator-ignore).

The Odditt API accepts two credential types, both exchanged for a short-lived
Bearer JWT at a login endpoint:

  * an API key           -> POST /v1/auth/login  (sends the X-API-Key header)
  * client_id + secret   -> POST /v1/oauth/login (body {client_id, client_secret})

Data endpoints also accept the API key directly via X-API-Key, so no login is
needed for them; the /v1/account/* endpoints require the Bearer token.

``AuthSession`` configures the generated client with the X-API-Key header (for an
API-key credential) and a dynamic ``access_token`` that lazily logs in and
transparently refreshes the Bearer token before it expires.

Example::

    from odditt_api_client import AuthSession, AccountApi, TrendsApi

    session = AuthSession.from_api_key("YOUR_API_KEY")
    trends = TrendsApi(session.api_client)    # uses X-API-Key
    account = AccountApi(session.api_client)   # uses the auto-refreshed Bearer

    session = AuthSession.from_client_credentials("CLIENT_ID", "CLIENT_SECRET")
"""

from __future__ import annotations

import threading
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional

from odditt_api_client.api.authentication_api import AuthenticationApi
from odditt_api_client.api_client import ApiClient
from odditt_api_client.configuration import Configuration
from odditt_api_client.exceptions import ApiException
from odditt_api_client.models.auth_o_auth_login_request import AuthOAuthLoginRequest
from odditt_api_client.models.auth_refresh_request import AuthRefreshRequest
from odditt_api_client.models.auth_token_pair import AuthTokenPair


class _AuthConfiguration(Configuration):
    """Configuration whose ``access_token`` is resolved dynamically per request."""

    def __init__(self, token_provider: Callable[[], str], **kwargs: object) -> None:
        self.__token_provider = token_provider
        super().__init__(**kwargs)  # type: ignore[arg-type]

    @property
    def access_token(self) -> str:  # type: ignore[override]
        return self.__token_provider()

    @access_token.setter
    def access_token(self, value: Optional[str]) -> None:
        # The base __init__ assigns access_token=None; ignore it — the token is
        # always supplied by the provider.
        pass


class AuthSession:
    """Auto-login/refresh auth wrapper. Pass ``.api_client`` to any *Api class."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        host: Optional[str] = None,
        skew_seconds: int = 60,
    ) -> None:
        if api_key is None and (client_id is None or client_secret is None):
            raise ValueError("provide api_key, or client_id and client_secret")

        self._api_key = api_key
        self._client_id = client_id
        self._client_secret = client_secret
        self._skew = timedelta(seconds=skew_seconds)
        self._token_pair: Optional[AuthTokenPair] = None
        self._expires_at: Optional[datetime] = None
        self._lock = threading.Lock()

        cfg_kwargs = {"host": host} if host else {}
        config = _AuthConfiguration(self._bearer_token, **cfg_kwargs)
        if api_key is not None:
            config.api_key["ApiKeyAuth"] = api_key  # X-API-Key for data endpoints
        self.api_client = ApiClient(config)

        # Unauthenticated client for the public login/refresh endpoints.
        self._auth_api = AuthenticationApi(ApiClient(Configuration(**cfg_kwargs)))

    @classmethod
    def from_api_key(cls, api_key: str, host: Optional[str] = None, skew_seconds: int = 60) -> "AuthSession":
        return cls(api_key=api_key, host=host, skew_seconds=skew_seconds)

    @classmethod
    def from_client_credentials(
        cls, client_id: str, client_secret: str, host: Optional[str] = None, skew_seconds: int = 60
    ) -> "AuthSession":
        return cls(client_id=client_id, client_secret=client_secret, host=host, skew_seconds=skew_seconds)

    # -- internals ---------------------------------------------------------

    def _bearer_token(self) -> str:
        with self._lock:
            if self._token_pair is not None and not self._expired():
                return self._token_pair.access_token
            if self._token_pair is not None and self._token_pair.refresh_token:
                self._token_pair = self._refresh()
            else:
                self._token_pair = self._login()
            self._expires_at = self._compute_expiry(self._token_pair)
            return self._token_pair.access_token

    def _login(self) -> AuthTokenPair:
        if self._api_key is not None:
            return self._auth_api.v1_auth_login_post(self._api_key)
        return self._auth_api.v1_oauth_login_post(
            AuthOAuthLoginRequest(client_id=self._client_id, client_secret=self._client_secret)
        )

    def _refresh(self) -> AuthTokenPair:
        assert self._token_pair is not None
        request = AuthRefreshRequest(refresh_token=self._token_pair.refresh_token)
        try:
            if self._api_key is not None:
                return self._auth_api.v1_auth_refresh_post(request)
            return self._auth_api.v1_oauth_refresh_post(request)
        except ApiException:
            return self._login()  # a rejected refresh token falls back to a full login

    def _expired(self) -> bool:
        return self._expires_at is None or datetime.now(timezone.utc) >= (self._expires_at - self._skew)

    def _compute_expiry(self, token_pair: AuthTokenPair) -> datetime:
        expires_at = getattr(token_pair, "expires_at", None)
        if expires_at is not None:
            parsed = self._parse_dt(expires_at)
            if parsed is not None:
                return parsed
        seconds = getattr(token_pair, "expires_in", None) or 3600
        return datetime.now(timezone.utc) + timedelta(seconds=int(seconds))

    @staticmethod
    def _parse_dt(value: object) -> Optional[datetime]:
        if isinstance(value, datetime):
            return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
        try:
            parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            return None
