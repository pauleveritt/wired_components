"""

Sample data for tests and demos.

We need sample data: resource trees, templates, almost like a working
application. We need it to be convenient to work with and refactor.
Rather than a big pile of Python or JSON, we'll use YAML and parse
into some classes.

Not doing anything exotic (e.g. strictyaml, pydantic.)

"""
from pathlib import Path

from wired import ServiceRegistry

from wired_components import wired_setup as global_setup
from wired_components.configuration import IConfiguration, Configuration
from wired_components.resource import Root, IRoot
from wired_components.scanner import WiredScanner, IScanner

from wired_components.samples.simple import components, views
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


def wired_setup(registry: ServiceRegistry):
    # Wire up the normal parts of wired_components
    global_setup(registry)

    # Wire up configuration and root
    configuration_setup(registry)
    root_setup(registry)

    # Get the scanner and look for things
    container = registry.create_container()
    scanner: WiredScanner = container.get(IScanner)
    scanner.scan(components)
    scanner.scan(views)

    from wired_components.component import register_component
    register_component(registry, components.Breadcrumb)


__all__ = [
    'load_resources',
    'load_yaml',
]
