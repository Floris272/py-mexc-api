"""Defines the _Wallet class."""
from mexc_api.common.api import Api
from mexc_api.common.enums import AccountType, Method


class _Wallet:
    """Defines all wallet endpoints."""

    def __init__(self, api: Api) -> None:
        self.api = api

    def info(self) -> list:
        """Returns all currency info."""
        return self.api.send_request(
            Method.GET, "/api/v3/capital/config/getall", {}, True
        )

    def withdraw(
        self,
        asset: str,
        network: str | None,
        address: str,
        amount: str,
        order_id: str | None = None,
        memo: str | None = None,
        remark: str | None = None,
    ) -> list:
        """Withdraws an asset from mexc to an address."""
        params = {
            "coin": asset.upper(),
            "network": network,
            "address": address,
            "amount": amount,
            "withdrawOrderId": order_id,
            "memo": memo,
            "remark": remark,
        }
        return self.api.send_request(
            Method.POST, "/api/v3/capital/withdraw/apply", params, True
        )

    def cancel_withdraw(self, withdraw_id: str) -> str:
        """Cancels a withdrawal."""
        params = {
            "id": withdraw_id,
        }
        response = self.api.send_request(
            Method.DELETE, "/api/v3/capital/withdraw", params, True
        )
        return response["id"]

    def get_withdrawal_history(
        self,
        asset: str | None = None,
        status: int | None = None,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> list:
        """Returns withdrawals based on the parameters."""
        params = {
            "coin": asset.upper() if isinstance(asset, str) else None,
            "status": status,
            "startTime": start_ms,
            "endTime": end_ms,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/withdraw/history", params, True
        )

    def get_deposit_history(
        self,
        asset: str | None = None,
        status: int | None = None,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int | None = None,
    ) -> list:
        """Returns deposits based on the parameters."""
        params = {
            "coin": asset.upper() if isinstance(asset, str) else None,
            "status": status,
            "startTime": start_ms,
            "endTime": end_ms,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/deposit/hisrec", params, True
        )

    def get_create_deposit_address(
        self,
        asset: str,
        network: str,
    ) -> list:
        """Creates an deposit address."""
        params = {
            "coin": asset.upper(),
            "network": network,
        }
        return self.api.send_request(
            Method.POST, "/api/v3/capital/deposit/address", params, True
        )

    def get_deposit_address(
        self,
        asset: str,
        network: str | None = None,
    ) -> dict:
        """Returns the deposit addresses of an asset."""
        params = {
            "coin": asset.upper(),
            "network": network,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/deposit/address", params, True
        )

    def get_withdrawal_address(
        self,
        asset: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns the withdrawal addresses of an asset. Returns all withdrawal addresses if no asset is given."""
        params = {
            "coin": asset.upper() if isinstance(asset, str) else None,
            "page": page,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/withdraw/address", params, True
        )

    def transfer(
        self,
        send_account_type: AccountType,
        receive_account_type: AccountType,
        asset: str,
        amount: str,
    ) -> list:
        """Tranfer an asset between account types"""
        params = {
            "fromAccountType": send_account_type,
            "toAccountType": receive_account_type,
            "asset": asset,
            "amount": amount,
        }
        return self.api.send_request(
            Method.POST, "/api/v3/capital/transfer", params, True
        )

    def get_transfers(
        self,
        send_account_type: AccountType,
        receive_account_type: AccountType,
        start_ms: int | None = None,
        end_ms: int | None = None,
        page: int | None = None,
        size: int | None = None,
    ) -> list:
        """Returns transfers baesed on the parameters."""
        params = {
            "fromAccountType": send_account_type,
            "toAccountType": receive_account_type,
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
            "size": size,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/transfer", params, True
        )

    def get_transfers_by_id(self, transfer_id: str) -> dict:
        """Returns an transfer."""
        params = {
            "tranId": transfer_id,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/transfer/tranId", params, True
        )

    def get_mx_convertible_assets(self) -> list:
        """Returns assets that can be converted into MX"""
        return self.api.send_request(
            Method.GET, "/api/v3/capital/convert/list", {}, True
        )

    def dust_transfer(self, asset: str | list[str]) -> dict:
        """Converts asset(s) to dust."""
        params = {
            "asset": asset,
        }
        return self.api.send_request(
            Method.POST, "/api/v3/capital/convert", params, True
        )

    def dust_log(
        self,
        start_ms: int | None = None,
        end_ms: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns the dust log."""
        params = {
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/capital/convert", params, True
        )
