from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from zope.interface import Interface, Attribute, implementer


class IResource(Interface):
    """ An entity in the system """

    name = Attribute('Unique identifier in a container')
    parent = Attribute('Object reference to the parent or None for root')
    title = Attribute('Text about this ')


class ICollection(IResource):
    """ A container resource such as a directory or folder """


@implementer(IResource)
@dataclass
class Resource:
    """ Superclass for all resource types """

    name: str
    parent: Optional[Resource]
    title: str
    body: str

    @property
    def __name__(self):
        return self.name

    @property
    def __parent__(self):
        return self.parent


@implementer(ICollection)
@dataclass
class Collection(Resource, dict):
    """ A container resource """

    def __post_init__(self):
        super(dict).__init__()
