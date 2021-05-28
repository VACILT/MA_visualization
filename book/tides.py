# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Tides
#
# Use the tools provided in the toolbar to drag, zoom or save the plot as pdf for further use.

# + tags=["hide-cell"]
import xarray as xr
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import numpy as np

# + tags=["hide-cell"]
root_path = '/project/MA_vis/MA_visualization/data/'
cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_tides = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_5'],group ='tides', combine = 'nested')
ds_tides = ds_tides.rename({'phony_dim_5': 'time'})
ds_tides['time'].attrs['units'] = 'h'


# + tags=["hide-cell"]
def bars(var, err):
    bars = ds_tides.hvplot.scatter(y=[var]) \
    *ds_tides.hvplot.errorbars(y=var, yerr1=err).opts(title=f'{var}')
    return (bars)


# + tags=["hide-input"]
gspec = pn.GridSpec(width=800, height=800, margin=5)
gspec[0:1, 0] = bars('A12u', 'p12u')
gspec[1:2, 0] = bars('A24u', 'p24u')
gspec[2:3, 0] = bars('A8u', 'p8u')
gspec

# + tags=["hide-input"]
gspec = pn.GridSpec(width=800, height=800, margin=5)
gspec[0:1, 0] = bars('A24v', 'p24v')
gspec[1:2, 0] = bars('A12v', 'p12v')
gspec[2:3, 0] = bars('A8v', 'p8v')
gspec
