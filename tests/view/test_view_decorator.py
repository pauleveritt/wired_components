from dataclasses import dataclass

from wired import ServiceRegistry, ServiceContainer


def test_view_decorator_function(
        registry: ServiceRegistry,
        view_container: ServiceContainer,
        sample_root,
        sample_view,
):
    from wired_components.resource import IDocument
    from wired_components.view import IView, View, register_view

    @dataclass
    class SomeView(View):
        flag: int = 99

    register_view(registry, SomeView, context=IDocument)

    # Get the view from the container
    view: SomeView = view_container.get(IView)

    # Assert some things
    assert isinstance(view, View)
    assert len(view.configuration.template_dirs) == 1
    assert view.context.title == 'A Doc At The Root'
    assert view.request.path == '/d1/'
    assert view.root.title == 'My Site'
    assert view.flag == 99
