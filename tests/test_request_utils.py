from typing import Tuple

#
import pytest


@pytest.mark.parametrize(
    'base, to, expected',
    [
        ('/', '/_static/base.css', '_static/base.css'),
        ('/about/', '/_static/base.css', '../_static/base.css'),
        ('/a/about/', '/_static/base.css', '../../_static/base.css'),
        ('/a/b/index/', '/_static/base.css', '../../../_static/base.css'),
        ('/a/b/about/', '/_static/base.css', '../../../_static/base.css'),
        ('/', '/', ''),
        ('/d1/', '/', '../'),
        ('/d1/', '/d1/', ''),
        ('/f1/f3/d3/', '/d1/', '../../../d1/'),
        ('/f1/f3/d3/', '/', '../../../'),
        ('/f1/f3/d3/', '/f1/', '../../'),
        ('/f1/f3/d3/', '/f1/f3/', '../'),
        ('/d1/', '/f1/f3/d3/', '../f1/f3/d3/'),
        ('/f1/f3/', '/', '../../'),
        ('/f1/f3/', '/f1/', '../'),
        ('/f1/f3/', '/f1/f3/d3/', 'd3/'),
        ('/', '/d1/', 'd1/'),
        ('/d1/', '/', '../'),
    ]
)
def test_relative_uri(base, to, expected):
    from wired_components.request.utils import relative_uri
    result = relative_uri(base, to)

    assert result == expected


@pytest.mark.parametrize(
    'path, expected',
    [
        ('/', '/'),
        ('/f1', '/f1/'),
        ('/f1/', '/f1/'),
        ('/d1', '/d1/'),
        ('/d1/', '/d1/'),
        ('/f1/d2', '/f1/d2/'),
        ('/f1/d2/', '/f1/d2/'),
        ('/f1/f3', '/f1/f3/'),
        ('/f1/f3/', '/f1/f3/'),
        ('/f1/f3/d3', '/f1/f3/d3/'),
        ('/f1/f3/d3/', '/f1/f3/d3/'),
    ]
)
def test_normalize_path(path: str, expected: str):
    from wired_components.request import normalize_path
    assert expected == normalize_path(path)


@pytest.mark.parametrize(
    'path, expected',
    [
        ('/', ''),
        ('/f1', 'f1'),
        ('/f1/', 'f1'),
        ('/d1', 'd1'),
        ('/d1/', 'd1'),
        ('/f1/d2', 'd2'),
        ('/f1/d2/', 'd2'),
        ('/f1/f3', 'f3'),
        ('/f1/f3/', 'f3'),
        ('/f1/f3/d3', 'd3'),
        ('/f1/f3/d3/', 'd3'),
    ]

)
def test_find_resource(sample_root, path: str, expected: str):
    from wired_components.request import find_resource
    resource = find_resource(sample_root, path)
    assert expected == resource.name


@pytest.mark.parametrize(
    'this_path, expected',
    (
            ('/', ()),
            ('/f1/', (
                    ('My Site', '/'),
            )),
            ('/d1', (
                    ('My Site', '/'),
            )),
            ('/f1/d2', (
                    ('My Site', '/'),
                    ('The Folder At The Root', '/f1/'),
            )),
            ('/f1/f3/', (
                    ('My Site', '/'),
                    ('The Folder At The Root', '/f1/'),
            )),
            ('/f1/f3/d3', (
                    ('My Site', '/'),
                    ('The Folder At The Root', '/f1/'),
                    ('F3 is in F1', '/f1/f3/'),
            )),
    )
)
def test_parents(
        sample_root, this_path: str, expected: Tuple[str],
):
    from wired_components.request import (
        find_resource,
        parents,
        resource_path,
    )
    resource = find_resource(sample_root, this_path)
    results = parents(resource)
    result = tuple(
        (
            (resource.title, resource_path(resource))
            for resource in results)
    )
    assert result == expected


@pytest.mark.parametrize(
    'target_path, expected',
    (
            ('/', '/'),
            ('/f1', '/f1/'),
            ('/f1/', '/f1/'),
            ('/d1', '/d1/'),
            ('/d1/', '/d1/'),
            ('/f1/d2', '/f1/d2/'),
            ('/f1/d2/', '/f1/d2/'),
            ('/f1/f3', '/f1/f3/'),
            ('/f1/f3/', '/f1/f3/'),
            ('/f1/f3/d3', '/f1/f3/d3/'),
            ('/f1/f3/d3/', '/f1/f3/d3/'),
    )
)
def test_resource_path(
        sample_root, target_path: str, expected: str,
):
    from wired_components.request import (
        find_resource,
        resource_path,
    )
    resource = find_resource(sample_root, target_path)
    path = resource_path(resource)
    assert expected == path


@pytest.mark.parametrize(
    'current_path, target_path, expected',
    [
        ('/', '/', ''),
        ('/d1/', '/', '../'),
        ('/d1/', '/d1/', ''),
        ('/f1/f3/d3/', '/d1', '../../../d1/'),
        ('/f1/f3/d3/', '/', '../../../'),
        ('/f1/f3/d3/', '/f1/', '../../'),
        ('/f1/f3/d3/', '/f1/f3/', '../'),
        ('/d1', '/f1/f3/d3/', '../f1/f3/d3/'),
        ('/f1/f3', '/', '../../'),
        ('/f1/f3', '/f1/', '../'),
        ('/f1/f3', '/f1/f3/d3', 'd3/'),
        ('/', '/d1', 'd1/'),
        ('/d1', '/', '../'),
    ]
)
def test_relative_path(
        sample_root, current_path: str, target_path: str,
        expected: str,
):
    from wired_components.request import (
        find_resource,
        relative_path,
    )
    current = find_resource(sample_root, current_path)
    target = find_resource(sample_root, target_path)
    result: str = relative_path(sample_root, current, target)
    assert result == expected


@pytest.mark.parametrize(
    'current_path, expected',
    [
        ('/f1/f3/d3/', '../../../../static/foo.css'),
        ('/f1/f3/d3/', '../../../../static/foo.css'),
        ('/d1', '../../static/foo.css'),
        ('/f1/f3', '../../../static/foo.css'),
        ('/', '../static/foo.css'),
        ('/d1', '../../static/foo.css'),
    ]
)
def test_static_relative_path(
        sample_root, current_path: str, expected: str,
):
    from wired_components.request import (
        find_resource,
        relative_static_path,
    )
    current = find_resource(sample_root, current_path)
    result: str = relative_static_path(current, 'static/foo.css')
    assert result == expected
