"""Stream type classes for tap-fleetio."""

from __future__ import annotations

from pathlib import Path

from tap_fleetio.client import fleetioStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class IssuesStream(fleetioStream):

    name = "issues"
    path = "/v2/issues"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "issues.json"  # noqa: ERA001


class ServiceEntriesStream(fleetioStream):

    name = "service_entries"
    path = "/v2/service_entries"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "service_entries.json"  # noqa: ERA001


class SubmittedInspectionFormsStream(fleetioStream):

    name = "submitted_inspection_forms"
    path = "/v1/submitted_inspection_forms"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "submitted_inspection_forms.json"  # noqa: ERA001


class VehiclesStream(fleetioStream):

    name = "vehicles"
    path = "/v1/vehicles"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "vehicles.json"  # noqa: ERA001


class ExpenseEntriesStream(fleetioStream):

    name = "expense_entries"
    path = "/v1/expense_entries"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "expense_entries.json"  # noqa: ERA001


class ContactsStream(fleetioStream):

    name = "contacts"
    path = "/v2/contacts"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "contacts.json"  # noqa: ERA001


class FuelEntriesStream(fleetioStream):

    name = "fuel_entries"
    path = "/v1/fuel_entries"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "fuel_entries.json"  # noqa: ERA001


class PartsStream(fleetioStream):

    name = "parts"
    path = "/v1/parts"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "parts.json"  # noqa: ERA001


class PurchaseOrdersStream(fleetioStream):

    name = "purchase_orders"
    path = "/v1/purchase_orders"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "purchase_orders.json"  # noqa: ERA001


class VehicleAssignmentsStream(fleetioStream):

    name = "vehicle_assignments"
    path = "/v1/vehicle_assignments"
    primary_keys = ["id"]
    api_version = "2024-03-15"
    records_jsonpath = "$.records[*]"
    schema_filepath = SCHEMAS_DIR / "vehicle_assignments.json"  # noqa: ERA001