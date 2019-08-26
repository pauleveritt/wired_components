import pytest


@pytest.fixture
def registry():
    from wired import ServiceRegistry
    return ServiceRegistry()


def test_wired_setup(registry):
    from wired_components import wired_setup
    assert wired_setup(registry) is None
