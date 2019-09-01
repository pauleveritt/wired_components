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
        context: Type[Resource] = Resource
):
    """ Implement the component decorator

     Breadcrumb(title='1')
     'Breadcrumb' -> partial
     partial(render_component, 'Breadcrumb', container, title='1'
     render_component
        component_factory = container.get(Component, name='Breadcrumb')
        component_instance = component_factory(name='Breadcrumbs')
     """
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