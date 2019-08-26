import pytest


@pytest.fixture
def registry():
    from wired import ServiceRegistry
    return ServiceRegistry()
