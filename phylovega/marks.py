from traitlets.config import Configurable
from traitlets import (
    Unicode,
    Int,
    Float,
    default
)
from phylovega.traitlets import HexColorString, VegaConfigurable


class TreeMarks(VegaConfigurable):
    """Style the marks in the tree visualization."""

    # --------------------------------------------------------
    # Node traits.
    # --------------------------------------------------------

    branch_color = HexColorString(
        '#ccc', help='Color of tree edges.', config=True)

    branch_width = Int(5, help='Width of the edges.', config=True)

    # --------------------------------------------------------
    # Node traits.
    # --------------------------------------------------------

    node_size = Int(70, help='Size of the nodes.').tag(config=True)

    node_edge_width = Int(
        1,
        help='Node edge width',
        config=True
    )

    node_edge_color = HexColorString(
        '#000',
        help="Color of node edge",
        config=True
    )

    node_color = HexColorString(
        '#000', help='Color of the nodes.', config=True)

    node_labels = Unicode(
        'id', help='Column to use for node labels.', config=True)

    node_text_size = Int(
        10, help="Node text size", config=True)

    node_text_column = Unicode(
        'id', help='Column to label the nodes.', config=True)

    node_text_xoffset = Float(
        0, 
        help="Node text X offset.", 
        config=True
    )

    node_text_yoffset = Float(
        help="Node text Y offset.", 
        config=True
    )

    @default('node_text_yoffset')
    def _default_node_text_yoffset(self):
        return -(self.node_text_size/3)

    node_text_color = HexColorString(
        '#000', help='Hex string for text color.', config=True)

    # --------------------------------------------------------
    # Leaf traits
    # --------------------------------------------------------

    leaf_size = Int(70, help='Size of the leaves.').tag(config=True)

    leaf_edge_width = Int(
        1,
        help='leaf edge width',
        config=True
    )

    leaf_edge_color = HexColorString(
        '#000',
        help="Color of leaf edge",
        config=True
    )

    leaf_color = HexColorString(
        '#000', help='Color of the leaves.', config=True)

    leaf_labels = Unicode(
        'id', help='Column to use for leaf labels.', config=True)

    leaf_text_size = Int(
        100, help="Leaf text size", config=True)

    leaf_text_color = HexColorString(
        '#000', help='Hex string for text color.', config=True)

    leaf_text_column = Unicode(
        'id', help='Column to label the leafs.', config=True)

    leaf_text_xoffset = Float(
        0,
        help="Leaf text X offset.", 
        config=True
    )

    leaf_text_yoffset = Float(
        help="Leaf text Y offset.",
        config=True
    )

    @default('leaf_text_yoffset')
    def _default_leaf_text_yoffset(self):
        return -(self.leaf_text_size/3)

    leaf_size = Int(0, help='Size of leaf node.', config=True)

    @property
    def branch_spec(self):
        """Branch specification represented by Python dictionary."""
        return {
            'type': 'path',
            'from': {'data': 'links'},
            'encode': {
                'update': {
                    'path': {'field': 'path'},
                    'stroke': {'value': self.branch_color},
                    'strokeWidth': {'value': self.branch_width}
                }
            }
        }

    @property
    def leaf_spec(self):
        """Leaf specification represented by Python dictionary."""
        return {
            'type': 'symbol',
            'from': {'data': 'leaves'},
            'encode':{
                'enter': {
                    'fill': {'value': self.leaf_color},
                    'stroke': {'value': self.leaf_edge_color}
                },
                'update': {
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'size': {'value': self.leaf_size},
                    'strokeWidth': {'value': self.leaf_edge_width}
                }
            }
        }

    @property
    def node_spec(self):
        """Node specification represented by Python dictionary."""
        return {
            'type': 'symbol',
            'from': {'data': 'nodes'},
            'encode': {
                'enter': {
                    'fill': {'value': self.node_color},
                    'stroke': {'value': self.node_edge_color},
                },
                'update': {
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'size': {'value': self.node_size},
                    'strokeWidth': {'value': self.node_edge_width}
                }
            }
        }

    @property
    def leaf_text_spec(self):
        """Leaf text specification represented by Python dictionary."""
        return {
            'type': 'text',
            'from': {'data': 'leaves'},
            'encode': {
                'enter': {
                    'fill': {'value': self.leaf_text_color},
                    'text': {'field': self.leaf_text_column}
                },
                'update': {
                    'fontSize': {'value': self.leaf_text_size},
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'dx': {'value': self.leaf_text_xoffset},
                    # Flip the sign--vega defines positive as down
                    'dy': {'value': -self.leaf_text_yoffset} 
                }
            }
        }

    @property
    def node_text_spec(self):
        """Node text specification represented by Python dictionary."""
        return {
            'type': 'text',
            'from': {'data': 'nodes'},
            'encode': {
                'enter': {
                    'fill': {'value': self.node_text_color},
                    'text': {'field': self.node_text_column}
                },
                'update': {
                    'fontSize': {'value': self.node_text_size},
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'dx': {'value': self.node_text_xoffset},
                    # Flip the sign--vega defines positive as down
                    'dy': {'value': -self.node_text_yoffset}
                }
            }
        }


    def get_spec(self):
        """Return spec."""
        return {
            'marks':[
                self.branch_spec,
                self.leaf_spec,
                self.node_spec,
                self.leaf_text_spec,
                self.node_text_spec,
            ]
        }
