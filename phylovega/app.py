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
        self.tree_data = TreeData(
            data=self.data, 
            chart_height=self.base_chart.height,
            chart_width=self.base_chart.width,
            config=self.config,
            
        )
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
