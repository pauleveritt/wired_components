from pathlib import Path

from yaml import Loader, load

from wired_components.request import find_resource
from wired_components.resource import Root, Collection, Document


def load_yaml(fn: Path):
    with open(str(fn), 'r') as f:
        data = load(f, Loader=Loader)
        return data


def load_resources(contents: Path) -> Root:
    # Make the root resource
    root_yaml = load_yaml(contents / 'index.yaml')
    root_yaml.pop('type')
    root = Root(name='', parent=None, **root_yaml)

    # Next do all the folders by finding all 'index.yaml'
    for resource in Path(contents).glob('**/index.yaml'):
        if resource.parent == contents:
            # We hit top-level index.yaml which we already used for root
            continue

        # Load yaml for this folder and make an instance
        folder_yaml = load_yaml(resource)

        # Find the parent folder, which should already be in root
        parent_path = resource.parents[1].relative_to(contents)
        if str(parent_path) == '.':
            parent_path = Path('')
        parent = find_resource(root, '/' + str(parent_path))
        folder_name = str(resource.parent.stem)
        folder_yaml.pop('type')
        folder = Collection(name=folder_name, parent=parent, **folder_yaml)
        parent[folder_name] = folder

    # Finally, do all the documents, now that we have a place to put them
    for resource in Path(contents).glob('**/*.yaml'):
        if resource.name == 'index.yaml':
            # Skip this, we already did it
            continue
        resource_yaml = load_yaml(resource)
        resource_yaml.pop('type')
        name = str(resource.stem)

        # Get the parent via resource path
        parent_path = resource.parent.relative_to(contents)
        parent = find_resource(root, '/' + str(parent_path))
        resource = Document(name=name, parent=parent, **resource_yaml)
        parent[name] = resource

    return root
