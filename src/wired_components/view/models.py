from dataclasses import dataclass, field
from typing import Dict, get_type_hints, Any, List

from wired.dataclasses import injected, Context
from zope.interface import Interface

from ..configuration import Configuration, IConfiguration
from ..request import Request, parents, IRequest
from ..resource import Resource, Root, IRoot


class IView(Interface):
    """ Gather state and logic needed to render a request/resource """

    pass


@dataclass
class View:
    configuration: Configuration = injected(IConfiguration)
    context: Resource = injected(Context)
    request: Request = injected(IRequest)
    root: Root = injected(IRoot)

    # TODO Add this to wired_dataclasses:
    # # If this is field(init=False) then skip
    #     if full_field.init == False:
    # continue
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
