from falcon_filtering.filtering_hook import FilteringHook


def test_empty_request(request_obj, mocker):
    hook = FilteringHook()

    class Resource:
        filtering_fields = ("foo", "bar")

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context.get("filters") == {}


def test_request_with_filter(request_obj, mocker):
    request_obj.params["filter[foo]"] = "bar"
    hook = FilteringHook()

    class Resource:
        filtering_fields = ("foo",)

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context["filters"]["foo"] == "bar"


def test_request_with_multiple_filter(request_obj, mocker):
    request_obj.params["filter[foo]"] = "foo"
    request_obj.params["filter[bar]"] = "bar"
    hook = FilteringHook()

    class Resource:
        filtering_fields = ("foo", "bar")

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context["filters"] == dict(foo="foo", bar="bar")


def test_request_with_non_filtering_keys(request_obj, mocker):
    request_obj.params["filter[foo]"] = "foo"
    request_obj.params["ignore[bar]"] = "bar"
    request_obj.params["foo"] = "foo"
    hook = FilteringHook()

    class Resource:
        filtering_fields = ("foo", "bar")

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context["filters"] == dict(foo="foo")


def test_request_with_filter_not_allowed(request_obj, mocker):
    request_obj.params["filter[bar]"] = "bar"
    hook = FilteringHook()

    class Resource:
        filtering_fields = ("foo",)

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context["filters"] == {}


def test_request_without_filtering_fields(request_obj, mocker):
    request_obj.params["filter[foo]"] = "bar"
    hook = FilteringHook()

    class Resource:
        pass

    hook(request_obj, mocker.Mock(), Resource(), dict())

    assert request_obj.context["filters"] == {}
