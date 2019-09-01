import pytest
from markupsafe import Markup
from wired import ServiceRegistry, ServiceContainer


@pytest.fixture
def renderer_container(registry) -> ServiceContainer:
    from wired_components.configuration import IConfiguration, Configuration
    template_dirs = [('wired_components.samples.simple', 'templates')]
    configuration = Configuration(template_dirs=template_dirs)
    container = registry.create_container()
    container.register_singleton(configuration, IConfiguration)

    # Now do wired_setup
    from wired_components.renderer import wired_setup
    wired_setup(registry)

    return container


@pytest.fixture
def this_renderer(renderer_container):
    from wired_components.renderer import IJinjaRenderer, JinjaRenderer

    # Finally, try to get one
    renderer: JinjaRenderer = renderer_container.get(IJinjaRenderer)
    return renderer


def test_renderer_wired_setup(registry: ServiceRegistry):
    from wired_components.renderer import wired_setup
    assert wired_setup(registry) is None


def test_renderer_construction():
    from wired_components.renderer import JinjaRenderer
    template_dirs = [('wired_components.samples.simple', 'templates')]
    renderer = JinjaRenderer(template_dirs=template_dirs)
    from jinja2 import Environment
    assert isinstance(renderer.environment, Environment)


def test_renderer_injection(this_renderer):
    assert len(this_renderer.template_dirs) == 1


def test_renderer_render(this_renderer):
    context = dict(label='somelabel')
    template_name = 'breadcrumb.jinja2'
    result: Markup = this_renderer.render(
        context, template_name=template_name,
    )
    assert result == 'label is somelabel'
