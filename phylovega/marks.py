
def get_mark_specification(
    edge_color="#ccc",
    edge_width=3,
    node_size=70,
    node_color="#000",
    node_labels="id",
    leaf_labels="id",
    leaf_size=0,
    leaf_color="#000"
    ):
    """
    """
    marks = []

    edges = get_edge_specification(
        edge_color=edge_color,
        edge_width=edge_width,
    )

    nodes = get_node_specification(
        node_size=node_size,
        node_color=node_color
    )

    leafs = get_leaf_specification(
        leaf_size=leaf_size,
        leaf_color=leaf_color
    )

    leaf_labels = get_leaf_text_specification(
        leaf_labels=leaf_labels
    )

    node_labels = get_node_text_specification(
        node_labels=node_labels
    )

    specification = dict(
        marks=[
            edges,
            nodes,
            leafs,
            leaf_labels,
            node_labels,
        ]
    )
    return specification


def get_edge_specification(
    edge_color="#ccc",
    edge_width=3
    ):
    """
    """
    # Build styles for edges.
    style = dict(
        path=dict(field="path"),
        stroke=dict(
            value=edge_color
        ),
        strokeWidth=dict(
            value=edge_width
        )
    )

    # Encode edge style.
    encode = dict(update=style)

    # Construct full specification for edges.
    specification = dict(
        type="path",
        encode=encode,
    )
    specification["from"] = dict(data="links")
    return specification


def get_leaf_specification(
    leaf_size=70,
    leaf_color="#000",
    ):
    """
    """
    style = dict(
        enter=dict(
            size=dict(value=leaf_size),
            stroke=dict(value='#000')
        ),
        update=dict(
            x=dict(field="x"),
            y=dict(field="y"),
            fill=dict(value=leaf_color)
        )
    )

    specification = dict(
        type="symbol",
        encode=style
    )
    specification["from"]=dict(data="leaves")

    return specification


def get_node_specification(
    node_size=70,
    node_color="#000",
    ):
    """
    """
    style = dict(
        enter=dict(
            size=dict(value=node_size),
            stroke=dict(value='#000')
        ),
        update=dict(
            x=dict(field="x"),
            y=dict(field="y"),
            fill=dict(value=node_color)
        )
    )

    specification = dict(
        type="symbol",
        encode=style
    )
    specification["from"]=dict(data="nodes")

    return specification


def get_leaf_text_specification(
    leaf_labels="id",
    leaf_label_color="#000",
    x_offset=2,
    y_offset=3
    ):
    """
    """
    encode = dict(
        enter=dict(
            fill=dict(value=leaf_label_color),
            text=dict(field=leaf_labels)
        ),
        update=dict(
            x=dict(field="x"),
            y=dict(field="y"),
            dx=dict(value=x_offset),
            dy=dict(value=y_offset)
        )
    )

    specification = dict(
        type="text",
        encode=encode
    )
    specification["from"] = dict(data="leaves")
    return specification


def get_node_text_specification(
    node_labels="id",
    node_label_color="#000",
    x_offset=-3,
    y_offset=4
    ):
    """
    """
    encode = dict(
        enter=dict(
            fill=dict(value=node_label_color),
            text=dict(field=node_labels)
        ),
        update=dict(
            x=dict(field="x"),
            y=dict(field="y"),
            dx=dict(value=x_offset),
            dy=dict(value=y_offset)
        )
    )

    specification = dict(
        type="text",
        encode=encode
    )
    specification["from"] = dict(data="nodes")
    return specification
