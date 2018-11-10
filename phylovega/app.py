from IPython.display import display
from traitlets.config import Application, Config
from traitlets import (
    Unicode,
    Int,
    Dict,
    List
)
from phylovega.traitlets import HexColorString
from .chart import BaseTreeChart
from .data import TreeData
from .marks import TreeMarks

VEGA_VERSION = 4

classes = [
    BaseTreeChart,
    TreeData,
    TreeMarks
]

traits = {}
for c in classes:
    for name, trait in c.class_own_traits().items():
        traits[name] = trait

aliases = {name: "{}.{}" for name in traits}

trait_docs = []
for trait in traits.values():
    name = trait.name
    doc = trait.help
    klass = trait.__class__.__name__
    trait_docs.append('{} : {}\n    {}\n'.format(name, klass, doc))


docstring = """Tree Chart

Parameters
----------
data : 
    Tree data.

{}
""".format('\n'.join(trait_docs))

class TreeChart(Application):
    __doc__ = docstring

    name = Unicode("TreeChart")
    description = Unicode("Create Tree visualizations in Vega.")

    # Attirubte
    data = List(help="Tree data as Python dictionary.", config=True)

    classes = List(classes, help="List of classes to expose to config.")
    aliases = Dict(aliases, help="Dictionary of aliases.")

    def __init__(self, data=data, config={}, **kwargs):
        config = Config(config)
        config.update(**kwargs)
        super(TreeChart, self).__init__(config=config, **kwargs)

        self.data = data
        self.init_classes()

    def _repr_mimebundle_(self, include=None, exclude=None):
        mimetype = 'application/vnd.vega.v{}+json'.format(VEGA_VERSION)
        spec = self.get_spec()
        return {mimetype: spec}

    @classmethod
    def _launch_app(cls, *args, **kwargs):
        self = cls(*args, **kwargs)
        self.initialize()
        self.start()

    def init_classes(self):
        self.base_chart = BaseTreeChart(config=self.config)
        self.tree_data = TreeData(data=self.data, config=self.config)
        self.tree_marks = TreeMarks(config=self.config)

    def initialize(self, argv=None):
        """"""
        self.parse_command_line(argv=argv)
        self.init_classes()

    def start(self):
        """"""
        pass

    def get_spec(self):
        """Get specification as Python dictionary."""
        spec = {}
        spec.update(**self.base_chart.get_spec())
        spec.update(**self.tree_data.get_spec())
        spec.update(**self.tree_marks.get_spec())
        return spec

    def show(self):
        """Show the graph."""
        bundle = self._repr_mimebundle_()
        display(bundle, raw=True)


main = TreeChart._launch_app

if __name__ == "__main__":
    main()



# from . import chart
# from . import marks
# from . import transforms
# from . import signals

# class TreeChart(object):
#     """Tree Chart in Vega.
#     """


#     def __init__(
#         self,
#         data=None,
#         height_scale=100,
#         length_scale=100,
#         height_slider=None,
#         length_slider=None,
#         **kwargs):

#         # Attributes to fix.
#         if height_slider is None:
#             self.height_scale = height_scale

#         else:
#             self.height_scale = "height_slider"

#         # Attributes to fix.
#         if length_slider is None:
#             self.length_scale = length_scale

#         else:
#             self.length_scale = "length_slider"

#         self.data = data
#         self.attrs = kwargs

#         self.node_attrs = dict(

#         )
#         self.slider_attrs = dict(
#             height_slider=height_slider,
#             length_slider=length_slider,
#         )


#     def get_specification(self):
#         specification = {}
#         specification.update(
#             **chart.get_chart_specification(
#                 height=500,
#                 width=500
#             ),
#             **signals.get_signal_specification(
#                 **self.slider_attrs
#             ),
#             **marks.get_mark_specification(
#                 **self.attrs
#             ),
#             **transforms.get_data_specification(
#                 self.data,
#                 height_scale=self.height_scale,
#                 width_scale=self.length_scale
#             )
#         )
#         return specification


#     def encode_nodes(
#             self,
#             color="",

#             labels="id",
#             label_size=12,
#         ):
#         """
#         """
#         self.node_attrs.update(

#         )
#         return self

#     def encode_leafs():
#         """
#         """

#     def encode_edges():
#         """
#         """

#     def display(self):
#         """Fast tree drawing using Vega.
#         """
#         display({"application/vnd.vega.v3+json": self.get_specification()}, raw=True)
