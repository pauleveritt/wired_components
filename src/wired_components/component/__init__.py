"""

Small, renderable units used in view templates.

Components are a popular paradigm in front-end frameworks. They take
passed-in props, do some munging, then render a template to an
HTML string.

Some go further and have a way to get registered data into a
deeply-nested component, such as dependency-injection (Angular) or
hooks (React.)

``wired_components`` uses the ``wired.dataclasses`` dependency injection.

Jinja2 components are tricky because they are string variables in the
template context which point to a callable. That callable needs access
to the currently-executing container. For now we are wrapping all
the possible components in a partial, as we enter a request-processing,
where the partial has access to the current container.

In the future we could resurrect the Jinja2 extension facility to make
"tags."

"""

from wired import ServiceRegistry

from .all_components import IAllComponents, all_components
from .make_context import make_context
from .models import IComponent
from .register_component import register_component
from .render_component import render_component
from .wrap_components import IWrapComponents, wrap_components


def wired_setup(registry: ServiceRegistry) -> None:
    registry.register_factory(all_components, IAllComponents)
    registry.register_factory(wrap_components, IWrapComponents)


__all__ = [
    'wired_setup',
    'IComponent',
    'register_component',
    'render_component',
    'IWrapComponents',
    'wrap_components',
    'IAllComponents',
    'all_components',
    'make_context',
]
