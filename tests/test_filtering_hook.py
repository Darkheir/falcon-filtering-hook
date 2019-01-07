from falcon_filtering.filtering_hook import FilteringHook


def test_empty_request(request_obj, mocker):
    hook = FilteringHook()
    hook(request_obj, mocker.Mock(), mocker.Mock(), dict())

    assert isinstance(request_obj.context.get("filters"), dict)


def test_request_with_filter(request_obj, mocker):
    request_obj.params["filter[foo]"] = 'bar'
    hook = FilteringHook()
    hook(request_obj, mocker.Mock(), mocker.Mock(), dict())

    assert request_obj.context["filters"]["foo"] == 'bar'


def test_request_with_multiple_filter(request_obj, mocker):
    request_obj.params["filter[foo]"] = 'foo'
    request_obj.params["filter[bar]"] = 'bar'
    hook = FilteringHook()
    hook(request_obj, mocker.Mock(), mocker.Mock(), dict())

    assert request_obj.context["filters"] == dict(foo='foo', bar='bar')


def test_request_with_non_filtering_keys(request_obj, mocker):
    request_obj.params["filter[foo]"] = 'foo'
    request_obj.params["ignore[bar]"] = 'bar'
    request_obj.params["foo"] = 'foo'
    hook = FilteringHook()
    hook(request_obj, mocker.Mock(), mocker.Mock(), dict())

    assert request_obj.context["filters"] == dict(foo='foo')
