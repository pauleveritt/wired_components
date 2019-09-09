"""

Provide a decorator and imperative function for registering views.

"""
from typing import Type, Optional

from wired import ServiceRegistry, ServiceContainer
from wired.dataclasses import Injector

from wired_components.resource import IResource
from .models import IView
from ..decorator import BaseDecorator
from ..resource import Resource


def register_view(
        registry: ServiceRegistry,
        target: Type,
        context: Optional[Type[Resource]] = IResource
):
    """ Imperative form of the decorator """

    def view_factory(container: ServiceContainer):
        injector = Injector(container)
        view_instance = injector(target)
        return view_instance

    registry.register_factory(view_factory, IView, context=context)


class view(BaseDecorator):
    for_ = IView
