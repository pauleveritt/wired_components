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


class IRoot(ICollection):
    """ A container resource for the resource tree root """


class IDocument(IResource):
    """ A leaf node in a collection """


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
        super(dict).__init__()  # type: ignore


@implementer(IResource)
@dataclass
class Root(Collection):
    """ The root of the resource tree """


@implementer(IDocument)
@dataclass
class Document(Resource):
    """ A leaf node in a collection """
