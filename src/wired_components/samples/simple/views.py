from dataclasses import dataclass

from wired.dataclasses import injected, Context

from wired_components.resource import Root
from wired_components.view import view


@view(context=Root)
@dataclass
class RootView:
    title: str = injected(Context, attr='title')
    template: str = 'rootview.jinja2'
