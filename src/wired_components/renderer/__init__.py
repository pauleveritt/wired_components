"""
Jinja2 environment for wired_component

Make an environment that can be used in views and components.
Register this as a singleton. Allow other packages to grab it
and register more places to look for templates.
"""

from wired import ServiceRegistry
from wired.dataclasses import register_dataclass

from .models import IJinjaRenderer, JinjaRenderer


def wired_setup(registry: ServiceRegistry) -> None:
    register_dataclass(registry, JinjaRenderer, for_=IJinjaRenderer)


__all__ = [
    'wired_setup',
    'IJinjaRenderer',
    'JinjaRenderer',
]
