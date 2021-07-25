# Documentation

In this chapter, we want to show what you need to build plots like this. Note that it's necessary to use the correct version and all requirements of the library itself. 

## Data reading

Big meteorological data is often given as NET-CDF or .h5-file. [x-array](http://xarray.pydata.org/en/stable/) is the perfect python-package to deal with such multi dimensional data. When the data is smaller and in a tabular like shape, [pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started) is the way to go. [Geopandas](https://geopandas.org/getting_started.html) helps matching geographic coordinates to basemaps and provides simple plotting. [numpy](https://numpy.org/) is pretty much required for all the used libraries.

We used:

```
xarray                    0.18.2
geopandas                 0.9.0       
pandas                    1.2.4
numpy                     1.20.3
```
## Plotting
We used the PyData data containers in the first step, so it's just logical to keep on this track. [hvPlot](https://hvplot.holoviz.org/user_guide/Introduction.html) is the best way to use this connected libraries.

```
hvplot                    0.7.2
```
## Using jupyter notebook
An [jupyter notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) contains the code and documentation of our project. This browser-based application runs  code, shows in- and output and supports documentation cells based on markdown. Everything is stored in one single file (.ipynb), which provides superior clarity.

```
notebook                  6.4.0
```

## From notebook to book

An Jupyter notebook consists of a code interpreter and narrative markdown cells. Sadly, the code interpreter only runs in the local repository or online using binder.
Pre-processing the dynamic notebook to a static book ([jupyter book](https://jupyterbook.org/intro.html)), gives accessibility to any visitor of this website.

 1.  Create a Folder (our: [/book](https://github.com/VACILT/MA_visualization/tree/main/book)).
 2.  Setup content as notebook-file (.ipynb) or markdown (.md).
 3.  Provide some metadata to the [_config.yml](https://github.com/VACILT/MA_visualization/blob/main/book/_config.yml).
 4.  create the table of content ([_toc.yml](https://github.com/VACILT/MA_visualization/blob/main/book/_toc.yml)).
 5.  go to the parent directory and run:
```
jupyter-book build ./book
```
6. The book will be created as html ([see here](https://github.com/VACILT/MA_visualization/tree/main/book/_build/html))
```
jupyter-book              0.11.1

```


