"""

Singleton representing URL information for the current request.

Processing a request, getting a view, rendering a component, generating
a response...all this has to start somewhere. This singleton represents
the incoming information, such as a Markdown file on disk or a URL path,
being provided by the outside system.

As such, it is a singleton added to the per-request container by the
outside system. When you integrate ``wired_components`` with Sphinx,
Pyramid, etc. you have to make one of these.

"""

from wired import ServiceRegistry

from .models import IUrl, Url


def wired_setup(registry: ServiceRegistry):
    pass


__all__ = [
    'wired_setup',
    'IUrl',
    'Url',
]
