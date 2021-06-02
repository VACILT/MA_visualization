#!/usr/bin/env python
# coding: utf-8

# # Tides
# 
# Use the tools provided in the toolbar to drag, zoom or save the plot as pdf for further use.

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import numpy as np
import pandas as pd


# In[2]:


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
ds_tides['time']=pd.date_range(f'{year}-{month:02d}-{day:02d}', periods = ds_tides.time.shape[0], freq = 'D')


#restr = lambda x: int(x[0])
#year, month, day = map(restr, ds_info['date'].values)
#pd.date_range(f'{year}-{month:02d}-{day:02d}', periods = ds_tides.time.shape[0], freq = 'D')


# In[3]:


graph_opts = dict(cmap = 'viridis', symmetric=True, logy = False, colorbar = True)
graph_top=ds_tides['A12u'].hvplot.contourf(x = 'time', y = 'alt' ).opts(**graph_opts, title='u')
graph_bottom=ds_tides['A12v'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='v')#.redim.range(v=(-100, 100))
hv_panel_top = pn.panel(graph_top)
hv_panel_bottom = pn.panel(graph_bottom)
gspec = pn.GridSpec(width=800, height=600, margin=5)
gspec[0:1, 0] = hv_panel_top
gspec[1:2, 0] = hv_panel_bottom
#hv_panel_bottom.pprint()
gspec


# In[4]:


gspec = pn.GridSpec(width=800, height=800, margin=5)
gspec[0:1, 0] = bars('A24v', 'p24v')
gspec[1:2, 0] = bars('A12v', 'p12v')
gspec[2:3, 0] = bars('A8v', 'p8v')
gspec

