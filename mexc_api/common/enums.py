"""This module stores the enums used by the mexc_api classes"""
from enum import Enum


class Method(Enum):
    """Method enum"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class StreamInterval(Enum):
    """Interval enum used by the websocket kline stream."""

    ONE_MIN = "Min1"
    FIVE_MIN = "Min5"
    FIFTEEN_MIN = "Min15"
    THIRTY_MIN = "Min30"
    SIXTY_MIN = "Min60"
    FOUR_HOUR = "Hour4"
    EIGHT_HOUR = "Hour8"
    ONE_DAY = "Day1"
    ONE_WEEK = "Week1"
    ONE_MONTH = "Month1"


class Interval(Enum):
    """Interval used by the spot http kline endpoint."""

    ONE_MIN = "1m"
    FIVE_MIN = "5m"
    FIFTEEN_MIN = "15m"
    THIRTY_MIN = "30m"
    SIXTY_MIN = "60m"
    FOUR_HOUR = "4h"
    EIGHT_HOUR = "8h"
    ONE_DAY = "1d"
    ONE_MONTH = "1M"


class Side(Enum):
    """Side enum"""

    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    """Order type enum"""

    LIMIT = "LIMIT"
    MARKET = "MARKET"
    LIMIT_MAKER = "LIMIT_MAKER"
    # ???
    # IMMEDIATE_OR_CANCEL ="IMMEDIATE_OR_CANCEL"
    # FILL_OR_KILL = "FILL_OR_KILL"


class Action(Enum):
    """Action type enum"""

    SUBSCRIBE = "SUBSCRIPTION"
    UNSUBSCRIBE = "UNSUBSCRIPTION"
