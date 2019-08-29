"""

Consolidate functions related to the current URL and resource.

Most web frameworks, and to some extent Sphinx, operate on a request/response
approach. The request is an instance with state coming from the outside
context (filesystem, HTTP request) and the system itself. The request
massages that into a system representation, with helper methods.

The request object in most systems turns in the primary extension point,
quickly becoming a garbage-barge. With ``wired``, most of that goes away,
as anybody can register something at a well-known location that is easily
injected into whatever wants it.

Some stuff is left over. ``wired_components.request`` is that.

"""
from wired import ServiceRegistry
from wired.dataclasses import register_dataclass

from wired_components.resource import IResource
from .models import IRequest, Request
from .utils import (
    find_resource,
    normalize_path,
    parents,
    relative_path,
    resource_path,
    relative_static_path,
)


def wired_setup(registry: ServiceRegistry) -> None:
    register_dataclass(
        registry, Request, for_=IRequest, context=IResource
    )


__all__ = [
    'wired_setup',
    'IRequest',
    'Request',
    'find_resource',
    'normalize_path',
    'parents',
    'relative_path',
    'resource_path',
    'relative_static_path',
]
