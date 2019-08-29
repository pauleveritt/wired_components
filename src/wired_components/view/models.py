from dataclasses import dataclass
from typing import Dict, get_type_hints, Any, List, Optional

from wired import ServiceContainer
from zope.interface import Interface, implementer

from wired_components.configuration import Configuration, IConfiguration
from wired_components.request import Request, IRequest, parents
from wired_components.resource import Resource, IResource, Root, IRoot


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
    parents: List[Optional[Resource]]

    @classmethod
    def wired_setup(cls, container: ServiceContainer):
        configuration = container.get(IConfiguration)
        context = container.get(IResource)
        request = container.get(IRequest)
        root = container.get(IRoot)

        p = parents(context)

        return View(
            configuration=configuration,
            context=context,
            request=request,
            root=root,
            parents=p,
        )

    def as_dict(self) -> Dict[str, Any]:
        # Return a flattened dictionary as context keys for each field.
        fields = get_type_hints(self.__class__)
        context = {name: getattr(self, name) for name, field in fields.items()}

        # Add this view instance in as something available in the context
        context['view'] = self
        return context
