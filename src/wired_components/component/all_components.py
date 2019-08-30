"""

List all registered components.

Various places in the system need a fast dump of all the IComponent
entries. We want a factory which generates this once per-container.
It is registered on the registry, so it is only registered once at
application startup. But its *result* is cached through the lifetime
of a request container.

Currently using zope.interface subscriptions.

Done with single-responsibility-principle in mind.

"""

from typing import Dict, Type

from wired import ServiceContainer
from zope.interface import Interface

from wired_components.resource import IResource
from .models import IComponent


class IAllComponents(Interface):
    """ Mapping of all known components in registry """


def all_components(container: ServiceContainer) -> Dict[str, Type]:
    """ Use zope.interface subscriptions to get known components """
    factories = getattr(container, '_factories')
    subscriptions = {
        component.__name__: component
        for component in factories.subscriptions(
            [IResource], IComponent
        )
    }
    return subscriptions
