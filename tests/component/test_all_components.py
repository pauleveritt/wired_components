from zope.interface import directlyProvides


def test_all_components(app_container):
    from wired_components.component import IAllComponents
    from wired_components.fixtures import Breadcrumb

    components = app_container.get(IAllComponents)
    assert components['Breadcrumb'] == Breadcrumb


def test_all_components_run_once(app_container, registry):
    # Confirm that this factory is only run once per container
    from wired_components.component import IAllComponents
    from wired_components.fixtures import Breadcrumb

    components = app_container.get(IAllComponents)
    assert len(components) == 1

    # Add another component
    from wired_components.component import IComponent
    directlyProvides(Breadcrumb, IComponent)
    from wired_components.component import register_component
    register_component(registry, Breadcrumb)

    # Doesn't show up
    components2 = app_container.get(IAllComponents)
    assert len(components2) == 1
