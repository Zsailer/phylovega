from traitlets import (
    Unicode,
    Int,
    Float,
    default
)
from phylovega.traitlets import (
    VegaConfigurable,
    VegaColorOption,
    VegaMenuOption,
    VegaRangeOption
)


class TreeMarkOptions(VegaConfigurable):
    # --------------------------------------------------------
    # branch traits.
    # --------------------------------------------------------

    branch_color = VegaColorOption(
        '#ccc', help='Color of tree edges.', config=True)

    branch_width = VegaRangeOption(2, help='Width of the edges.', config=True)

    # --------------------------------------------------------
    # Node traits.
    # --------------------------------------------------------

    node_size = VegaRangeOption(50, help='Size of the nodes.').tag(config=True)

    node_edge_width = VegaRangeOption(
        1,
        help='Node edge width',
        config=True
    )

    node_edge_color = VegaColorOption(
        '#000',
        help="Color of node edge",
        config=True
    )

    node_color = VegaColorOption(
        '#000', help='Color of the nodes.', config=True)

    node_labels = VegaMenuOption(
        'id', help='Column to use for node labels.', config=True)

    node_text_size = VegaRangeOption(
        10, help="Node text size", config=True)

    node_text_column = VegaMenuOption(
        'id', help='Column to label the nodes.', config=True)

    node_text_xoffset = VegaRangeOption(
        4,
        help="Node text X offset.",
        config=True
    )

    node_text_yoffset = VegaRangeOption(
        3,
        help="Node text Y offset.",
        config=True
    )

    node_text_color = VegaColorOption(
        '#000', help='Hex string for text color.', config=True)

    # --------------------------------------------------------
    # Leaf traits
    # --------------------------------------------------------

    leaf_size = VegaRangeOption(
        50, help='Size of the leaves.').tag(config=True)

    leaf_edge_width = VegaRangeOption(
        1,
        help='leaf edge width',
        config=True
    )

    leaf_edge_color = VegaColorOption(
        '#000',
        help="Color of leaf edge",
        config=True
    )

    leaf_color = VegaColorOption(
        '#000', help='Color of the leaves.', config=True)

    leaf_labels = VegaMenuOption(
        'id', help='Column to use for leaf labels.', config=True)

    leaf_text_size = VegaRangeOption(
        10, help="Leaf text size", config=True)

    leaf_text_color = VegaColorOption(
        '#000', help='Hex string for text color.', config=True)

    leaf_text_column = VegaMenuOption(
        'id', help='Column to label the leafs.', config=True)

    leaf_text_xoffset = VegaRangeOption(
        4,
        help="Leaf text X offset.",
        config=True
    )

    leaf_text_yoffset = VegaRangeOption(
        3,
        help="Leaf text Y offset.",
        config=True
    )

    leaf_size = VegaRangeOption(0, help='Size of leaf node.', config=True)


class TreeMarks(TreeMarkOptions):
    """Style the marks in the tree visualization."""

    def vega_mark(self, name, value):
        _, key = self.vega_input(name, value)
        if key in ['value', 'field']:
            return {key: value}
        elif key in ['signal']:
            return {key: name}

    @property
    def branch_spec(self):
        """Branch specification represented by Python dictionary."""
        return {
            'type': 'path',
            'from': {'data': 'links'},
            'encode': {
                'update': {
                    'path': {'field': 'path'},
                    'stroke': self.vega_mark('branch_color', self.branch_color),
                    'strokeWidth': self.vega_mark('branch_width', self.branch_width),
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
                    'fill': self.vega_mark('leaf_color', self.leaf_color),
                    'stroke': self.vega_mark('leaf_edge_color', self.leaf_edge_color)
                },
                'update': {
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'size': self.vega_mark('leaf_size', self.leaf_size),
                    'strokeWidth': self.vega_mark('leaf_edge_width', self.leaf_edge_width)
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
                    'stroke': self.vega_mark('node_edge_color', self.node_edge_color),
                },
                'update': {
                    'fill': self.vega_mark('node_color', self.node_color),
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'size': self.vega_mark('node_size', self.node_size),
                    'strokeWidth': self.vega_mark('node_edge_width', self.node_edge_width)
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
                    'fill': self.vega_mark('leaf_text_color', self.leaf_text_color),
                    'text': self.vega_mark('leaf_text_column', self.leaf_text_column)
                },
                'update': {
                    'fontSize': self.vega_mark('leaf_text_size', self.leaf_text_size),
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'dx': self.vega_mark('leaf_text_xoffset', self.leaf_text_xoffset),
                    'dy': self.vega_mark('leaf_text_yoffset', self.leaf_text_yoffset)
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
                    'fill': self.vega_mark('node_text_color', self.node_text_color),
                    'text': self.vega_mark('node_text_column', self.node_text_column)
                },
                'update': {
                    'fontSize': self.vega_mark('node_text_size', self.node_text_size),
                    'x': {'field': 'x'},
                    'y': {'field': 'y'},
                    'dx': self.vega_mark('node_text_xoffset', self.node_text_xoffset),
                    'dy': self.vega_mark('node_text_yoffset', self.node_text_yoffset)
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
