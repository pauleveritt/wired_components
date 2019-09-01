from dataclasses import dataclass

import pytest
from wired import ServiceRegistry, ServiceContainer

# Break the rules on "don't import from wired_components at
# global scope" because we need them for the parametrize
from wired_components.resource import (
    IDocument,
    IResource,
)


@pytest.mark.parametrize(
    'interface',
    (
            'ignore',
            IResource,
            IDocument,
    )
)
def test_view_decorator_function(
        registry: ServiceRegistry,
        view_container: ServiceContainer,
        simple_root,
        interface,
):
    # Test a view registered for all resources
    from wired_components.view import IView, View, register_view

    @dataclass
    class SomeView(View):
        flag: int = 99

    if interface == 'ignore':
        # Simulate omitting the ``context=`` argument
        register_view(registry, SomeView)
    else:
        register_view(registry, SomeView, context=interface)

    # Get the view from the container
    view: SomeView = view_container.get(IView)

    # Assert some things
    assert isinstance(view, View)
    assert len(view.configuration.template_dirs) == 1
    assert view.context.title == 'A Doc At The Root'
    assert view.request.path == '/d1/'
    assert view.root.title == 'My Site'
    assert view.flag == 99
