from typing import Callable, Type, get_type_hints

from wired import ServiceContainer, ServiceRegistry
from zope.interface.adapter import AdapterRegistry

from wired_components.component import IComponent
from wired_components.request import Request
from wired_components.resource import Resource, IResource
from wired_components.view import View


def register_component(
        registry: ServiceRegistry,
        target: Callable,
        context: Type[Resource] = IResource
):
    """ Imperative form of the component decorator """
    component_name = target.__name__

    def component_factory(container: ServiceContainer):
        def construct_component(**props):
            """ A partial-partial, used to collect kwargs during calling """
            all_args = props.copy()

            # TODO Would be nice to replace this with DI once wired
            # supports props.
            # Only pass resource or view if the dataclass wants it
            fields = get_type_hints(target)
            if 'request' in fields:
                request: Request = container.get(Request)
                all_args['request'] = request
            if 'context' in fields:
                all_args['context'] = container.context
            if 'view' in fields:
                view: View = container.get(View)
                all_args['view'] = view
            component_instance = target(**all_args)
            return component_instance

        return construct_component

    # Use the name of the class, e.g. Breadcrumb, as the name argument
    # during registration
    registry.register_factory(
        component_factory, IComponent, context=context, name=component_name
    )
    # Next, add a zope.interface "subscription" to allow later reading of
    # all registered components
    adapter_registry: AdapterRegistry = registry._factories
    adapter_registry.subscribe([IResource], IComponent, target)


def register_component2(
        registry: ServiceRegistry,
        target: Callable,
        context: Type[Resource] = IResource
):
    """ Imperative form of the component decorator """

    # This is one using a hypothetical fork of wired.dataclasses.injector
    # while Michael and I discuss props
    component_name = target.__name__

    def component_factory(container: ServiceContainer):
        def construct_component(**kwargs):
            """ A partial-partial, used to collect kwargs during calling """

            # Let's use copied version of Injector, one that supports props
            from wired_components.injector2 import Injector
            injector = Injector(target)
            component_instance = injector(
                container=container,
                props=kwargs
            )
            return component_instance

        return construct_component

    # Use the name of the class, e.g. Breadcrumb, as the name argument
    # during registration
    registry.register_factory(
        component_factory, IComponent, context=context, name=component_name
    )
    # Next, add a zope.interface "subscription" to allow later reading of
    # all registered components
    adapter_registry: AdapterRegistry = registry._factories
    adapter_registry.subscribe([IResource], IComponent, target)
