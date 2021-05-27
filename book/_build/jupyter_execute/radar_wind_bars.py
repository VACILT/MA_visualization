#!/usr/bin/env python
# coding: utf-8

# # Zonal and meridional wind by altidude
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


# In[3]:


root_path = '/project/MA_vis/MA_visualization/data/'
cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_wind = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_7'],group ='wind', combine = 'nested')
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info')
dates=[]
for i in cascade_infiles:
    dates.append(i[-13:-3])

ds_wind = ds_wind.rename({'phony_dim_7': 'time', 'phony_dim_8': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'
ds_wind['time']=np.arange(0,11,1/24)
ds_wind['time'].attrs['units'] = f'days after {dates[0]}'


# In[4]:


def bars(alti):
    bars = ds_wind.sel(alt=alti).hvplot.scatter(y=['u','v'], symmetric =True, ylim=[-100,100])     *ds_wind.sel(alt=alti).hvplot.errorbars(y='u', yerr1='u_err')     *ds_wind.sel(alt=alti).hvplot.errorbars(y='v', yerr1='v_err').opts(title=f'zonal (u) and meridional (v) flow in {alti} km')
    return (bars)


# In[5]:


gspec = pn.GridSpec(width=800, height=600, margin=5)
gspec[0:1, 0] = bars(80)
gspec[1:2, 0] = bars(90)
gspec[2:3, 0] = bars(100)
gspec


# In[6]:


#hvplot.help('scatter')


# In[ ]:




