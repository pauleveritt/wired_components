from dataclasses import dataclass

from wired.dataclasses import injected, Context

from wired_components.resource import Root, Collection, Document
from wired_components.view import view


@view(context=Root)
@dataclass
class RootView:
    title: str = injected(Context, attr='title')
    template: str = 'rootview.jinja2'


@view(context=Collection)
@dataclass
class CollectionView:
    title: str = injected(Context, attr='title')
    template: str = 'collectionview.jinja2'


@view(context=Document)
@dataclass
class DocumentView:
    title: str = injected(Context, attr='title')
    template: str = 'documentview.jinja2'
