import pytest
from wired import ServiceContainer, ServiceRegistry


@pytest.fixture
def view_container(
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


@pytest.fixture
def sample_view(registry: ServiceRegistry) -> None:
    """ Put one view in the registry """

    from wired_components.view import View, register_view
    from wired_components.resource import IDocument
    register_view(registry, View, context=IDocument)
