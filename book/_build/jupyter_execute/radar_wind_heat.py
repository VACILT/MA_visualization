#!/usr/bin/env python
# coding: utf-8

# # Zonal and meridional wind
# 
# Use the tools provided in the toolbar to drag, zoom or save the plot as pdf for further use.

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import param
import numpy as np
import pandas as pd


# In[2]:


root_path = '/project/MA_vis/MA_visualization/data/'
cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_wind = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_8'],group ='wind', combine = 'nested', engine='netcdf4')
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info',  engine='netcdf4')
ds_info2 = xr.open_dataset(cascade_infiles[-1], group = 'info',  engine='netcdf4')
ds_wind = ds_wind.rename({'phony_dim_8': 'time', 'phony_dim_9': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'
restr = lambda x: int(x[0])
year, month, day = map(restr, ds_info['date'].values)
year2, month2, day2 = map(restr, ds_info2['date'].values)
ds_wind['time']=pd.date_range(start=f'{year}-{month:02d}-{day:02d}', end=f'{year2}-{month2:02d}-{day2:02d}', periods = (len(cascade_infiles)-1)*24)


# In[3]:


graph_opts = dict(cmap = 'RdBu_r', symmetric=True, logy = False, colorbar = True)
graph_u=ds_wind['u'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='u').redim.range(u=(-100, 100))
graph_v=ds_wind['v'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='v').redim.range(v=(-100, 100))
heatmap=(graph_u + graph_v).cols(1)


# In[4]:


hvplot.save(heatmap, 'heatmap.html')


# In[5]:


from IPython.display import HTML
HTML(filename="heatmap.html")

