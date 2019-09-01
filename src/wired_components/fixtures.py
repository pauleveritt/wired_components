from dataclasses import dataclass
from pathlib import Path

import pytest
from wired import ServiceContainer
from zope.interface import directlyProvides

from wired_components.samples import simple
from .component import IComponent, register_component
from .resource import Root
from wired_components.samples.simple import load_resources


@pytest.fixture
def simple_root() -> Root:
    d = Path(simple.__file__).parent / 'contents'
    root: Root = load_resources(d)
    return root


@dataclass
class Breadcrumb:
    label: str


@dataclass
class Link:
    label: str


@pytest.fixture
def configuration_setup(registry) -> None:
    """ At startup, stash a service with some app configuration """

    from wired_components.configuration import IConfiguration, Configuration
    template_dirs = [('wired_components.samples.simple', 'templates')]
    configuration = Configuration(template_dirs=template_dirs)
    registry.register_singleton(configuration, IConfiguration)


@pytest.fixture
def root_setup(registry, simple_root) -> None:
    """ At startup, stash resource tree root in a registry singleton """

    from wired_components.resource import IRoot
    registry.register_singleton(simple_root, IRoot)


@pytest.fixture
def renderer_setup(registry) -> None:
    """ Connect the renderer to the registry """

    from wired_components.renderer import wired_setup as renderer_setup
    renderer_setup(registry)


@pytest.fixture
def component_setup(registry):
    """ Top-level setup of component """

    from wired_components.component import wired_setup
    wired_setup(registry)


@pytest.fixture
def request_setup(registry):
    """ Top-level setup of request """
    from wired_components.request import wired_setup
    wired_setup(registry)


@pytest.fixture
def startup_container(registry) -> ServiceContainer:
    """ A container that reflects post-startup, before a request starts """

    # No context
    container = registry.create_container()
    return container


@pytest.fixture
def register_breadcrumb(registry) -> None:
    directlyProvides(Breadcrumb, IComponent)
    register_component(registry, Breadcrumb)
