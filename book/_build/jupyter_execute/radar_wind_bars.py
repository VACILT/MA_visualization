#!/usr/bin/env python
# coding: utf-8

# # Zonal and meridional wind by altidude
# 
# Use the tools provided in the toolbar to drag, zoom or save the plot as pdf for further use.

# In[1]:


import xarray as xr
#import holoviews.plotting.mpl
import pandas as pd
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import param
import numpy as np


# In[2]:


root_path = '/project/MA_vis/MA_visualization/data/'


# In[3]:


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


# In[4]:


hvc_opts = dict(x = 'time', y = 'alt')
con_err_v = ds_wind['v_err'].hvplot.contour(**hvc_opts)
con_err_u = ds_wind['u_err'].hvplot.contour(**hvc_opts)
bars = ds_wind.hvplot.scatter(y=['u','v'], symmetric =True, hover=False, ylim=[-100,100]) *ds_wind.hvplot.errorbars(y='u', yerr1='u_err') *ds_wind.hvplot.errorbars(y='v', yerr1='v_err').opts(toolbar=None)
bars


# In[5]:


hvplot.save(bars, 'bars.html')


# In[6]:


from IPython.display import HTML
HTML(filename="bars.html")

