def test_resource_wired_setup(registry):
    from wired_components.resource import wired_setup
    assert wired_setup(registry) is None


def test_resource_construction():
    from wired_components.resource import Resource
    resource = Resource(
        name='name1', parent=None, title='title1', body='body1'
    )
    assert resource.name == 'name1'
    assert resource.parent is None
    assert resource.title == 'title1'
    assert resource.body == 'body1'
    assert resource.__name__ == 'name1'
    assert resource.__parent__ is None


def test_collection_construction():
    from wired_components.resource import Collection
    collection = Collection(
        name='name1', parent=None, title='title1', body='body1'
    )
    assert collection.name == 'name1'
    assert collection.parent is None
    assert collection.title == 'title1'
    assert collection.body == 'body1'
    assert collection.__name__ == 'name1'
    assert collection.__parent__ is None


def test_root_construction():
    from wired_components.resource import Root
    root = Root(
        name='name1', parent=None, title='title1', body='body1'
    )
    assert root.name == 'name1'
    assert root.parent is None
    assert root.title == 'title1'
    assert root.body == 'body1'
    assert root.__name__ == 'name1'
    assert root.__parent__ is None
