"""

Gather state and logic needed to render a request/resource.

Views are the central actor in processing a ``wired_components``
request. They gather the needed input, specify a renderer, then
do the rendering.

Views can be registered against certain context types, allowing
different views for different kinds of resources.

"""
from wired import ServiceRegistry

from .decorator import register_view, view
from .models import IView, View, as_dict


def wired_setup(registry: ServiceRegistry) -> None:
    # No views should be registered by default, the application has
    # to provide all the views
    pass


__all__ = [
    'wired_setup',
    'IView',
    'View',
    'register_view',
    'view',
    'as_dict'
]
