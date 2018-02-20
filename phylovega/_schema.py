BASE_SPEC = {
    "$schema": "https://vega.github.io/schema/vega/v3.json",
    "width": 1000,
    "height": 700,
    "padding": 5,

    # -------------- SCALES -------------

    "signals": [
        {
            "name": "branchScale",
            "value": 200,
            "bind": {
                "input": "range",
                "min": 0,
                "max": 500,
                "step": 50
            }
        },
        {
            "name": "heightScale",
            "value": 100,
            "bind": {
                "input": "range",
                "min": 0,
                "max": 100,
                "step": 5
            }
        },
        {
            "name": "cladify",
            "value": "datum",
            "on": [
                {"events": "@ancestor:mousedown, @ancestor:touchstart", "update": "datum"},
            ]
        },
    ],

    "scales": [
        {
        "name": "color",
        "type": "sequential",
        "range": {"scheme": "magma"},
        "domain": {"data": "tree", "field": "depth"},
        "zero": True
        }
    ],

    "marks": [
        {
            "type": "path",
            "from": {"data": "links"},
            "encode": {
                "update":{
                    "path": {"field": "path"},
                    "stroke": {"value": "#ccc"},
                    "strokeWidth": {"value": 3},
                },
            },
        },
        {
            "name": "ancestor",
            "type": "symbol",
            "from": {"data": "nodes"},
            "encode": {
                "enter": {
                    "size": {"value": 70},
                    "stroke": {"value": "#000"},
                },
                "update": {
                    "x": {"field": "x"},
                    "y": {"field": "y"},
                    "fill": {"value": "#000"},
                }
            }
        },
        {
            "type": "text",
            "from": {"data": "leaves"},
            "encode": {
                "enter": {
                    "fill": {"value": "#000"},
                    "text": {"field": "label"},
                },
                "update": {
                    "x": {"field": "x"},
                    "y": {"field": "y"},
                    "dx": {"value": 2},
                    "dy": {"value": 3},
                }
            }
        },
    ]
}

# -------------------- DATA TRANSFORM SPECS ---------------------

TREE_TRANSFORM_SPEC = {
    "name": "tree",
    "transform": [
        {
            "type": "stratify",
            "key": "id",
            "parentKey": "parent"
        },
        {
            "type": "tree",
            "method": "cluster",
            "size": [{"signal": "height"}, {"signal": "width - 100"}],
            "as": ["y0", "x0", "depth0", "children0"]
        },
        {
            "type": "tree",
            "method": "cluster",
            "size": [{"signal": "height"}, {"signal": "width - 100"}],
            "as": ["y", "x", "depth", "children"]
        },
        {
            "type": "formula",
            "expr": "datum.distance * branchScale",
            "as": "x"
        },
        {
            "type": "formula",
            "expr": "datum.y0 * (heightScale / 100)",
            "as": "y"
        },
    ],
}

TREE0_TRANSFORM_SPEC = {
    "name": "tree0",
    "transform": [
        {
            "type": "stratify",
            "key": "id",
            "parentKey": "parent"
        },
        {
            "type": "tree",
            "method": "cluster",
            "size": [{"signal": "height"}, {"signal": "width - 100"}],
            "as": ["y0", "x0", "depth0", "children0"]
        },
        {
            "type": "tree",
            "method": "cluster",
            "size": [{"signal": "height"}, {"signal": "width - 100"}],
            "as": ["y", "x", "depth", "children"]
        },
        {
            "type": "formula",
            "expr": "datum.distance * branchScale",
            "as": "x"
        },
        {
            "type": "formula",
            "expr": "datum.y0 * (heightScale / 100)",
            "as": "y"
        }
    ]
}


EDGE_TRANSFORM_SPEC = {
    "name": "links",
    "source": "tree",
    "transform": [
        {
            "type": "treelinks",
            "key": "id"
        },
        {
            "type": "linkpath",
            "orient": "horizontal",
            "shape": "orthogonal"
        }
    ]
}

NODE_GROUPING_TRANSFORM_SPEC = [
    {
        "name": "nodes",
        "source": "tree",
        "transform": [{ "type": "filter", "expr": "datum.type == 'node'" }]
    },
    {
        "name": "leaves",
        "source": "tree",
        "transform": [{ "type": "filter", "expr": "datum.type == 'leaf'" }]
    }
]
