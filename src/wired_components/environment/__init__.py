"""
Jinja2 environment for wired_component

Make an environment that can be used in views and components.
Register this as a singleton. Allow other packages to grab it
and register more places to look for templates.
"""

from jinja2 import Environment, PackageLoader, ChoiceLoader
from wired import ServiceRegistry


# def make_environment() -> Environment:
#     # Construct the Jinja2 environment in here to allow setting the
#     # package loader and to load the components
#     choice_loader = ChoiceLoader([
#         PackageLoader('goku', 'views'),
#         PackageLoader('goku', 'components'),
#     ])
#     environment = Environment(loader=choice_loader)
#     return environment
#

def wired_setup(registry: ServiceRegistry):
    pass
    # environment = make_environment()
    # registry.register_singleton(environment, Environment)


__all__ = [
    'wired_setup',
]
