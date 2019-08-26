"""

System configuration object.

In ``wired_components``, well-known services are available at well-known
places. They are also replaceable with alternate implementations.

Since some services need a configuration system prior to startup,
``wired_components`` provides a built-in configuration object. It has
values reflecting what the other parts of ``wired_components`` need.
If your pluggable app needs more, just register a different implementation.

"""
from wired import ServiceRegistry

from .models import IConfiguration, Configuration


def wired_setup(registry: ServiceRegistry):
    pass


__all__ = [
    'wired_setup',
    'IConfiguration',
    'Configuration',
]
