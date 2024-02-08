"""REST client handling, including fleetioStream base class."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterable

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BasePageNumberPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream
import sys

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class fleetioCursorPagination(BasePageNumberPaginator):
    """
    Pagination for Streams supporting cursor based pagination
    """
    def has_more(self, response) -> bool:
        if (response.json().get('next_cursor') ) == None:
            has_more = False
        else:
            has_more = True
        return has_more
    
    def get_next(self, response):
        next_cursor = response.json().get("next_cursor")
        next_page = None
        if(next_cursor != None):
            next_page = next_cursor
            
        return next_page

class fleetioStream(RESTStream):
    """fleetio stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://secure.fleetio.com/api"

    #records_jsonpath = "$[*]"  # Or override `parse_response`.

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        headers["Authorization"] = f"Token {self.config.get('api_token')}"
        headers["Account-Token"] = self.config.get('account_token')
        headers["X-Client-Name"] = "data_connector"
        headers["X-Client-Platform"] = "fleetio_singer_tap"
        headers["X-Api-Version"] = self.api_version
        return headers

    def get_new_paginator(self):
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return fleetioCursorPagination(None)

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        start_replication = self.get_context_state(context)
        params: dict = {}
        if next_page_token and self.api_version == "2024-03-15":
            params["start_cursor"] = next_page_token
        params["per_page"] = 100
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
