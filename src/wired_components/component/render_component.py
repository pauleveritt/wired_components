"""

Render a component with props and a container.

This is pointed to by the partial, which makes a callable that can
be used in the Jinja2 template as a variable.

Done as SRP (single-responsibility-principle.)

"""

from markupsafe import Markup
from wired import ServiceContainer

from wired_components.renderer import IJinjaRenderer, JinjaRenderer
from .make_context import make_context


def render_component(
        container: ServiceContainer,
        component_name: str,
        **kwargs
) -> Markup:
    # Get the context for the template
    context = make_context(container, component_name, **kwargs)

    # Get the template
    template_name = f'{component_name.lower()}.jinja2'

    # Get the renderer
    renderer: JinjaRenderer = container.get(IJinjaRenderer)

    # Render and return
    m = renderer.render(context, template_name)
    return m
