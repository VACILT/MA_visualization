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
import pandas as pd

# + tags=["hide-cell"]
root_path = '/project/MA_vis/MA_visualization/data/'
cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_info = xr.open_dataset(cascade_infiles[0],group ='info')
ds_info['date']
ds_tides = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_6'],group ='tides', combine = 'nested')
ds_tides = ds_tides.rename({'phony_dim_5': 'alt','phony_dim_6': 'time'})
ds_tides['alt'] = ds_info['alt'].squeeze().values
ds_tides['alt'].attrs['units'] = 'km'
restr = lambda x: int(x[0])
year, month, day = map(restr, ds_info['date'].values)
ds_tides['time']=pd.date_range(f'{year}-{month:02d}-{day:02d}', periods = len(cascade_infiles)-1)
ds_tides['A12u']

# + tags=["hide-input"]
levels=10

graph_opts = dict(cmap = 'viridis', logy = False, colorbar = True)
graph_top=ds_tides['A12v'].hvplot.contourf(by = 'time.hour',levels=10).opts(**graph_opts, title='u')
graph_bottom=ds_tides['A12v'].hvplot.contourf(y = 'alt', by = 'time.day',levels=10 ).opts(**graph_opts, title='v')
hv_panel_top = pn.panel(graph_top)
hv_panel_bottom = pn.panel(graph_bottom)
gspec = pn.GridSpec(width=800, height=600, margin=5)
gspec[0:1, 0] = hv_panel_top
gspec[1:2, 0] = hv_panel_bottom
#hv_panel_bottom.pprint()
gspec
# -

hvplot.help('contourf')

from bokeh.models.formatters import DatetimeTickFormatter
formatter = DatetimeTickFormatter(months='%b %Y')
sst.hvplot(xformatter=formatter)


