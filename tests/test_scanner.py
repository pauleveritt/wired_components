import pytest
from wired import ServiceContainer


@pytest.fixture
def scanner_container(registry) -> ServiceContainer:
    # Put the scanner in the registry
    from wired_components.scanner import wired_setup
    wired_setup(registry)

    # Make a container and return it
    container: ServiceContainer = registry.create_container()
    return container


def test_scanner_wired_setup(registry):
    from wired_components import wired_setup
    assert wired_setup(registry) is None


def test_scanner_container_instance(registry, scanner_container):
    from wired_components.scanner import IScanner, WiredScanner
    scanner: WiredScanner = scanner_container.get(IScanner)
    assert scanner.registry == registry
