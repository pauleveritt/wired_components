from wired import ServiceRegistry

from wired_components.fixtures import SomeView


def test_view_wired_setup(registry: ServiceRegistry):
    from wired_components.view import wired_setup
    assert wired_setup(registry) is None


def test_view_instance(registry, view_container, simple_root, sample_view):
    # Get the view from the container
    from wired_components.view import IView, View
    view: SomeView = view_container.get(IView)

    # See if we're constructed correctly
    assert view.flag == 'someview'


def test_view_as_dict(registry, view_container, simple_root, sample_view):
    # Get the view from the container
    from wired_components.view import IView, View, as_dict
    view: View = view_container.get(IView)

    results = as_dict(view)
    assert 'flag' in results
