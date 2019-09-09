from typing import Type

from venusian import attach, Scanner
from wired import ServiceRegistry

from wired_components.resource import Resource


class component:
    def __init__(self, context: Type[Resource] = None):
        self.context = context

    def __call__(self, wrapped):
        from wired_components.component import register_component

        def callback(scanner: Scanner, name: str, cls):
            registry: ServiceRegistry = getattr(scanner, 'registry')

            register_component(
                registry,
                target=cls,
                context=self.context,
            )

        attach(wrapped, callback, category='wired_component')
        return wrapped
