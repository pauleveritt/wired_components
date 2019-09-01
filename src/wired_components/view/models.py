from dataclasses import dataclass, field
from typing import Dict, get_type_hints, Any, List

from zope.interface import Interface, implementer

from wired_components.configuration import Configuration
from wired_components.request import Request, parents
from wired_components.resource import Resource, Root


class IView(Interface):
    """ Gather state and logic needed to render a request/resource """

    pass


@implementer(IView)
@dataclass
class View:
    configuration: Configuration
    context: Resource
    request: Request
    root: Root
    parents: List[Resource] = field(init=False)

    def __post_init__(self):
        self.parents = parents(self.context)

    def as_dict(self) -> Dict[str, Any]:
        # Return a flattened dictionary as context keys for each field.
        fields = get_type_hints(self.__class__)
        context = {name: getattr(self, name) for name, field in fields.items()}

        # Add this view instance in as something available in the context
        context['view'] = self
        return context
