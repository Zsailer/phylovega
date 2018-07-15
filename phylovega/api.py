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
        height=None,
        width=None,
        **kwargs):

        # Attributes to fix.
        self.width_scale=100
        self.height_scale=100
        self.height = height
        self.width = width
        self.data = data
        self.attrs = kwargs


    def get_specification(self):
        specification = {}
        specification.update(
            **chart.get_chart_specification(
                height=self.height,
                width=self.width
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

    def display(self):
        """Fast tree drawing using Vega.
        """
        display({"application/vnd.vega.v3+json": x.get_specification()}, raw=True)
