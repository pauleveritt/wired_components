from dataclasses import dataclass, field

from jinja2 import ChoiceLoader, Environment, Template, PackageLoader
from markupsafe import Markup
from wired.dataclasses import injected
from zope.interface import Interface, implementer

from wired_components.configuration import TemplateDirs
from ..configuration import IConfiguration


class IJinjaRenderer(Interface):
    """ Marker for getting a Jinja2 environment and renderer"""


@implementer(IJinjaRenderer)
@dataclass
class JinjaRenderer:
    template_dirs: TemplateDirs = injected(IConfiguration, attr='template_dirs')
    environment: Environment = field(init=False)

    def __post_init__(self):
        choice_loader = ChoiceLoader(
            [
                PackageLoader(template_dir[0], template_dir[1])
                for template_dir in self.template_dirs
            ]
        )
        self.environment = Environment(loader=choice_loader)

    def render(
            self, context, template_name: str,
    ) -> Markup:
        """ Given a dataclass, flatten it and render with jinja2 template """

        template: Template = self.environment.get_or_select_template(
            template_name
        )
        result = template.render(**context)
        m = Markup(result)
        return m
