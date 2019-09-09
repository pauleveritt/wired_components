"""

Sample data for tests and demos.

We need sample data: resource trees, templates, almost like a working
application. We need it to be convenient to work with and refactor.
Rather than a big pile of Python or JSON, we'll use YAML and parse
into some classes.

Not doing anything exotic (e.g. strictyaml, pydantic.)

"""
from pathlib import Path

from markupsafe import Markup
from wired import ServiceRegistry, ServiceContainer

from wired_components import wired_setup as global_setup
from wired_components.configuration import IConfiguration, Configuration
from wired_components.renderer import JinjaRenderer, IJinjaRenderer
from wired_components.request import find_resource
from wired_components.resource import Root, IRoot, Resource
from wired_components.samples.simple import components, views
from wired_components.scanner import WiredScanner, IScanner
from wired_components.view import View, IView, as_dict
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


def render_path(registry: ServiceRegistry, resource_path: str) -> str:
    """ Render a resource at a path, to a string """

    # Get the root, then the context at the path
    container1: ServiceContainer = registry.create_container()
    root: Root = container1.get(IRoot)
    context: Resource = find_resource(root, resource_path)

    # Now make a container to process this context
    container2: ServiceContainer = registry.create_container(context=context)
    view: View = container2.get(IView)

    renderer: JinjaRenderer = container2.get(IJinjaRenderer)
    context_dict = as_dict(view)
    template_name = view.template
    markup: Markup = renderer.render(
        context_dict, template_name=template_name, container=container2
    )

    return str(markup)


__all__ = [
    'load_resources',
    'load_yaml',
    'render_path',
]
