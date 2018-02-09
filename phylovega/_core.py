import json
from vega3 import Vega
from . import _schema

class VegaTree(object):
    """Create an object that draws a Phylogenetic Tree using Vega.
    """
    def __init__(self, data=None):
        self.data = data
        self._schema = None
        self._set_to_default_spec()

    def _set_to_default_spec(self):
        schema = _schema.BASE_SPEC
        schema['data'] = []

        # Add data field
        tree_spec = _schema.TREE_TRANSFORM_SPEC
        tree_spec['values'] = self.data_spec

        # Edge_transform
        edge_spec = _schema.EDGE_TRANSFORM_SPEC
        node_spec = _schema.NODE_GROUPING_TRANSFORM_SPEC

        schema['data'] += [tree_spec, edge_spec] + node_spec
        self._schema = schema

    @property
    def data_spec(self):
        return self.data.to_dict(orient='records')

    @property
    def schema(self):
        return self._schema

    def display(self):
        """Display the object"""
        self.vega_object = Vega(self.schema)
        self.vega_object.display()

    def to_json(self, filename=None):
        """Write to JSON"""
        s = json.dumps(self.schema)

        if filename is None:
            return s
        else:
            with open(filename, 'w') as f:
                f.write(s)
