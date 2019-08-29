"""

Gather state and logic needed to render a request/resource.

Views are the central actor in processing a ``wired_components``
request. They gather the needed input, specify a renderer, then
do the rendering.

Views can be registered against certain context types, allowing
different views for different kinds of resources.

"""
from wired import ServiceRegistry

from wired_components.resource import IResource
from .models import IView, View


def wired_setup(registry: ServiceRegistry) -> None:
    registry.register_factory(
        View.wired_setup, IView, context=IResource,
    )



__all__ = [
    'wired_setup',
    'IView',
    'View',
]
