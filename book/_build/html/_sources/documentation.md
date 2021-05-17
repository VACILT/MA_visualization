# Documentation

In this chapter, we want to show what you need to build plots like this. 

## Data reading

Big meteorological data is often given as NET-CDF or .h5-file. [x-array is](http://xarray.pydata.org/en/stable/) the perfect python-package to deal with such multi dimensional data.

## Plotting

## from notebook to book

Jupyter notebooks provides a good mix of code interpreter and narrativ markdown cells. Sadly, it only runs in the local repository or online using binder.
Preprozessing the dynamic notebook to a static books, gives accessibility to any visitor of this webside.

Setup content as notebook-file (.ipynb) or markdown (.md). Provide some metadata to the _config.yml and create the table of contends (_toc.yml). Then the .html is created by jupyter-book:

```
jupyter-book build ./book
```