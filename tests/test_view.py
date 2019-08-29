import pytest
from wired import ServiceContainer, ServiceRegistry


@pytest.fixture
def configuration():
    import wired_components
    from wired_components.configuration import Configuration
    template_dirs = [(wired_components, 'configuration')]
    configuration = Configuration(template_dirs=template_dirs)
    return configuration


@pytest.fixture
def view_container(registry, sample_root, configuration) -> ServiceContainer:
    from wired_components.configuration import IConfiguration
    from wired_components.request import wired_setup as request_setup
    from wired_components.resource import IRoot
    from wired_components.url import IUrl, Url
    from wired_components.view import wired_setup as view_setup

    # Outside system puts some things in the registry
    registry.register_singleton(configuration, IConfiguration)
    registry.register_singleton(sample_root, IRoot)
    request_setup(registry)
    view_setup(registry)

    # Make a container and return it
    container: ServiceContainer = registry.create_container(
        context=sample_root
    )
    url = Url(path='somepath')
    container.register_singleton(url, IUrl)
    return container


def test_view_wired_setup(registry: ServiceRegistry):
    from wired_components.view import wired_setup
    assert wired_setup(registry) is None


def test_view_instance(registry, view_container, sample_root):
    # Get the view from the container
    from wired_components.view import IView, View
    view: View = view_container.get(IView)

    # See if we're constructed correctly
    assert len(view.configuration.template_dirs) == 1
    assert view.context.title == 'My Site'
    assert view.request.path == 'somepath'
    assert view.root.title == 'My Site'
    assert view.parents == []


def test_view_as_dict(registry, view_container, sample_root):
    # Get the view from the container
    from wired_components.view import IView, View
    view: View = view_container.get(IView)

    results = view.as_dict()
    assert 'configuration' in results
    assert 'context' in results
    assert 'request' in results
    assert 'root' in results
    assert 'parents' in results
    assert 'view' in results
