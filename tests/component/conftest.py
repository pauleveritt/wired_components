import pytest
from wired import ServiceContainer


@pytest.fixture
def app_container(
        registry,
        register_breadcrumb,
        sample_root,
        component_setup,
) -> ServiceContainer:
    container = registry.create_container()
    return container


@pytest.fixture
def txn_container(
        registry,
        configuration_setup,
        renderer_setup,
        register_breadcrumb,
        sample_root,
        component_setup,
) -> ServiceContainer:
    container = registry.create_container(context=sample_root)
    return container
