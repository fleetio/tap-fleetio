"""Tests standard tap features using the built-in SDK tests library."""

import os
import datetime

from singer_sdk.testing import get_tap_test_class, SuiteConfig

from tap_fleetio.tap import Tapfleetio

SAMPLE_CONFIG = {
    "api_key": os.environ.get("TAP_FLEETIO_API_KEY"),
    "account_token": os.environ.get("TAP_FLEETIO_ACCOUNT_TOKEN")
}

suite_config = SuiteConfig(
    max_records_limit = 100
)


# Run standard built-in tap tests from the SDK:
TestTapfleetio = get_tap_test_class(
    tap_class=Tapfleetio,
    config=SAMPLE_CONFIG,
    suite_config = suite_config,
)
