import pytest
from wired import ServiceContainer, ServiceRegistry


@pytest.fixture
def view_container(
        registry: ServiceRegistry,
        root_setup,
        simple_root,
        request_setup,
        configuration_setup,
) -> ServiceContainer:
    # Make a container and return it
    container: ServiceContainer = registry.create_container(
        context=simple_root['d1']
    )
    return container


@pytest.fixture
def sample_view(registry: ServiceRegistry) -> None:
    """ Put one view in the registry """

    from wired_components.view import View, register_view
    from wired_components.resource import IResource
    register_view(registry, View, context=IResource)
