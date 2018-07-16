from IPython.display import display

from . import chart
from . import marks
from . import transforms


class TreeChart(object):
    """Tree Chart in Vega.
    """
    def __init__(
        self,
        data=None,
        height_scale=100,
        width_scale=100,
        **kwargs):

        # Attributes to fix.
        self.width_scale=width_scale
        self.height_scale=height_scale
        self.data = data
        self.attrs = kwargs

        self.node_attrs = dict(

        )


    def get_specification(self):
        specification = {}
        specification.update(
            **chart.get_chart_specification(

            ),
            **marks.get_mark_specification(
                **self.attrs
            ),
            **transforms.get_data_specification(
                self.data,
                height_scale=self.height_scale,
                width_scale=self.width_scale
            )
        )
        return specification


    def encode_nodes(
            self,
            color="",

            labels="id",
            label_size=12,
        ):
        """
        """
        self.node_attrs.update(

        )
        return self

    def encode_leafs():
        """
        """

    def encode_edges():
        """
        """

    def display(self):
        """Fast tree drawing using Vega.
        """
        display({"application/vnd.vega.v3+json": self.get_specification()}, raw=True)
