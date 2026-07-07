# coding: utf-8

"""Tests for the hand-written AuthSession auth helper."""

from datetime import datetime, timedelta, timezone
from unittest.mock import patch

import pytest

from odditt_api_client import AuthSession
from odditt_api_client.models.auth_token_pair import AuthTokenPair


def _pair(access, in_secs=3600, refresh="refresh-token"):
    return AuthTokenPair(
        access_token=access,
        refresh_token=refresh,
        expires_at=datetime.now(timezone.utc) + timedelta(seconds=in_secs),
        expires_in=in_secs,
        token_type="Bearer",
    )


def test_from_api_key_sets_x_api_key():
    with patch("odditt_api_client.auth_session.AuthenticationApi"):
        session = AuthSession.from_api_key("my-key")
        assert session.api_client.configuration.api_key["ApiKeyAuth"] == "my-key"


def test_logs_in_and_caches_bearer():
    with patch("odditt_api_client.auth_session.AuthenticationApi") as auth_api:
        instance = auth_api.return_value
        instance.v1_auth_login_post.return_value = _pair("tok1")
        session = AuthSession.from_api_key("my-key")
        assert session._bearer_token() == "tok1"
        assert session._bearer_token() == "tok1"  # cached
        instance.v1_auth_login_post.assert_called_once_with("my-key")


def test_refreshes_when_expired():
    with patch("odditt_api_client.auth_session.AuthenticationApi") as auth_api:
        instance = auth_api.return_value
        instance.v1_auth_login_post.return_value = _pair("tok1", in_secs=-10)
        instance.v1_auth_refresh_post.return_value = _pair("tok2", in_secs=3600)
        session = AuthSession(api_key="my-key", skew_seconds=0)
        assert session._bearer_token() == "tok1"  # initial login (already expired)
        assert session._bearer_token() == "tok2"  # expired -> refresh
        instance.v1_auth_refresh_post.assert_called_once()


def test_client_credentials_login():
    with patch("odditt_api_client.auth_session.AuthenticationApi") as auth_api:
        instance = auth_api.return_value
        instance.v1_oauth_login_post.return_value = _pair("otok")
        session = AuthSession.from_client_credentials(client_id="id", client_secret="secret")
        assert "ApiKeyAuth" not in session.api_client.configuration.api_key
        assert session._bearer_token() == "otok"
        instance.v1_oauth_login_post.assert_called_once()


def test_requires_credentials():
    with pytest.raises(ValueError):
        AuthSession()
    with pytest.raises(ValueError):
        AuthSession(client_id="id")
