"""

Provide a decorator and imperative function for registering views.

"""
from typing import Type

from wired import ServiceRegistry, ServiceContainer

from ..request import Request, IRequest
from .models import IView, View
from ..configuration import Configuration, IConfiguration
from ..decorator import BaseDecorator
from ..request import find_resource
from ..resource import Resource, Root, IRoot
from ..url import Url, IUrl


def register_view(
        registry: ServiceRegistry,
        target: Type,
        context: Type[Resource]
):
    """ Implement the view decorator """

    def view_factory(container: ServiceContainer):
        url: Url = container.get(IUrl)
        root: Root = container.get(IRoot)
        # TODO Perhaps the next line could be replaced with a
        #   IResource service?
        context_instance = find_resource(root, url.path)
        configuration: Configuration = container.get(IConfiguration)
        request: Request = container.get(IRequest, context=context_instance)
        view_instance: View = target(
            configuration=configuration,
            context=context_instance,
            request=request,
            root=root,
        )

        return view_instance

    registry.register_factory(view_factory, IView, context=context)


class view(BaseDecorator):
    for_ = View
    register_function = register_view
