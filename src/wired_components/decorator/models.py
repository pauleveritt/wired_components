from typing import Type, Callable

from venusian import Scanner
from wired import ServiceRegistry
from wired.dataclasses import register_dataclass


class BaseDecorator:
    """ Subclass this to fill in the slots """

    for_: Type
    register_function: Callable

    def __init__(
            self, for_: Type = None, context: Type = None, name: str = None
    ):
        # Some decorators (e.g. resource) require a ``for_`` in their
        # usage, as one decorator covers lots of classes. Others
        # (e.g. ``view``) provide the ``for_`` once, as a a class attribute.
        self.for_ = for_ if for_ else self.for_
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

        attach(wrapped, callback, category='wired_component')
        return wrapped
