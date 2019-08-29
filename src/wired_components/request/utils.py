"""

Mimic the various Pyramid path helpers.

"""
from typing import Union, Optional, List

from wired_components.resource import Root, Resource

SEP = "/"


# Taken from Sphinx
def relative_uri(base: str, to: str):
    """Return a relative URL from ``base`` to ``to``."""

    # if to.startswith(SEP):
    #     return to
    b2 = base.split(SEP)
    t2 = to.split(SEP)
    # remove common segments (except the last segment)
    for x, y in zip(b2[:-1], t2[:-1]):
        if x != y:
            break
        b2.pop(0)
        t2.pop(0)
    if b2 == t2:
        # Special case: relative_uri('f/index.html','f/index.html')
        # returns '', not 'index.html'
        return ''
    if len(b2) == 1 and t2 == ['']:
        # Special case: relative_uri('f/index.html','f/') should
        # return './', not ''
        return '.' + SEP
    prefix = ('..' + SEP) * (len(b2) - 1)
    main_path = SEP.join(t2)
    result = prefix + main_path
    return result


def normalize_path(path: str) -> str:
    """ All paths should end with a slash """
    if not path.endswith('/'):
        path += '/'
    return path


def find_resource(root: Root, path: str) -> Resource:
    if path == '/' or path == '/.':
        return root
    path = normalize_path(path)
    items = iter(path[1:-1].split('/'))
    resource = root
    while True:
        try:
            current = next(items)
            resource = resource[current]
        except StopIteration:
            return resource


def parents(resource: Resource) -> List[Optional[Resource]]:
    these_parents: List[Optional[Resource]] = []
    parent = resource.parent
    while parent is not None:
        these_parents.append(parent)
        parent = parent.parent
    return list(reversed(these_parents))


def resource_path(resource: Resource) -> str:
    """ Give a slash-separated representation of resource w/ trailing / """

    # Bail out quickly if we are the root or in the root
    if resource.parent is None:
        return '/'
    elif resource.parent.parent is None:
        return '/' + resource.name + '/'

    # The root is '' so skip it
    resource_parents = parents(resource)

    # Get the names for each parent, then join with slashes
    resource_parent_names = [p.name for p in resource_parents if p]
    path = '/'.join(resource_parent_names) + '/' + resource.name + '/'
    return path


def relative_path(
        root: Root, current: Resource, target: Union[Resource, str],
) -> str:
    """ Given current resource, generate relative path to target """

    # First, if the target is a string path, get the resource
    if isinstance(target, str):
        target = find_resource(root, normalize_path(target))

    result = relative_uri(
        base=resource_path(current),
        to=resource_path(target)
    )
    return result


def relative_static_path(current: Resource, target: str):
    # Bail out quickly if we are the root or in the root
    current_path = resource_path(current)
    target_path = target
    result = relative_uri(current_path, target_path)
    return result
