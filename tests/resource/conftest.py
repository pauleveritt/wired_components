import pytest
from wired import ServiceContainer, ServiceRegistry


@pytest.fixture
def resource_container(
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
