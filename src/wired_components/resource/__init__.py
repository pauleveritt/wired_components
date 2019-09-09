"""

Retrieve an entity in the system from the container.

``wired_components`` has a resource-with-view approach to rendering that
comes from Sphinx and from Pyramid traversal. A filename (or a URL) points
at a resource. You fetch the resource, then based on the resource type,
fetch the appropriate view, template, etc.

Based on this, getting the resource is important. But it's pluggable. You
can use a directory tree of Markdown or RST, a dbms, a big pile of YAML.
One aspect to note, though: resources are represented in a *tree* via the
``__parent__`` attribute.

"""
from wired import ServiceRegistry

from .decorators import (
    resource,
)
from .models import (
    IResource,
    Resource,
    ICollection,
    Collection,
    IRoot,
    Root,
    IDocument,
    Document,
)

from .services import context_parents, Parents, IParents


def wired_setup(registry: ServiceRegistry):
    registry.register_factory(context_parents, IParents)


__all__ = [
    'wired_setup',
    'IResource',
    'Resource',
    'ICollection',
    'Collection',
    'IRoot',
    'Root',
    'IDocument',
    'Document',
    'resource',
    'context_parents',
    'IParents',
    'Parents',
]
