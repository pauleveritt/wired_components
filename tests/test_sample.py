from pathlib import Path

from wired_components.resource import Root


def test_load_yaml(mocker):
    from wired_components.samples.simple import load_yaml
    yaml_string = """\
- title: Dummy Page
"""
    mocker.patch(
        'builtins.open', mocker.mock_open(read_data=yaml_string)
    )
    fn = Path('dummy_resources.yaml')
    data = load_yaml(fn)
    assert 'Dummy Page' == data[0]['title']


def test_load_resources_root(simple_root: Root):
    assert simple_root.name == ''
    assert simple_root.parent is None
    assert simple_root['f1'].name == 'f1'
    assert simple_root['f1'].parent == simple_root
    assert simple_root['d1'].name == 'd1'
    assert simple_root['d1'].parent == simple_root
