from dataclasses import dataclass

import pytest
from wired import ServiceRegistry
from zope.interface import implementer


def test_component_register_component(
        registry: ServiceRegistry,
        simple_root,
):
    from wired_components.component import IComponent, register_component

    # Register a component
    @implementer(IComponent)
    @dataclass
    class SomeComponent:
        flag: int

    register_component(registry, SomeComponent)

    # Make a container with an IResource in it
    container = registry.create_container(context=simple_root)

    # Now get the component *class*
    component_class = container.get(IComponent, name='SomeComponent')

    # Try to make a component *instance*
    with pytest.raises(TypeError):
        # Requires a prop to be passed in
        component_class()

    # Now construct the component instance the correct way, with a prop
    component_instance: SomeComponent = component_class(flag=44)
    assert component_instance.flag == 44
