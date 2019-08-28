"""

Scanner for decorators in wired_component, add-ons, and project.

We use a (``venusian.Scanner``) object to look for decorators post-import
time. We'd like the same object to be findable whether in ``wired_components``,
an add-on package, or a custom project.

"Always trust the container". This package makes an instance which is
registered as a singleton in the container and can be looked up at an
interface, easy-peasy, with ``container.get(IScanner)``.

"""
from wired import ServiceRegistry

from .models import IScanner, WiredScanner


def wired_setup(registry: ServiceRegistry):
    scanner = WiredScanner(registry=registry)
    registry.register_singleton(scanner, IScanner)


__all__ = [
    'wired_setup',
    'IScanner',
    'WiredScanner',
]
