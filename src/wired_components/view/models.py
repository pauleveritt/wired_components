from dataclasses import dataclass
from typing import Dict, get_type_hints, Any

from zope.interface import Interface


class IView(Interface):
    """ Gather state and logic needed to render a request/resource """

    pass


@dataclass
class View:
    pass


def as_dict(view: View) -> Dict[str, Any]:
    # Return a flattened dictionary as context keys for each field.
    fields = get_type_hints(view.__class__)
    context = {name: getattr(view, name) for name, field in fields.items()}

    # Add this view instance in as something available in the context
    context['view'] = view
    return context
