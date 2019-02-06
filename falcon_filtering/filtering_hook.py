import logging
import re
from typing import Any

from falcon import Request, Response


class FilteringHook(object):
    """Falcon Hook to extract filtering information from request.

    The extracted information are set in the request context dict
    under the "filters" key.
    """

    def __init__(self, filtering_key: str = "filter") -> None:
        """
        :param filtering_key: Base name for the filter query parameters
        """
        self._logger = logging.getLogger(__name__)
        self._filter_key = filtering_key
        self._regex = re.compile(r"{}\[(.*)\]".format(filtering_key))

    def __call__(self, request: Request, response: Response, resource: Any, params: dict) -> None:
        """Actual hook operation that extract the filtering values from the request URL

        :param request: Falcon Request
        :param response: Falcon response
        :param resource: Reference to the resource class instance associated with the request
        :param params: dict of URI Template field names
        """
        request.context.setdefault("filters", dict())
        if not hasattr(resource, "filtering_fields") or not resource.filtering_fields:
            self._logger.debug("filtering_fields is not defined in resource, skipping")
            return
        self._set_filters(request, resource)

    def _set_filters(self, request: Request, resource: Any) -> None:
        """Extract the filters from the request and set it in the context dict.

        :param request: The Falcon request
        """
        for key, value in request.params.items():
            match = self._regex.match(key)
            if not match:
                continue
            field_name = match.group(1)
            if field_name not in resource.filtering_fields:
                # Field not allowed, ignoring
                continue
            request.context["filters"][field_name] = value
