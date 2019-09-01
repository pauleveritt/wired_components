import pytest

pytest_plugins = [
    'wired_components.fixtures'
]


@pytest.fixture
def registry():
    from wired import ServiceRegistry
    return ServiceRegistry()
