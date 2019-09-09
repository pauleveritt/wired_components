from dataclasses import dataclass, field
from typing import Dict, Type

from jinja2 import ChoiceLoader, Environment, Template, PackageLoader
from markupsafe import Markup
from wired import ServiceContainer
from wired.dataclasses import injected
from zope.interface import Interface, implementer

from ..configuration import IConfiguration, TemplateDirs


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
            self, context: Dict, template_name: str,
            container: ServiceContainer
    ) -> Markup:
        """ Given a dataclass, flatten it and render with jinja2 template """

        # Always put the wrapped components into the template context
        from ..component import IWrapComponents
        wrapped_components: Dict[str, Type] = container.get(IWrapComponents)

        context.update(wrapped_components)

        template: Template = self.environment.get_or_select_template(
            template_name
        )
        result = template.render(**context)
        m = Markup(result)
        return m
