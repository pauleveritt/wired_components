from dataclasses import dataclass
from pathlib import Path

import pytest
from wired import ServiceContainer
from zope.interface import directlyProvides

from wired_components import sample
from .component import (
    IComponent, register_component, wired_setup as comp_setup,
)
from .resource import Root
from .sample import load_resources


@pytest.fixture
def sample_root() -> Root:
    d = Path(sample.__file__).parent / 'contents'
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
    template_dirs = [('wired_components.sample', 'templates')]
    configuration = Configuration(template_dirs=template_dirs)
    registry.register_singleton(configuration, IConfiguration)


@pytest.fixture
def renderer_setup(registry) -> None:
    """ Connect the renderer to the registry """

    from wired_components.renderer import wired_setup as renderer_setup
    renderer_setup(registry)


@pytest.fixture
def component_setup(registry):
    """ Top-level setup of component """
    comp_setup(registry)


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
