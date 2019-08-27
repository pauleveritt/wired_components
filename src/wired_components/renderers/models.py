from dataclasses import dataclass, field

from jinja2 import ChoiceLoader, Environment
from wired.dataclasses import injected, factory
from zope.interface import Interface, implementer

from wired_components.configuration import TemplateDirs
from ..configuration import IConfiguration


class IJinjaRenderer(Interface):
    """ Marker for getting a Jinja2 environment and renderer"""


@implementer(IJinjaRenderer)
@factory()
@dataclass
class JinjaRenderer:
    template_dirs: TemplateDirs = injected(IConfiguration, attr='template_dirs')
    environment: Environment = field(init=False)

    def __post_init__(self):
        choice_loader = ChoiceLoader(self.template_dirs)
        self.environment = Environment(loader=choice_loader)
