"""Defines the _Market class"""
from mexc_api.common.api import Api
from mexc_api.common.enums import Method, OrderType, Side


class _Account:
    """Defines all Market endpoints"""

    def __init__(self, api: Api) -> None:
        self.api = api

    def test_new_order(
        self,
        symbol: str,
        side: Side,
        order_type: OrderType,
        quantity: str | None = None,
        quote_order_quantity: str | None = None,
        price: str | None = None,
        client_order_id: str | None = None,
    ) -> dict:
        """Creates a test order."""
        params = {
            "symbol": symbol.upper(),
            "side": side.value,
            "quantity": quantity,
            "price": price,
            "type": order_type.value,
            "quoteOrderQty": quote_order_quantity,
            "newClientOrderId": client_order_id,
        }
        return self.api.send_request(Method.POST, "/api/v3/order/test", params, True)

    def new_order(
        self,
        symbol: str,
        side: Side,
        order_type: OrderType,
        quantity: str | None = None,
        quote_order_quantity: str | None = None,
        price: str | None = None,
        client_order_id: str | None = None,
    ) -> dict:
        """Creates a new order"""
        params = {
            "symbol": symbol.upper(),
            "side": side.value,
            "quantity": quantity,
            "price": price,
            "type": order_type.value,
            "quoteOrderQty": quote_order_quantity,
            "newClientOrderId": client_order_id,
        }
        return self.api.send_request(Method.POST, "/api/v3/order", params, True)

    def batch_order(self) -> dict:
        """Creates multiple orders."""
        raise NotImplementedError

    def cancel_order(
        self,
        symbol: str,
        order_id: str | None = None,
        client_order_id: str | None = None,
    ) -> dict:
        """Cancels an order based on the order id or client order id."""
        params = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "origClientOrderId": client_order_id,
        }

        return self.api.send_request(Method.DELETE, "/api/v3/order", params, True)

    def cancel_open_orders(self, symbol: str) -> dict:
        """Cancels all open orders"""
        params = {
            "symbol": symbol.upper(),
        }
        return self.api.send_request(Method.DELETE, "/api/v3/openOrders", params, True)

    def get_order(
        self,
        symbol: str,
        order_id: str | None = None,
        client_order_id: str | None = None,
    ) -> dict:
        """Returns an order for a symbol based on the order id or client order id."""
        params = {
            "symbol": symbol.upper(),
            "orderId": order_id,
            "origClientOrderId": client_order_id,
        }
        return self.api.send_request(Method.GET, "/api/v3/order", params, True)

    def get_open_orders(self, symbol: str) -> dict:
        """Returns all open orders for a symbol."""
        params = {
            "symbol": symbol.upper(),
        }
        return self.api.send_request(Method.GET, "/api/v3/openOrders", params, True)

    def get_orders(
        self,
        symbol: str,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns all orders for a symbol within the optional start and end timestamps."""
        params = {
            "symbol": symbol.upper(),
            "limit": limit,
            "startTime": start_ms,
            "endTime": end_ms,
        }
        return self.api.send_request(Method.GET, "/api/v3/allOrders", params, True)

    def get_account_info(self) -> dict:
        """Returns the account info"""
        return self.api.send_request(Method.GET, "/api/v3/account", {}, True)

    def get_trades(
        self,
        symbol: str,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns all trades for a symbol within the optional start and end timestamps."""
        params = {
            "symbol": symbol.upper(),
            "limit": limit,
            "startTime": start_ms,
            "endTime": end_ms,
        }
        return self.api.send_request(Method.GET, "/api/v3/myTrades", params, True)

    def enable_mx_deduct(self, is_enabled: bool) -> dict:
        """Enables mx deduct."""
        params = dict(mxDeductEnable=is_enabled)
        return self.api.send_request(
            Method.POST, "/api/v3/mxDeduct/enable", params, True
        )

    def get_mx_deduct(self) -> dict:
        """Returns the mx deduct status."""
        return self.api.send_request(Method.GET, "/api/v3/mxDeduct/enable", {}, True)

    def create_listen_key(self) -> str:
        """Returns a listen key"""
        response = self.api.send_request(
            Method.POST, "/api/v3/userDataStream", {}, True
        )
        return response["listenKey"]

    def get_all_listen_keys(self) -> dict:
        """Returns a listen key"""
        return self.api.send_request(Method.GET, "/api/v3/userDataStream", {}, True)

    def keep_alive_listen_key(self, listen_key: str) -> None:
        """Keeps the listen key alive"""
        params = {"listenKey": listen_key}
        self.api.send_request(Method.PUT, "/api/v3/userDataStream", params, True)

    def delete_listen_key(self, listen_key: str) -> None:
        """deletes a listen key"""
        params = {"listenKey": listen_key}
        self.api.send_request(Method.DELETE, "/api/v3/userDataStream", params, True)
