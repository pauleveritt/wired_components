from wired import ServiceRegistry
from wired.dataclasses import register_dataclass


def test_renderers_wired_setup(registry: ServiceRegistry):
    from wired_components.renderers import wired_setup
    assert wired_setup(registry) is None


def test_renderers_construction():
    import wired_components
    from wired_components.renderers import JinjaRenderer
    template_dirs = [(wired_components, 'configuration')]
    renderer = JinjaRenderer(template_dirs=template_dirs)
    from jinja2 import Environment
    assert isinstance(renderer.environment, Environment)


def test_renderers_injection(registry):
    # See if configuration is gotten from a container

    # Make a container with IConfiguration wired up
    import wired_components
    from wired_components.configuration import IConfiguration, Configuration
    template_dirs = [(wired_components, 'configuration')]
    configuration = Configuration(template_dirs=template_dirs)
    container = registry.create_container()
    container.register_singleton(configuration, IConfiguration)

    # Now wire up JinjaRenderer
    from wired_components.renderers import IJinjaRenderer, JinjaRenderer
    register_dataclass(registry, JinjaRenderer, for_=IJinjaRenderer)

    # Finally, try to get one
    renderer = container.get(IJinjaRenderer)
    assert renderer.template_dirs == template_dirs
