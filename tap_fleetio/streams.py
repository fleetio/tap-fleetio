"""Stream type classes for tap-fleetio."""

from __future__ import annotations

from pathlib import Path

from tap_fleetio.client import fleetioStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class IssuesStream(fleetioStream):

    name = "issues"
    path = "/v2/issues"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "issues.json"  # noqa: ERA001


class ServiceEntriesStream(fleetioStream):

    name = "service_entries"
    path = "/v2/service_entries"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "service_entries.json"  # noqa: ERA001


class SubmittedInspectionFormsStream(fleetioStream):

    name = "submitted_inspection_forms"
    path = "/v1/submitted_inspection_forms"
    primary_keys = ["id"]
    replication_key = "submitted_at"
    schema_filepath = SCHEMAS_DIR / "submitted_inspection_forms.json"  # noqa: ERA001


class VehiclesStream(fleetioStream):

    name = "vehicles"
    path = "/v1/vehicles"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "vehicles.json"  # noqa: ERA001
