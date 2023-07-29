"""Defines the Api class."""
import hashlib
import hmac
from typing import Any

from requests import Session

from .enums import Method
from .exceptions import MexcAPIError
from .utils import get_timestamp


class Api:
    """Defines a base api class."""

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str = "https://api.mexc.com",
        recv_window: int = 5000,
    ) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

        self.base_url = base_url
        self.recv_window = recv_window

        self.session = Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "X-MEXC-APIKEY": self.api_key}
        )

    def get_query(self, params: dict) -> str:
        """Returns a query string of all given parameters."""
        query = ""
        for key, value in params.items():
            query += f"{key}={value}&"
        return query[:-1]

    def get_signature(self, query: str) -> str:
        """Returns the signature based on the api secret and the query."""
        return hmac.new(
            self.api_secret.encode("utf-8"), query.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def remove_none_params(self, params: dict) -> dict:
        """Returns a dict without empty parameter values."""
        return {k: v for k, v in params.items() if v is not None}

    def send_request(
        self, method: Method, endpoint: str, params: dict, sign: bool = False
    ) -> Any:
        """
        Sends a request with the given method to the given endpoint.
        RecvWindow, timestamp and signature are added to the parameters.

        Throws an MexcAPIError if the response has an error.
        Returns the json encoded content of the response.
        """
        params = self.remove_none_params(params)

        if sign:
            params["recvWindow"] = self.recv_window
            params["timestamp"] = get_timestamp()
            params["signature"] = self.get_signature(self.get_query(params))
        response = self.session.request(method.value, self.base_url + endpoint, params)

        if not response.ok:
            raise MexcAPIError(response.status_code, response.json().get("msg"))

        return response.json()
