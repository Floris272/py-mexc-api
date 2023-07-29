"""Defines the _SubAccount class."""
from mexc_api.common.api import Api
from mexc_api.common.enums import AccountType, Method


class _SubAccount:
    """Defines all sub account endpoints."""

    def __init__(self, api: Api) -> None:
        self.api = api

    def create_sub_account(self, account_name: str, desc: str) -> dict:
        """Creates an sub account."""
        params = {"subAccount": account_name, "note": desc}
        return self.api.send_request(
            Method.POST, "/api/v3/sub-account/virtualSubAccount", params, True
        )

    def get_sub_accounts(
        self,
        account_name: str | None = None,
        frozen: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns info of a sub account. Returns all subaccounts if name is not given."""
        params = {
            "subAccount": account_name,
            "isFreeze": frozen,
            "page": page,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/sub-account/list", params, True
        )

    def create_api_key(
        self,
        account_name: str,
        desc: str,
        permissions: list[str] | None = None,
        ips: list[str] | None = None,
    ) -> dict:
        """Creates an api key for a sub account."""
        params = {
            "subAccount": account_name,
            "note": desc,
            "permissions": permissions,
            "ip": ips,
        }
        return self.api.send_request(
            Method.POST, "/api/v3/sub-account/apiKey", params, True
        )

    def get_api_key(self, account_name: str) -> dict:
        """Returns the api key(s) of a sub account."""
        params = {"subAccount": account_name}
        return self.api.send_request(
            Method.GET, "/api/v3/sub-account/apiKey", params, True
        )

    def delete_api_key(self, account_name: str, api_key: str) -> None:
        """Deletes the api key of a sub account."""
        params = {"subAccount": account_name, "apiKey": api_key}
        self.api.send_request(Method.DELETE, "/api/v3/sub-account/apiKey", params, True)

    def transfer(
        self,
        send_account_type: AccountType,
        receive_account_type: AccountType,
        asset: str,
        amount: str,
        sender: str | None = None,
        receiver: str | None = None,
    ) -> str:
        """
        Transfers an asset between accounts.
        The default sender/receiver is the master account.
        Returns the transfer id.
        """
        params = {
            "fromAccount": sender,
            "toAccount": receiver,
            "fromAccountType": send_account_type,
            "toAccountType": receive_account_type,
            "asset": asset.upper(),
            "amount": amount,
        }
        response = self.api.send_request(
            Method.POST, "/api/v3/capital/sub-account/universalTransfer", params, True
        )
        return response["tranId"]

    def get_transfers(
        self,
        send_account_type: AccountType,
        receive_account_type: AccountType,
        start_ms: int | None = None,
        end_ms: int | None = None,
        sender: str | None = None,
        receiver: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns all transfers for the given parameters. The default sender/receiver is the master account."""
        params = {
            "fromAccount": sender,
            "toAccount": receiver,
            "fromAccountType": send_account_type,
            "toAccountType": receive_account_type,
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/sub-account/universalTransfer", params, True
        )
