from traitlets import Int, Unicode, List

from .base import Specification
from . import transforms


class DataSpec(Specification):
    """Vega Specification for a phylogenetic tree visualization.
    """
    def __init__(self, df):
        values = df.to_dict(orient='records')

    values = List(
        help="Data values.")

    transform = List(
        help="A list of transforms to perform on the input data.")

    name = Unicode(
        "tree",
        help="A unique name for the data set")
