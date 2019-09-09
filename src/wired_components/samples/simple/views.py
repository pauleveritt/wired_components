from dataclasses import dataclass

from wired.dataclasses import injected

from wired_components.resource import IResource, Root
from wired_components.view import View, view


@view(context=Root)
@dataclass
class RootView(View):
    title: str = injected(IResource, attr='title')
    template: str = 'rootview.jinja2'
