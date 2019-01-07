import logging
import re

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

    def __call__(
        self, request: Request, response: Response, resource: object, params: dict
    ) -> None:
        """Actual hook operation that extract the filtering values from the request URL

        :param request: Falcon Request
        :param response: Falcon response
        :param resource: Reference to the resource class instance associated with the request
        :param params: dict of URI Template field names
        """
        request.context.setdefault("filters", dict())
        self._set_filters(request)

    def _set_filters(self, request: Request) -> None:
        """Extract the filters from the request and set it in the context dict.

        :param request: The Falcon request
        """
        for key, value in request.params.items():
            match = self._regex.match(key)
            if not match:
                continue
            request.context["filters"][match.group(1)] = value
