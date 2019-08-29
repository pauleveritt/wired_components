"""

Sample data for tests and demos.

We need sample data: resource trees, templates, almost like a working
application. We need it to be convenient to work with and refactor.
Rather than a big pile of Python or JSON, we'll use YAML and parse
into some classes.

Not doing anything exotic (e.g. strictyaml, pydantic.)

"""

from .loader import load_resources

__all__ = [
    'load_resources',
]
