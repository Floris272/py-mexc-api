"""Defines the Spot class."""
from ..common.api import Api
from .endpoints._account import _Account
from .endpoints._etf import _Etf
from .endpoints._market import _Market
from .endpoints._rebate import _Rebate
from .endpoints._sub_account import _SubAccount
from .endpoints._wallet import _Wallet


class Spot:
    """Class for handling the MEXC REST API."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        api = Api(api_key, api_secret)

        self.market = _Market(api)
        self.account = _Account(api)
        self.subaccount = _SubAccount(api)
        self.etf = _Etf(api)
        self.rebate = _Rebate(api)
        self.wallet = _Wallet(api)
