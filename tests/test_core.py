"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_fleetio.tap import Tapfleetio

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "api_token": "xxx",
    "account_token": "xxx"
}


# Run standard built-in tap tests from the SDK:
TestTapfleetio = get_tap_test_class(
    tap_class=Tapfleetio,
    config=SAMPLE_CONFIG,
)


# TODO: Create additional tests as appropriate for your tap.
