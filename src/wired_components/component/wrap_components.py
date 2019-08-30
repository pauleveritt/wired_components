"""

Wrap each component in a partial that has access to container and props.

Components are registered at startup but render multiple times per
container. In Jinja2, they are just a variable with a string value.
We need that string to point to a callable. And we need that callable
to have access to both the container and the arguments passed in as
keywords.

This wrapping should happen once per request container. After that, all
the partials will have access to the container. When each component does
a call (many times across all the views and subcomponents in a request),
the only thing passed to the partial are the props.

Thus, a wired factory is the right approach. Its result is cached for
the entire container. Since we are registering with context=None, one
factory serves all cases.

Done as SRP (single-responsibility-principle.)

"""

from functools import partial
from typing import Type, Dict, Any

from wired import ServiceContainer
from zope.interface import Interface

from wired_components.component import IAllComponents
from .render_component import render_component


class IWrapComponents(Interface):
    """ Marker for wrap components service """


def wrap_components(
        container: ServiceContainer,
) -> Dict[str, Type]:
    """ Wrap component rendering with a partial to gain access to container

    """

    # Get all the components, from the container
    components: Dict[str, Any] = container.get(IAllComponents)

    # For each, wrap them in a partial that contains the container
    return {
        component_name: partial(
            render_component,
            component_name=component_name,
            container=container,
            all_components=components,
        )
        for component_name, component in components.items()
    }
