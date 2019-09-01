import pytest
from wired import ServiceContainer, ServiceRegistry


@pytest.fixture
def resource_container(
        registry: ServiceRegistry,
        root_setup,
        sample_root,
        request_setup,
        configuration_setup,
) -> ServiceContainer:
    from wired_components.url import IUrl, Url

    # Make a container and return it
    container: ServiceContainer = registry.create_container(
        context=sample_root['d1']
    )
    url = Url(path='/d1/')
    container.register_singleton(url, IUrl)
    return container
