from traitlets import (
    HasTraits,
    Integer, 
    Unicode,
    List
)

class TreeData(HasTraits):
    """Object that constructs the Vega transformations
    needed to create a tree layout.
    """
    width_scale = Integer(100, help="Width scale.")
    height_scale = Integer(100, help="Height scale")
    data = List(help="Data dictionary.")

    def __init__(self, data):
        self.data = data

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
                # Step 2: statify
                {
                    'type': 'stratify',
                    'parentKey': 'parent',
                    'key': 'id'
                },
                {
                    'type': 'tree',
                    'method': 'cluster',
                    'size': [self.height_scale, self.width_scale],#{'signal': 'height'}, {'signal': 'width - 100'}],
                    'as': ['y0', 'x0', 'depth0', 'children0']
                },
                {
                    'type': 'tree',
                    'method': 'cluster',
                    # {'signal': 'height'}, {'signal': 'width - 100'}],
                    'size': [self.height_scale, self.width_scale],
                    'as': ['y', 'x', 'depth', 'children']
                },
                {
                    'type': 'formula',
                    'expr': 'datum.distance * {}'.format(self.width_scale),
                    'as': 'x'
                },
                {
                    'type': 'formula',
                    'expr': 'datum.y0 * ({} / 100)'.format(self.width_scale),
                    'as': 'y'
                }
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


# def get_data_specification(
#     data,
#     width_scale=100,
#     height_scale=100
#     ):
#     """
#     """

#     # Compute topology and node positions.
#     topology = get_topology_transform_specification(
#         data=data,
#         width_scale=width_scale,
#         height_scale=height_scale
#     )

#     # Compute positions of edges.
#     edges = get_edge_transform_specification(

#     )

#     # Group nodes for easy styling.
#     node_group = get_node_group_specification(

#     )

#     # Group edges for easy styling.
#     edge_group = get_edge_group_specification(

#     )

#     specification = dict(
#         data=[
#             topology,
#             edges,
#             node_group,
#             edge_group
#         ]
#     )
#     return specification



# def get_topology_transform_specification(
#     data=None,
#     width_scale=100,
#     height_scale=100
#     ):
#     """Construct the series of transforms to draw a tree in vega.

#     Steps:
#     1. Stratify
#     2. Cluster
#     """
#     # Stratify
#     step1 = dict(
#         type="stratify",
#         parentKey="parent",
#         key="id"
#     )

#     # Cluster
#     step2_ = dict(
#         type="tree",
#         method="cluster",
#         size=[{"signal": "height"}, {"signal": "width - 100"}]
#     )
#     step2_["as"] = ["y0", "x0", "depth0", "children0"]

#     # Cluster
#     step2 = dict(
#         type="tree",
#         method="cluster",
#         size=[{"signal": "height"}, {"signal": "width - 100"}]

#     )
#     step2["as"] = ["y", "x", "depth", "children"]

#     # Compute x positions
#     step3 = dict(
#         type="formula",
#         expr="datum.distance * {}".format(width_scale),
#     )
#     step3["as"] = "x"

#     # Compute y positions
#     step4 = dict(
#         type="formula",
#         expr="datum.y0 * ({} / 100)".format(height_scale),
#     )
#     step4["as"] = "y"

#     # Transform dataframe elements to vega data source format.
#     values = data.to_dict(orient='records')

#     specification = dict(
#         name="tree",
#         transform=[
#             step1,
#             step2_,
#             step2,
#             step3,
#             step4
#         ],
#         values=values
#     )
#     return specification


# def get_edge_transform_specification():
#     """Build edge transform grammar.
#     """
#     transform = []
#     step1 = dict(
#         type="treelinks",
#         key="id"
#     )

#     transform.append(step1)

#     step2 = dict(
#         type="linkpath",
#         orient="horizontal",
#         shape="orthogonal"
#     )

#     transform.append(step2)

#     # Define specification
#     specification = dict(
#         name="links",
#         source="tree",
#         transform=transform
#     )
#     return specification


# def get_node_group_specification():
#     """
#     """
#     specification = dict(
#         name="nodes",
#         source="tree",
#         transform=[dict(
#             type="filter",
#             expr="datum.type == 'node'"
#         )]
#     )
#     return specification


# def get_edge_group_specification():
#     """
#     """
#     specification = dict(
#         name="leaves",
#         source="tree",
#         transform=[dict(
#             type="filter",
#             expr="datum.type == 'leaf'"
#         )]
#     )
#     return specification
