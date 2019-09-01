from typing import Type, Callable

from venusian import Scanner
from wired import ServiceRegistry


class BaseDecorator:
    """ Subclass this to fill in the slots """

    for_: Type
    register_function: Callable

    def __init__(self, context: Type, name: str = None):
        self.for_ = self.for_
        self.context = context
        self.name = name

    def __call__(self, wrapped):
        from venusian import attach
        register_function = self.__class__.register_function

        def callback(scanner: Scanner, name: str, cls):
            registry: ServiceRegistry = getattr(scanner, 'registry')
            register_function(registry, cls, context=self.context)

        attach(wrapped, callback, category='goku')
        return wrapped
