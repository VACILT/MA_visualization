#!/usr/bin/env python
# coding: utf-8

# # Distribution of meteors
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
#ds_info = ds_info.rename({'phony_dim_2': 'point'})
ds_info['alt_dist'].attrs['long_name'] = 'altitude'
ds_info['alt_dist'].attrs['units'] = 'km'


# In[3]:


mean_count=str(np.array(ds_info['alt_dist']).mean().round(decimals=1))
total_counts=str(len(np.array(ds_info['alt_dist'][0])))
alt_count=ds_info['alt_dist'].hvplot.hist(xlim=[60,120],bins=100, invert=True,                                          title=f'Mean altitude: {mean_count}               Total Counts: {total_counts}')


# In[4]:


import hvplot.pandas
import geopandas as gpd
#pd.options.plotting.backend = 'holoviews'
data=dict(lat=np.array(ds_info['geo_lat'][0]),lon=np.array(ds_info['geo_lon'][0]))
df=pd.DataFrame.from_dict(data)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
meteo_loc=gdf.hvplot(geo=True,tiles=True, color='blue', alpha=0.2)


# In[5]:


meteo=(alt_count + meteo_loc).cols(1)


# In[6]:


hvplot.save(meteo, 'meteo.html')


# In[7]:


from IPython.display import HTML
HTML(filename="meteo.html")


# In[ ]:




