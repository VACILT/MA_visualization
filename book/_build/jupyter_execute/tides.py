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
ds_info = xr.open_dataset(cascade_infiles[0],group ='info', engine='netcdf4')
ds_info['date']
ds_tides = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['phony_dim_7'],group ='tides', combine = 'nested', engine='netcdf4')
ds_tides = ds_tides.rename({'phony_dim_6': 'alt','phony_dim_7': 'time'})
ds_tides['alt'] = ds_info['alt'].squeeze().values
ds_tides['alt'].attrs['units'] = 'km'
restr = lambda x: int(x[0])
year, month, day = map(restr, ds_info['date'].values)
ds_tides['time']=pd.date_range(f'{year}-{month:02d}-{day:02d}', periods = len(cascade_infiles)-1)


# In[3]:


graph_opts = dict(cmap = 'viridis', logy = False, colorbar = True,  line_width=2)
graph_u=ds_tides.hvplot.contour(x = 'time', y = 'alt', z='A12u', levels=25).opts(**graph_opts, title='u').redim.range(A12u=(0, 60))
graph_v=ds_tides.hvplot.contour(x = 'time', y = 'alt', z='A12v', levels=25).opts(**graph_opts, title='v').redim.range(A12v=(0, 60))
tides=(graph_u + graph_v).cols(1)


# In[4]:


hvplot.save(tides, 'tides.html')


# In[5]:


from IPython.display import HTML
HTML(filename="tides.html")


# In[ ]:





# In[ ]:




