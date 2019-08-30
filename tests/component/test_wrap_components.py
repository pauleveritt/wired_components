from zope.interface import directlyProvides


def test_wrap_components(app_container):
    from wired_components.component import IWrapComponents

    wrapped_components = app_container.get(IWrapComponents)
    breadcrumb_wrapper = wrapped_components['Breadcrumb']
    keywords = breadcrumb_wrapper.keywords
    assert keywords['component_name'] == 'Breadcrumb'


def test_wrap_components_run_once(app_container, registry):
    from wired_components.component import IWrapComponents
    from wired_components.fixtures import Breadcrumb

    wrapped_components = app_container.get(IWrapComponents)
    assert len(wrapped_components) == 1

    # Add another component
    from wired_components.component import IComponent
    directlyProvides(Breadcrumb, IComponent)
    from wired_components.component import register_component
    register_component(registry, Breadcrumb)

    wrapped_components = app_container.get(IWrapComponents)
    assert len(wrapped_components) == 1
