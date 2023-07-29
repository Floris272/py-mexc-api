"""Defines the _Rebate class."""
from mexc_api.common.api import Api
from mexc_api.common.enums import Method


class _Rebate:
    """Defines all rebate endpoints."""

    def __init__(self, api: Api) -> None:
        self.api = api

    def get_records(
        self,
        start_ms: int | None = None,
        end_ms: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict:
        """Returns rebate records."""
        params = {
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
            "limit": limit,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/rebate/taxQuery", params, True
        )

    def get_record_details(
        self,
        start_ms: int | None = None,
        end_ms: int | None = None,
        page: int | None = None,
    ) -> dict:
        """Returns rebate record details."""
        params = {
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
        }
        return self.api.send_request(Method.GET, "/api/v3/rebate/detail", params, True)

    def get_self_rebate_records(
        self,
        start_ms: int | None = None,
        end_ms: int | None = None,
        page: int | None = None,
    ) -> dict:
        """Returns self rebate records."""
        params = {
            "startTime": start_ms,
            "endTime": end_ms,
            "page": page,
        }
        return self.api.send_request(
            Method.GET, "/api/v3/rebate/detail/kickback", params, True
        )

    def get_refer_code(self) -> str:
        """Returns an refer code"""
        response = self.api.send_request(
            Method.GET, "/api/v3/rebate/referCode", {}, True
        )
        return response["referCode"]
