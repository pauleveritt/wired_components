from typing import List, Tuple, Optional

from jinja2 import Environment, ChoiceLoader


class JinjaEnvironment(Environment):
    """ Use PackageLoader to manage a series of template directories """

    dirs = Optional[List[Tuple[str, str]]]

    def __init__(self):
        self.dirs = []
        loader = ChoiceLoader(self.dirs)
        super().__init__(loader=loader)
