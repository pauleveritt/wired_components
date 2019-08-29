from pathlib import Path

from wired_components.resource import Root


def test_load_yaml(mocker):
    from wired_components.sample.loader import load_yaml
    yaml_string = """\
- title: Dummy Page
"""
    mocker.patch(
        'builtins.open', mocker.mock_open(read_data=yaml_string)
    )
    fn = Path('dummy_resources.yaml')
    data = load_yaml(fn)
    assert 'Dummy Page' == data[0]['title']


def test_load_resources_root(sample_root: Root):
    assert sample_root.name == ''
    assert sample_root.parent is None
    assert sample_root['f1'].name == 'f1'
    assert sample_root['f1'].parent == sample_root
    assert sample_root['d1'].name == 'd1'
    assert sample_root['d1'].parent == sample_root
