from wired import ServiceRegistry

from .component import wired_setup as component_setup
from .renderer import wired_setup as renderer_setup
from .request import wired_setup as request_setup


def wired_setup(registry: ServiceRegistry):
    component_setup(registry)
    renderer_setup(registry)
    request_setup(registry)
