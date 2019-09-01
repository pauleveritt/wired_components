"""

Base decorator support.

Making each piece in ``wired.components`` into a decorator is essential
to adoption. People don't want to wire things together. Let's make it
easy to write custom dataclass-DI-style decorators, then provides some.

"""

from .models import BaseDecorator

__all__ = [
    'BaseDecorator',
]