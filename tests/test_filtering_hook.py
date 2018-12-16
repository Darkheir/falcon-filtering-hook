from unittest import TestCase
from unittest.mock import Mock

from falcon_filtering.filtering_hook import FilteringHook


class TestFilteringHook(TestCase):
    def setUp(self):
        self._request = Mock()
        self._request.context = dict()
        self._request.params = dict()

        self._response = Mock()
        self._resource = Mock()
        self._params = dict()

    def test_empty_request(self):
        hook = FilteringHook()
        hook(self._request, self._response, self._resource, self._params)

        self.assertIsInstance(self._request.context.get("filters"), dict)

    def test_request_with_filter(self):
        self._request.params["filter[foo]"] = 'bar'
        hook = FilteringHook()
        hook(self._request, self._response, self._resource, self._params)

        self.assertEqual(self._request.context["filters"]["foo"], 'bar')

    def test_request_with_multiple_filter(self):
        self._request.params["filter[foo]"] = 'foo'
        self._request.params["filter[bar]"] = 'bar'
        hook = FilteringHook()
        hook(self._request, self._response, self._resource, self._params)

        self.assertDictEqual(self._request.context["filters"], dict(foo='foo', bar='bar'))
