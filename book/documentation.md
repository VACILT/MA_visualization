# Documentation

In this chapter, we want to show what you need to build plots like this. Note that it's nessesary to use the correct version and all requirements of the library itself. 

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
We used the PyData data containers in the first step, so it's just locical to keep on this track. [hvPlot](https://hvplot.holoviz.org/user_guide/Introduction.html) is the best way to use this connected libraries.

```
hvplot                    0.7.2
```
## using jupyter notebook
```
notebook                  6.4.0
```

## from notebook to book

Jupyter notebook provides a good mix of code interpreter and narrativ markdown cells. Sadly, it only runs in the local repository or online using binder.
Preprozessing the dynamic notebook to a static books, gives accessibility to any visitor of this webside.

Setup content as notebook-file (.ipynb) or markdown (.md). Provide some metadata to the _config.yml and create the table of contends (_toc.yml). Then the .html is created by jupyter-book:

```
jupyter-book              0.11.1

```

```
jupyter-book build ./book
```
