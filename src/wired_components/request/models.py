from __future__ import annotations

from dataclasses import dataclass

from wired.dataclasses import injected, Context
from zope.interface import Interface, implementer

from wired_components.resource import IRoot
from .utils import relative_static_path, resource_path, relative_path
from ..resource import Resource, Root
from ..url import IUrl


class IRequest(Interface):
    """ Marker for request implementations """


@implementer(IRequest)
@dataclass
class Request:
    """ State and methods related to the currently-processed entity """

    context: Resource = injected(Context)
    root: Root = injected(IRoot)

    def static_url(self, asset_path: str) -> str:
        path = relative_static_path(self.context, asset_path)
        return path

    # noinspection PyMethodMayBeStatic
    def resource_path(self, resource: Resource) -> str:
        return resource_path(resource)

    def relative_path(self, target: Resource) -> str:
        return relative_path(self.root, self.context, target)
