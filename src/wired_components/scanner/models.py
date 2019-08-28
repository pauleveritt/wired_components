from dataclasses import dataclass
from types import ModuleType

from venusian import Scanner
from wired import ServiceRegistry
from zope.interface import Interface, implementer


class IScanner(Interface):
    """ A decorator scanner """

    def scan(target: ModuleType) -> None:
        """ Look in a module for decorators """


@implementer(IScanner)
@dataclass
class WiredScanner(Scanner):
    registry: ServiceRegistry
