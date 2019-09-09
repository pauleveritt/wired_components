import pytest
from markupsafe import Markup


@pytest.fixture
def app(registry) -> None:
    from wired_components.samples.simple import wired_setup
    wired_setup(registry)


def test_homepage(registry, app, simple_root):
    from wired_components.renderer import IJinjaRenderer, JinjaRenderer
    from wired_components.view import IView, View

    context = simple_root
    container = registry.create_container(context=context)

    # Get the view for root
    view: View = container.get(IView)


    renderer: JinjaRenderer = container.get(IJinjaRenderer)
    context = view.as_dict()
    template_name = view.template
    result: Markup = renderer.render(
        context, template_name=template_name,
    )

    assert result == '<div>Root: My Site</div>'