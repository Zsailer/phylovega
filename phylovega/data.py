from traitlets.config import Configurable
from traitlets import (
    Integer, 
    Unicode,
    List,
    default
)
from phylovega.traitlets import VegaConfigurable


class TreeData(VegaConfigurable):
    """Object that constructs the Vega transformations
    needed to create a tree layout.
    """
    width_scale = Integer(100, help="Width scale.", config=True)

    @default('width_scale')
    def _default_width_scale(self):
        dist = [el['distance'] for el in self.data]
        dist = max(dist)
        return int(self.chart_width / dist)

    height_scale = Integer(100, help="Height scale", config=True)
    data = List(help="Data dictionary.", config=True)

    def __init__(self, data, chart_height, chart_width, config=None, **kwargs):
        super().__init__(config=config, **kwargs)
        self.data = data
        self.chart_height = chart_height
        self.chart_width = chart_width

    @property
    def edge_group_spec(self):
        """Edge groups specification as Python dictionary."""
        return {
            'name': 'leaves',
            'source': 'tree',
            'transform': [
                {
                    'type': 'filter',
                    'expr': 'datum.type == "leaf"'
                }
            ]
        }

    @property
    def node_group_spec(self):
        """Node groups specification as Python dictionary."""
        return {
            'name': 'nodes',
            'source': 'tree', 
            'transform': [
                {
                    'type': 'filter',
                    'expr': 'datum.type == "node"'
                }
            ]
        }

    @property
    def edge_transform_spec(self):
        """Edge transform specification as Python dictionary."""
        return {
            'name': 'links',
            'source': 'tree',
            'transform': [
                {
                    'type': 'treelinks',
                    'key': 'id'
                },
                {
                    'type': 'linkpath',
                    'orient': 'horizontal',
                    'shape': 'orthogonal'
                },
            ]
        }


    @property
    def data_transform_spec(self):
        """Layout specification as Python dictionary."""
        return {
            'name': 'tree',
            'values': self.data,
            'transform': [
                {
                    'type': 'stratify',
                    'parentKey': 'parent',
                    'key': 'id'
                },
                {
                    'type': 'tree',
                    'method': 'cluster',
                    'size': [self.chart_height, self.chart_width],
                    'as': ['y0', 'x0', 'depth0', 'children0']
                },
                {
                    'type': 'tree',
                    'method': 'cluster',
                    'size': [self.chart_height, self.chart_width],
                    'as': ['y', 'x', 'depth', 'children']
                },
                {
                    'type': 'formula',
                    'expr': '0.8 * datum.distance * {}'.format(self.width_scale),
                    'as': 'x'
                },
                # {
                #     'type': 'formula',
                #     'expr': 'datum.y0 * ({} / 100)'.format(self.width_scale),
                #     'as': 'y'
                # }
            ]
        }


    def get_spec(self):
        """Get specification as Python dictionary."""
        return {
            'data': [
                self.data_transform_spec,
                self.edge_transform_spec,
                self.node_group_spec,
                self.edge_group_spec
            ]
        }
