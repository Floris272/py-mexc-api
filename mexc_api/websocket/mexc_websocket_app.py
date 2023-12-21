"""Defines the MexcWebsocketApp class."""
import json
import logging
import time
from threading import Thread
from typing import Callable

from websocket import WebSocketApp

from mexc_api.spot import Spot


class MexcWebsocketApp(WebSocketApp):  # type: ignore[misc]
    """
    Implements the WebSocketApp ands starts the run in a thread.
    Also creates a second thread for keeping the listen key alive.
    """

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        on_open: Callable | None = None,
        on_message: Callable | None = None,
        on_error: Callable | None = None,
        on_close: Callable | None = None,
    ) -> None:
        self.logger = logging.getLogger(__name__)
        spot = Spot(api_key, api_secret)
        self.listen_key = spot.account.create_listen_key()
        stream_url = f"wss://wbs.mexc.com/ws?listenKey={self.listen_key}"

        super().__init__(
            stream_url,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )

        Thread(
            target=self.run_forever, kwargs={"reconnect": 1, "ping_interval": 20}
        ).start()

        Thread(
            target=lambda: self._keep_alive(spot),
            daemon=True,
            name="Mexc keep alive listen key",
        ).start()

    def _keep_alive(self, spot: Spot) -> None:
        """Keeps the listen key alive."""
        while self._keep_alive:  # type: ignore[truthy-function]
            time.sleep(1800)
            spot.account.keep_alive_listen_key(self.listen_key)

    def send_message(self, message: dict) -> None:
        """Sends a message to the connected server."""
        self.logger.debug("Sending message to Mexc WebSocket Server: %s", message)
        self.send(json.dumps(message))
