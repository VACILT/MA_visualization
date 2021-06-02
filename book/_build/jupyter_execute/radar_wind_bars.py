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
from bokeh.plotting import figure, show, output_notebook
output_notebook()


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


bars = ds_wind.hvplot.scatter(y=['u','v'], symmetric =True, ylim=[-100,100], groupby='alt')


# In[5]:


#hvplot.help('scatter')


# In[6]:


bars


# In[7]:


from bokeh.embed import file_html
from bokeh.resources import CDN
import IPython

html_repr = file_html(pn.Column(bars).get_root(), CDN)
IPython.display.HTML(html_repr)


# In[ ]:




