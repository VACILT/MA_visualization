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


# In[2]:


root_path = '/project/MA_vis/MA_visualization/data/'
cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_wind = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_8'],group ='wind', combine = 'nested', engine='netcdf4')
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info',  engine='netcdf4')
dates=[]
for i in cascade_infiles:
    dates.append(i[-13:-3])
    ds_wind['date'] = dates[0:11]


# In[3]:


ds_wind = ds_wind.rename({'phony_dim_8': 'time', 'phony_dim_9': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'
ds_wind['time']=np.arange(0,11,1/24)
ds_wind['time'].attrs['units'] = f'days after {dates[0]}'
ds_wind['dates']=np.arange(0,11,1)


# In[4]:


graph_opts = dict(cmap = 'RdBu_r', symmetric=True, logy = False, colorbar = True)
graph_top=ds_wind['u'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='u').redim.range(u=(-100, 100))
graph_bottom=ds_wind['v'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='v').redim.range(v=(-100, 100))
hv_panel_top = pn.panel(graph_top)
hv_panel_bottom = pn.panel(graph_bottom)
gspec = pn.GridSpec(width=800, height=600, margin=5)
gspec[0:1, 0] = hv_panel_top
gspec[1:2, 0] = hv_panel_bottom
#hv_panel_bottom.pprint()
gspec


# In[ ]:




