# Simple versioning for [Django REST framework][docs]

[![pypi-version]][pypi]

# Overview

Django Rest Framework provides the ability to version an API via multiple methods, namespacing the URL, adding a version to the Accept header or query parameter, and provides this version to your code. However, it doesn't go further than this in helping split up what code is ran based on this version, leaving this a task up to the developer.

This mixin allows the developer to set which class is ran depending on what version is passed to the API, without interferring with how DRF generic views work.

# Requirements

* Python 2.7+
* Django Rest Framework 3.1+

# Installation

Install using `pip`...

    pip install django-rest-versioning

# Example

You wire up your generic views in the same way:

```python
from django.conf.urls import url, include
from items.views import ItemList

# Wire up your API using generic views
urlpatterns = [
    url(r'^items/$', ItemList.as_view())
]
```

Ensure the resulting generic view has the versioning mixin, and that you provide a versions dictionary detailing where each version of the endpoint exists.

```python

class ItemList(VersionedEndpoint, APIView):
	"""
	List all crazes.
	"""
	versions = {
		1.0 : 'api.v1.items.ItemList',
		2.0 : 'api.v2.items.ItemList'
	}
```

Each version of the endpoint can now do what it needs to do per version

```python

# v1
class ItemList(ListAPIView):
	"""
	List all items for v1.
	"""
    serializer_class = ItemSerializer
	queryset = Item.objects.all()
```

```python

# v2
class ItemList(ListCreateAPIView):
	"""
	List all items for v2, enable creation on v2
	"""
    serializer_class = ItemSerializer
	queryset = Item.objects.all()
```

# Considerations

If you request a version which does not have a corresponding entry in the versions dictionary, the dispatcher will select the latest version available by running `max` on the keys of the versions. This requires that keys in the dictionary are numerical, and ordered. This could be improved upon in the future.

If a module or class is not found, an `ImportError` or `AttributeError` will be raised.

[pypi-version]: https://img.shields.io/pypi/v/django-rest-versioning.svg
[pypi]: https://pypi.python.org/pypi/django-rest-versioning


[docs]: http://www.django-rest-framework.org/
