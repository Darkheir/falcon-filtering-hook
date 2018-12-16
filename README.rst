falcon-filtering-hook
======================

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
    :target: LICENSE
.. image:: https://travis-ci.org/Darkheir/falcon-filtering-hook.svg?branch=master
    :target: https://travis-ci.org/Darkheir/falcon-filtering-hook
.. image:: https://codecov.io/gh/Darkheir/falcon-filtering-hook/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Darkheir/falcon-filtering-hook


A small falcon hook to parse filtering elements from the request.

Usage
-----

The easiest way to use this hook is the following:

.. code:: python

    @falcon.before(FilteringHook())
    def on_get(self, req, resp, user):
        # Here req['context']['filters'] is set

The Hook will look in the query parameters for parameters looking like :code:`filter[key]=value`.

It will create a filters dict into the request context accessible at :code:`req.context['filters']`.
Inside this dict the key will be the one extracted from between the brackets.
i.e. :code:`key` in the example above.

Configuration options
---------------------

One parameter can be passed to the hook:

* filtering_key : The base name of the key used for the filters. Default: :code:`filter`.

Example:

.. code:: python

    @falcon.before(PaginationFromRequestHook(
        filtering_key='custom_filter',
    ))
    def on_get(self, req, resp, user):
        # Get request

