__doc__ = """Base module for defining a Vega specification.
"""

from traitlets import HasTraits
from traitlets import default, Int, Unicode


class Specification(HasTraits):
    """Base Vega specification object"""

    def get_specification(self):
        """Return the specification for this object."""
        return {name: getattr(self, name) for name in self.trait_names()}


class TopLevelSpec(Specification):
    """Top level Vega specification.

    Attributes
    ----------
    description:

    background:
    """
    width = Int(help="width of window.")

    @default('width')
    def _width_default(self):
        return 500

    height = Int(help="height of window.")

    @default('height')
    def _height_default(self):
        return 200

    description = Unicode(
        "Phylogenetic Tree.",
        help="A text description of the visualization")

    background = Unicode(help="Background color.")

    padding = Int(
        5,
        help="The padding in pixels to add around the visualization.")

    autosize = Unicode(
        "pad",
        help="Sets how the visualization size should be determined")
