from traitlets.config import Configurable
from traitlets import (
    Integer,
)
from phylovega.traitlets import VegaConfigurable


class BaseTreeChart(VegaConfigurable):
    """Object for specifying chart styling.
    """
    width = Integer(500, help="Width of the tree chart.", config=True)
    height = Integer(500, help="Height of the tree chart.", config=True)
    padding = Integer(5, help="Padding around tree chart.", config=True)

    def get_spec(self):
        return { 
            'width' : self.width,
            'height': self.height,
            'padding': self.padding
        }
