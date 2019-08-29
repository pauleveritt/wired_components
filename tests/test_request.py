import pytest
from wired import ServiceContainer


@pytest.fixture
def request_container(registry, sample_root) -> ServiceContainer:
    from wired_components.resource import IResource, IRoot
    from wired_components.url import IUrl, Url

    # Requests need some things in the container
    registry.register_singleton(sample_root, IRoot)
    url = Url(path='somepath')

    # Put the request in the registry
    from wired_components.request import wired_setup
    wired_setup(registry)

    # Make a container and return it
    container: ServiceContainer = registry.create_container(
        context=sample_root
    )
    container.register_singleton(url, IUrl)
    return container


def test_request_wired_setup(registry):
    from wired_components.request import wired_setup
    assert wired_setup(registry) is None


def test_request_container_instance(registry, request_container, sample_root):
    from wired_components.request import IRequest, Request

    request: Request = request_container.get(IRequest)
    assert request.context.name == ''
    assert request.path == 'somepath'
    assert request.root == sample_root
