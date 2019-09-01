def test_construction():
    from wired_components.resource import resource, IDocument

    r = resource(for_=IDocument)
    assert r.for_ == IDocument
    assert r.context is None
    assert r.name is None
