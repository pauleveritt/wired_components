"""
Jinja2 environment for wired_component

Make an environment that can be used in views and components.
Register this as a singleton. Allow other packages to grab it
and register more places to look for templates.
"""

from wired import ServiceRegistry

from .models import IJinjaRenderer, JinjaRenderer


def wired_setup(registry: ServiceRegistry):
    pass
    # The environment is too tricky for a dataclass since it is a
    # subclass of jinja2.Environment.
    # registry.register_singleton(environment_factory, IJinjaEnvironment)


__all__ = [
    'wired_setup',
    'IJinjaRenderer',
    'JinjaRenderer',
]
