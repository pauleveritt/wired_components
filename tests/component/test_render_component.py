def test_render_component(txn_container):
    from wired_components.component import render_component
    result = render_component(
        txn_container,
        'Breadcrumb',
        label='somelabel9'
    )
    assert result == 'label is somelabel9'
