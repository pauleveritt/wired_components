from pathlib import Path

import pytest

from wired_components import sample
from wired_components.resource import Root
from wired_components.sample import load_resources


@pytest.fixture
def sample_root() -> Root:
    d = Path(sample.__file__).parent
    root: Root = load_resources(d)
    return root
