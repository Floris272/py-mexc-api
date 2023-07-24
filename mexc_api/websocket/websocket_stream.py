"""Defines the MexcWebsocketClient"""
import logging
from typing import Callable, Literal

from mexc_api.common.enums import Action, StreamInterval

from .mexc_websocket_app import MexcWebsocketApp


class SpotWebsocketStreamClient:
    """Handles the stream subscriptions"""

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        on_message: Callable,
        on_close: Callable | None = None,
        on_error: Callable | None = None,
    ):
        self.logger = logging.getLogger(__name__)
        self.streams: set[str] = set()

        self.mexc_websocket_app = MexcWebsocketApp(
            api_key=api_key,
            api_secret=api_secret,
            on_message=on_message,
            on_open=self._on_open,
            on_close=on_close,
            on_error=on_error,
        )
        self.logger.debug("Mexc WebSocket Client started.")

    def _on_open(self, _app: MexcWebsocketApp) -> None:
        for stream in self.streams:
            self._change_subscription(stream)

    def _change_subscription(
        self, stream: str, action: Action = Action.SUBSCRIBE
    ) -> None:
        """Subscribes to or unsubscribes from stream."""
        self.streams.add(stream)
        message = {"method": action.value, "params": [stream]}
        self.mexc_websocket_app.send_message(message)

    def stop(self) -> None:
        """Stops the websocket connection."""
        self.mexc_websocket_app.close()

    def trades(self, symbol: str, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to the trade stream of a symbol"""
        self._change_subscription(f"spot@public.deals.v3.api@{symbol.upper()}", action)

    def klines(
        self, symbol: str, interval: StreamInterval, action: Action = Action.SUBSCRIBE
    ) -> None:
        """Subscribes to the kline stream of a symbol"""
        self._change_subscription(
            f"spot@public.kline.v3.api@{symbol.upper()}@{interval.value}", action
        )

    def diff_depth(self, symbol: str, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to the increase depth stream of a symbol."""
        self._change_subscription(
            f"spot@public.increase.depth.v3.api@{symbol.upper()}", action
        )

    def partial_depth(
        self, symbol: str, level: Literal[5, 10, 20], action: Action = Action.SUBSCRIBE
    ) -> None:
        """Subscribes to the partial depth stream of a symbol."""
        self._change_subscription(
            f"spot@public.limit.depth.v3.api@{symbol.upper()}@{level}", action
        )

    def book_ticker(self, symbol: str, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to the book ticker stream of a symbol."""
        self._change_subscription(
            f"spot@public.bookTicker.v3.api@{symbol.upper()}", action
        )

    def account_updates(self, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to account updates"""
        self._change_subscription("spot@private.account.v3.api", action)

    def account_deals(self, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to account deals"""
        self._change_subscription("spot@private.deals.v3.api", action)

    def account_orders(self, action: Action = Action.SUBSCRIBE) -> None:
        """Subscribes to account orders"""
        self._change_subscription("spot@private.orders.v3.api", action)
