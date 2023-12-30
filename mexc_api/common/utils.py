"""Defines utils used in the package."""
import time


def get_timestamp() -> int:
    """Returns the current timestamp in milliseconds."""
    return round(time.time() * 1000)
