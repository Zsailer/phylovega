# PhyloVega

**Visualize phylogenetic trees in Vega from Python.**

![](docs/phylovega-example.gif)

## How does it work?

PhyloVega defines a strict Vega specification that works best for phylogenetic trees. It accepts a PhyloPandas DataFrame as input and
translates it to a Vega `data` field. It then creates a series of Vega
`transform`s to construct a hierarchical tree visualization.

## In the works

Here is a list of features that will eventually make it into PhyloVega.

* Interactive!
* Circular trees
* ... (feel free to add to this list).

## Install

Get the latest release with `pip`:

```
pip install phylovega
```

Install the development version by cloning this repo and calling:
```
pip install -e .
```

## Dependencies

PhyloVega uses the Vega3 specification. To use in the jupyter notebook, you must install the following Python dependencies.

* [PhyloPandas](https://github.com/Zsailer/phylopandass): Pandas DataFrame for Phylogenetics
* [ipyvega](https://github.com/vega/ipyvega): IPython/Jupyter notebook module for Vega and Vega-Lite (a visualization grammar).
