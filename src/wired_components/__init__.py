from wired import ServiceRegistry

from .component import wired_setup as component_setup
from .renderer import wired_setup as renderer_setup
from .request import wired_setup as request_setup
from .resource import wired_setup as resource_setup
from .scanner import wired_setup as scanner_setup


def wired_setup(registry: ServiceRegistry):
    component_setup(registry)
    renderer_setup(registry)
    request_setup(registry)
    resource_setup(registry)
    scanner_setup(registry)
