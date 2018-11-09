from traitlets import (
    HasTraits,
    Integer,
)

class BaseTreeChart(HasTraits):
    """Object for specifying chart styling.
    """
    width = Integer(500, help="Width of the tree chart.")
    height = Integer(500, help="Height of the tree chart.")
    padding = Integer(5, help="Padding around tree chart.")

    def get_spec(self):
        return { 
            'width' : self.width,
            'height': self.height,
            'padding': self.padding
        }
