"""

Interface and base model for Url.

Systems can provide alternate implementations of Url. The interface and
dataclass here give a starting point.

"""

from dataclasses import dataclass

from zope.interface import Attribute, Interface, implementer


class IUrl(Interface):
    """ Information from the outside system about the current request """

    path = Attribute('Filename or URL path for the current URL resource')


@implementer(IUrl)
@dataclass
class Url:
    path: str
