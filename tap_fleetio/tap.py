"""fleetio tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_fleetio import streams


class Tapfleetio(Tap):
    """fleetio tap class."""

    name = "tap-fleetio"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The key to authenticate against the Fleetio API",
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
            default="https://secure.fleetio.com/api",
            description="Fleetio API base url",
        )
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
            streams.VehiclesStream(self),
            streams.ExpenseEntriesStream(self),
            streams.ContactsStream(self),
            streams.FuelEntriesStream(self),
            streams.PartsStream(self),
            streams.PurchaseOrdersStream(self),
            streams.VehicleAssignmentsStream(self),
        ]


if __name__ == "__main__":
    Tapfleetio.cli()
