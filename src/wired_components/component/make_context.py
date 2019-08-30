"""

Make the Jinja2 context for rendering a component.

The component context needs a few things:

- The instance of the dataclass, with fields flattened into a dict
- All the wrapped components, because a component might render a subcomponent

Done as SRP (single-responsibility-principle.)

"""

import dataclasses
from typing import Dict, Any

from wired import ServiceContainer


def make_context(
        container: ServiceContainer,
        component_name: str,
        **kwargs
) -> Dict[str, Any]:
    """ Make component fields, other info into dict for template context """

    from wired_components.component import IWrapComponents, IComponent

    # Start with all the wrapped components
    context: Dict[str, Any] = container.get(IWrapComponents)

    # We get the component again in case there are multiple components
    # registered with the same name, but for more specific contexts.
    component_factory = container.get(IComponent, name=component_name)

    # TODO Try to replace this part with DI+props in wired.components
    #   (see above in component_factory)
    component_instance = component_factory(**kwargs)

    # Copy all the fields into the context dict
    for field in dataclasses.fields(component_instance):
        context[field.name] = getattr(component_instance, field.name)

    return context
