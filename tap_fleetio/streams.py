"""Stream type classes for tap-fleetio."""

from __future__ import annotations

from pathlib import Path

from tap_fleetio.client import fleetioStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class IssuesStream(fleetioStream):

    name = "issues"
    path = "/issues"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "issues.json"  # noqa: ERA001


class ServiceEntriesStream(fleetioStream):

    name = "service_entries"
    path = "/service_entries"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "service_entries.json"  # noqa: ERA001


class SubmittedInspectionFormsStream(fleetioStream):

    name = "submitted_inspection_forms"
    path = "/submitted_inspection_forms"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "submitted_inspection_forms.json"  # noqa: ERA001


class VehiclesStream(fleetioStream):

    name = "vehicles"
    path = "/vehicles"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "vehicles.json"  # noqa: ERA001


class ExpenseEntriesStream(fleetioStream):

    name = "expense_entries"
    path = "/expense_entries"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "expense_entries.json"  # noqa: ERA001


class ContactsStream(fleetioStream):

    name = "contacts"
    path = "/contacts"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "contacts.json"  # noqa: ERA001


class FuelEntriesStream(fleetioStream):

    name = "fuel_entries"
    path = "/fuel_entries"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "fuel_entries.json"  # noqa: ERA001


class PartsStream(fleetioStream):

    name = "parts"
    path = "/parts"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "parts.json"  # noqa: ERA001


class PurchaseOrdersStream(fleetioStream):

    name = "purchase_orders"
    path = "/purchase_orders"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "purchase_orders.json"  # noqa: ERA001


class VehicleAssignmentsStream(fleetioStream):

    name = "vehicle_assignments"
    path = "/vehicle_assignments"
    primary_keys = ["id"]
    api_version = "2025-05-05"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "vehicle_assignments.json"  # noqa: ERA001
