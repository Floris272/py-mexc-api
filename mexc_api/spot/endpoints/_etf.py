"""Defines the _Etf class."""
from mexc_api.common.api import Api
from mexc_api.common.enums import Method


class _Etf:
    """Defines all etf endpoints."""

    def __init__(self, api: Api) -> None:
        self.api = api

    def info(self, etf_symbol: str) -> dict:
        """Returns etf info."""
        params = {"symbol": etf_symbol.upper()}
        return self.api.send_request(Method.GET, "/api/v3/etf/info", params)
