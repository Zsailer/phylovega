from IPython.display import display
from traitlets.config import Application, Config
from traitlets import (
    Unicode,
    Int,
    Dict,
    List
)
from .chart import BaseTreeChart
from .data import TreeData
from .marks import TreeMarkOptions, TreeMarks
from .signals import TreeSignals

VEGA_VERSION = 4

classes = [
    BaseTreeChart,
    TreeData,
    TreeMarkOptions,
    TreeMarks,
    TreeSignals
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


docstring = """Visualize Tree in Vega.

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

    def __init__(self, data=[], config=None, **kwargs):
        """"""
        config = Config()#config=config)
        config.update(**kwargs)
        super(TreeChart, self).__init__(config=config, **kwargs)

        self.data = data
        self.init_classes()

    @classmethod
    def from_dendropy(cls, tree, config={}, **kwargs):
        """Read from DendroPy Tree."""
        try:
            import phylopandas as pd
            df = pd.read_dendropy(tree)
            data = df.to_dict(orient='records')
            return cls(data=data, config={}, **kwargs)
        except ImportError:
            Exception("DendroPy and Phylopandas must be installed.")

    @classmethod
    def from_phylopandas(cls, df, config={}, **kwargs):
        """Read from phylopandas DataFrame"""
        try:
            data = df.to_dict(orient='records')
            return cls(data=data, config=config, **kwargs)
        except ImportError:
            Exception("DendroPy and Phylopandas must be installed.")

    @classmethod
    def from_newick(cls, newick_file, config={}, **kwargs):
        """Read tree from newick file."""
        try:
            import phylopandas as pd
            df = pd.read_newick(newick_file)
            data = df.to_dict(orient='records')
            return cls(data=data, config={}, **kwargs)
        except ImportError:
            Exception("DendroPy and Phylopandas must be installed.")

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
        self.base_chart = BaseTreeChart(data=self.data, config=self.config)
        self.tree_data = TreeData(
            data=self.data, 
            chart_height=self.base_chart.height,
            chart_width=self.base_chart.width,
            config=self.config,
        )
        self.tree_marks = TreeMarks(config=self.config)
        self.tree_signals = TreeSignals(config=self.config)

    def initialize(self, argv=None):
        """"""
        self.parse_command_line(argv=argv)
        self.init_classes()

    def get_spec(self):
        """Get specification as Python dictionary."""
        spec = {}
        spec.update(**self.base_chart.get_spec())
        spec.update(**self.tree_data.get_spec())
        spec.update(**self.tree_marks.get_spec())
        spec.update(**self.tree_signals.get_spec())
        return spec

    def show(self):
        """Show the graph."""
        bundle = self._repr_mimebundle_()
        display(bundle, raw=True)


main = TreeChart._launch_app

if __name__ == "__main__":
    main()
