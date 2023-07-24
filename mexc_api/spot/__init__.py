"""Defines the Spot class."""
from ..common.api import Api
from .endpoints._account import _Account
from .endpoints._market import _Market


class Spot:
    """Class for handling the MEXC REST API."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        api = Api(api_key, api_secret)

        self.market = _Market(api)
        self.account = _Account(api)
