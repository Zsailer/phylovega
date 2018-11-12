from traitlets.config import Configurable
from traitlets import (
    Integer,
    default
)
from phylovega.traitlets import VegaConfigurable


class BaseTreeChart(VegaConfigurable):
    """Object for specifying chart styling.
    """
    padding = Integer(5, help="Padding around tree chart.", config=True)
    width = Integer(300, help="Width of the tree chart.", config=True)

    height = Integer(help="Height of the tree chart.", config=True)

    @default('height')
    def _default_height(self):
        leafs = [el for el in self.data if el['type'] == 'leaf']
        return len(leafs) * 12

    def __init__(self, data, config=None, **kwargs):
        super().__init__(config=config, **kwargs)
        self.data = data

    def get_spec(self):
        return { 
            'width' : self.width,
            'height': self.height,
            'padding': self.padding,
            'autosize': 'fit'
        }
