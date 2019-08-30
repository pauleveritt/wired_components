def test_make_context(txn_container):
    from wired_components.component import make_context

    context = make_context(txn_container, 'Breadcrumb', label='somelabel')
    assert 'Breadcrumb' in context
    assert context['label'] == 'somelabel'
