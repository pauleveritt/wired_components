from dataclasses import dataclass

from wired_components.component import component


@component()
@dataclass
class Breadcrumb:
    label: str
