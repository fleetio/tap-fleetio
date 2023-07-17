"""fleetio tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_fleetio import streams


class Tapfleetio(Tap):
    """fleetio tap class."""

    name = "tap-fleetio"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "account_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="Account Token",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://data-testing.preview.fleet.io/api",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.fleetioStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.IssuesStream(self),
            streams.ServiceEntriesStream(self),
            streams.SubmittedInspectionFormsStream(self),
            streams.VehiclesStream(self)
        ]


if __name__ == "__main__":
    Tapfleetio.cli()
