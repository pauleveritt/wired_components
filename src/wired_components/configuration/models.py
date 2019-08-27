from dataclasses import dataclass, field
from importlib.resources import Package, Resource
from typing import List, Optional, Tuple

from zope.interface import Interface, Attribute, implementer

PackageResource = Tuple[Package, Resource]
TemplateDirs = Optional[List[PackageResource]]


class IConfiguration(Interface):
    """ The configuration object """

    template_dirs = Attribute('Package directories where Jinja2 looks for templates')


@implementer(IConfiguration)
@dataclass
class Configuration:
    # ``template_dir`` is a list of strings with a colon separat
    template_dirs: TemplateDirs = None
