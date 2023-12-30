"""Defines the _Market class."""
from mexc_api.common.api import Api
from mexc_api.common.enums import Interval, Method


class _Market:
    """Defines all Market endpoints."""

    def __init__(self, api: Api) -> None:
        self.api = api

    def test(self) -> None:
        """Tests connectivity to the Rest API."""
        self.api.send_request(Method.GET, "/api/v3/ping", {})

    def server_time(self) -> int:
        """Returns the server time."""
        response = self.api.send_request(Method.GET, "/api/v3/time", {})
        return response["serverTime"]

    def default_symbols(self) -> list[str]:
        """Returns all symbols."""
        response = self.api.send_request(Method.GET, "/api/v3/defaultSymbols", {})
        return response["data"]

    def exchange_info(
        self, symbol: str | None = None, symbols: list[str] | None = None
    ) -> dict:
        """
        Returns the rules and symbol info of the given symbol(s).
        All symbols will be returned when no parameter is given.
        """

        if symbol:
            symbol.upper()
        elif symbols:
            symbols = [symbol.upper() for symbol in symbols]

        params = {"symbol": symbol, "symbols": symbols}
        return self.api.send_request(Method.GET, "/api/v3/exchangeInfo", params)

    def order_book(self, symbol: str, limit: int | None = None) -> dict:
        """Returns the bids and asks of symbol."""
        params = {"symbol": symbol.upper(), "limit": limit}
        return self.api.send_request(Method.GET, "/api/v3/depth", params)

    def trades(self, symbol: str, limit: int | None = None) -> list:
        """Returns the the recent of symbol."""
        params = {"symbol": symbol.upper(), "limit": limit}
        return self.api.send_request(Method.GET, "/api/v3/trades", params)

    def agg_trades(
        self,
        symbol: str,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> list:
        """Returns the aggregate trades of symbol."""
        params = {
            "symbol": symbol.upper(),
            "limit": limit,
            "startTime": start_ms,
            "endTime": end_ms,
        }
        return self.api.send_request(Method.GET, "/api/v3/aggTrades", params)

    def klines(
        self,
        symbol: str,
        interval: Interval,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> list:
        """
        Returns the klines of a symbol on the given interval
        between the optional start and end timestamps.
        """
        params = {
            "symbol": symbol.upper(),
            "interval": interval.value,
            "limit": limit,
            "startTime": start_ms,
            "endTime": end_ms,
        }
        return self.api.send_request(Method.GET, "/api/v3/klines", params)

    def avg_price(self, symbol: str) -> dict:
        """Returns the average price of a symbol."""
        params = {
            "symbol": symbol.upper(),
        }
        return self.api.send_request(Method.GET, "/api/v3/avgPrice", params)

    def ticker_24h(self, symbol: str | None = None) -> list:
        """
        Returns ticker data from the last 24 hours.
        Data for all symbols will be sent if symbol was not given.
        """
        if symbol:
            symbol.upper()

        params = {
            "symbol": symbol,
        }
        response = self.api.send_request(Method.GET, "/api/v3/ticker/24hr", params)
        return [response] if isinstance(response, dict) else response

    def ticker_price(self, symbol: str | None = None) -> list:
        """
        Returns the ticker price of a symbol.
        Prices of all symbols will be send if symbol was not given.
        """
        if symbol:
            symbol.upper()

        params = {
            "symbol": symbol,
        }
        response = self.api.send_request(Method.GET, "/api/v3/ticker/price", params)
        return [response] if isinstance(response, dict) else response

    def ticker_book_price(self, symbol: str | None = None) -> list:
        """
        Returns the best price/qty on the order book for a symbol.
        Data for all symbols will be sent if symbol was not given.
        """
        if symbol:
            symbol.upper()

        params = {
            "symbol": symbol,
        }
        response = self.api.send_request(
            Method.GET, "/api/v3/ticker/bookTicker", params
        )
        return [response] if isinstance(response, dict) else response
