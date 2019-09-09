from wired import ServiceRegistry


def test_view_wired_setup(registry: ServiceRegistry):
    from wired_components.view import wired_setup
    assert wired_setup(registry) is None


def test_view_instance(registry, view_container, simple_root, sample_view):
    # Get the view from the container
    from wired_components.view import IView, View
    view: View = view_container.get(IView)

    # See if we're constructed correctly
    assert len(view.configuration.template_dirs) == 1
    assert view.context.title == 'A Doc At The Root'
    assert view.root.title == 'My Site'
    assert view.parents[0].title == 'My Site'


def test_view_as_dict(registry, view_container, simple_root, sample_view):
    # Get the view from the container
    from wired_components.view import IView, View
    view: View = view_container.get(IView)

    results = view.as_dict()
    assert 'configuration' in results
    assert 'context' in results
    assert 'request' in results
    assert 'root' in results
    assert 'view' in results

    # TODO wired bring this back when wired.dataclasses gets support for
    #   init=False
    # assert 'parents' in results
