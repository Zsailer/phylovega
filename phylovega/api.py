from IPython.display import display

from . import chart
from . import marks
from . import transforms
from . import signals

class TreeChart(object):
    """Tree Chart in Vega.
    """
    def __init__(
        self,
        data=None,
        height_scale=100,
        length_scale=100,
        height_slider=None,
        length_slider=None,
        **kwargs):

        # Attributes to fix.
        if height_slider is None:
            self.height_scale = height_scale

        else:
            self.height_scale = "height_slider"

        # Attributes to fix.
        if length_slider is None:
            self.length_scale = length_scale

        else:
            self.length_scale = "length_slider"

        self.data = data
        self.attrs = kwargs

        self.node_attrs = dict(

        )
        self.slider_attrs = dict(
            height_slider=height_slider,
            length_slider=length_slider,
        )


    def get_specification(self):
        specification = {}
        specification.update(
            **chart.get_chart_specification(
                height=500,
                width=500
            ),
            **signals.get_signal_specification(
                **self.slider_attrs
            ),
            **marks.get_mark_specification(
                **self.attrs
            ),
            **transforms.get_data_specification(
                self.data,
                height_scale=self.height_scale,
                width_scale=self.length_scale
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
