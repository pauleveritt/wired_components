from typing import Type, Callable

from venusian import Scanner
from wired import ServiceRegistry
from wired.dataclasses import register_dataclass


class BaseDecorator:
    """ Subclass this to fill in the slots """

    for_: Type
    register_function: Callable

    def __init__(self, context: Type = None, name: str = None):
        self.for_ = self.for_
        self.context = context
        self.name = name

    def __call__(self, wrapped):
        from venusian import attach

        def callback(scanner: Scanner, name: str, cls):
            registry: ServiceRegistry = getattr(scanner, 'registry')

            register_dataclass(
                registry,
                cls,
                for_=self.for_,
                context=self.context,
                # name=self.name,
            )

        attach(wrapped, callback, category='goku')
        return wrapped
