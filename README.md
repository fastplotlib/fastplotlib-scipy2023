# fastplotlib SciPy 2023

Materials for the `fastplotlib` talk at SciPy 2023. This repo includes installation instructions and the demo notebooks covered in our talk. 

The demos cover the following topics:
1. `Images` - plotting simple images, feature changes, image updates, `ImageWidget`
2. `Lines` - 2D line plots, fancy indexing of features, `LineCollection`, `LineStack`, `LinearSelector`, `LinearRegionSelector`, `Heatmap`
4. Interactivity - high-level interactivity system to link graphics and their features together, addding event handlers for further interaction
5. `GridPlots` - grid of `Subplots`
6. `Scatters` - 2D and 3D scatter plots

# Installation instructions

See the `fastplotlib` repo for [installation](https://github.com/kushalkolar/fastplotlib#:~:text=on%20gitter.-,Installation,-Install%20using%20pip). 

In order to run the notebooks you will also need to have `imageio` and `zarr` installed. These are not dependencies of `fastplotlib`, but are being used in these demos.

### Install using pip
```
pip install tiffile imageio zarr
```

# General `fastplotlib` API
## 1. Graphics - objects that are drawn
- `Image`, `Line`, `Scatter`, `Heatmap`
- Collections - `LineCollection`, `LineStack` (ex: neural timeseries data)
- Interactions
## 2. Layouts
- `Plot` - a single plot area
- `GridPlot` - a grid of `Subplots`
## 3. Widgets - high level widgets to make repetitive UIs easier
- `ImageWidget`- n-dimensional widget for Image data
- Sliders, support window functions, `GridPlot`, etc.

# Docs
For a more in-depth look at our API, please visit our [docs](https://fastplotlib.readthedocs.io/en/latest/?badge=latest).

# Contributions
`fastplotlib` is a relatively new software, and we are always looking for feedback or help! Please see the [contributing guide](https://github.com/kushalkolar/fastplotlib/blob/master/CONTRIBUTING.md). 

You can also look at our [Roadmap for 2023](https://github.com/kushalkolar/fastplotlib/issues/55) and [Issues](https://github.com/kushalkolar/fastplotlib/issues) for more ideas on how to contribute.
