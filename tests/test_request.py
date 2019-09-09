import pytest
from wired import ServiceContainer


@pytest.fixture
def request_container(registry, simple_root) -> ServiceContainer:
    from wired_components.request import wired_setup as request_setup
    from wired_components.resource import IRoot

    # Outside system puts some things in the registry
    registry.register_singleton(simple_root, IRoot)
    request_setup(registry)

    # Make a container and return it
    container: ServiceContainer = registry.create_container(
        context=simple_root
    )
    return container


def test_request_wired_setup(registry):
    from wired_components.request import wired_setup
    assert wired_setup(registry) is None


def test_request_instance(registry, request_container, simple_root):
    # Get the request from the container
    from wired_components.request import IRequest, Request
    request: Request = request_container.get(IRequest)

    # See if we're constructed correctly
    assert request.context.title == 'My Site'
    assert request.root == simple_root
