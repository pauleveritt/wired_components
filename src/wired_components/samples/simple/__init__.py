"""

Sample data for tests and demos.

We need sample data: resource trees, templates, almost like a working
application. We need it to be convenient to work with and refactor.
Rather than a big pile of Python or JSON, we'll use YAML and parse
into some classes.

Not doing anything exotic (e.g. strictyaml, pydantic.)

"""
from dataclasses import dataclass
from pathlib import Path

from wired import ServiceRegistry
from wired.dataclasses import injected
from zope.interface import implementer

from wired_components import wired_setup as global_setup
from wired_components.configuration import IConfiguration, Configuration
from wired_components.resource import IResource, Root, IRoot
from wired_components.view import IView, View, register_view
from .loader import load_resources, load_yaml


def root_setup(registry: ServiceRegistry) -> None:
    from wired_components import samples
    d = Path(samples.__file__).parent / 'simple' / 'contents'
    root: Root = load_resources(d)
    registry.register_singleton(root, IRoot)


def configuration_setup(registry) -> None:
    """ At startup, stash a service with some app configuration """

    template_dirs = [('wired_components.samples.simple', 'templates')]
    configuration = Configuration(template_dirs=template_dirs)
    registry.register_singleton(configuration, IConfiguration)


@implementer(IView)
@dataclass
class RootView(View):
    title: str = injected(IResource, attr='title')
    template: str = 'rootview.jinja2'


def wired_setup(registry: ServiceRegistry):
    # Wire up the normal parts of wired_components
    global_setup(registry)

    # Wire up configuration and root
    configuration_setup(registry)
    root_setup(registry)

    # Now make some views
    register_view(registry, RootView, context=IResource)


__all__ = [
    'load_resources',
    'load_yaml',
]
