#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import param
import numpy as np


# In[2]:


#root_path = '/projekt1/radar/webtool/'
root_path = '/project/MA_vis/MA_visualization/data/'


# In[3]:


cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_wind = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['date'],group ='wind', combine = 'nested')
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info')
dates=[]
for i in cascade_infiles:
    dates.append(i[-13:-3])
ds_wind['date'] = dates[0:11]


# ## Prepare Dateset

# In[4]:


#ds_wind = xr.open_dataset(cascade_infiles[i_file], group = 'wind')
#ds_tides= xr.open_dataset(cascade_infiles[i_file], group = 'tides')
#ds_wind


# In[5]:


ds_wind = ds_wind.rename({'phony_dim_7': 'time', 'phony_dim_8': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'
ds_wind['time'].attrs['units'] = 'h'
ds_wind['time']=np.arange(1,25,1)
#ds_wind


# In[6]:


hvc_opts = dict(x = 'time', y = 'alt')

con_err_v = ds_wind['v_err'].hvplot.contour(**hvc_opts)
con_err_u = ds_wind['u_err'].hvplot.contour(**hvc_opts)


# In[7]:


bars = ds_wind.hvplot.scatter(y=['u','v'], symmetric =True, hover=False, ylim=[-100,100]) *ds_wind.hvplot.errorbars(y='u', yerr1='u_err') *ds_wind.hvplot.errorbars(y='v', yerr1='v_err').opts(toolbar=None)


# In[8]:


bars


# In[9]:


#hvplot.help('scatter')

