"""

Standalone factories for resource-related operations.

"""
from typing import List, Optional

from wired import ServiceContainer
from wired.dataclasses import Context
from zope.interface import Interface

from wired_components.request import parents
from wired_components.resource import Resource


class IParents(Interface):
    """ Marker for a list of parent resources """


Parents = List[Optional[Resource]]


def context_parents(container: ServiceContainer) -> Parents:
    context: Resource = container.get(Context)
    p = parents(context)
    return p
