#!/usr/bin/env python
# coding: utf-8

# In[3]:


import xarray as xr
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import hvplot.pandas
import glob
import numpy as np
import pandas as pd
import datetime
import geopandas as gpd
import sys
import os
from bokeh.resources import INLINE

# In[14]:


date_format = '%Y%m%d' 
sdate_str = sys.argv[1]
edate_str = sys.argv[2] # '20210104'#
root_path = '/projekt1/radar/webtool/'


# In[23]:


sdate = datetime.datetime.strptime(sdate_str, date_format)       # as timedelta
edate = datetime.datetime.strptime(edate_str, date_format) 
delta = edate-sdate

infile_ls = []
for i in range(delta.days + 1):
    day = sdate + datetime.timedelta(days=i)
    infile = f'{root_path}hdf_files/MR_wind_{day.strftime(date_format)}.h5'
    #print(infile)
    infile_ls.append(infile)


# In[ ]:


ds_wind = xr.open_mfdataset(infile_ls, concat_dim=['phony_dim_8'], group ='wind', combine = 'nested', engine='netcdf4')

ds_info = xr.open_dataset(infile_ls[0], group = 'info',  engine='netcdf4')
ds_info2 = xr.open_dataset(infile_ls[-1], group = 'info',  engine='netcdf4')

ds_wind = ds_wind.rename({'phony_dim_8': 'time', 'phony_dim_9': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'

restr = lambda x: int(x[0])
year, month, day = map(restr, ds_info['date'].values)
year2, month2, day2 = map(restr, ds_info2['date'].values)

ds_wind['time']=pd.date_range(start=f'{year}-{month:02d}-{day:02d}', 
                              freq = '1H', 
                              periods = (len(infile_ls))*24)

# tides
ds_tides = xr.open_mfdataset(infile_ls, concat_dim=['phony_dim_7'],group ='tides', combine = 'nested', engine='netcdf4')
ds_tides = ds_tides.rename({'phony_dim_7': 'time', 'phony_dim_6': 'alt'})

ds_tides['alt'] = ds_info['alt'].squeeze().values
ds_tides['alt'].attrs['long_name'] = 'altitude'
ds_tides['alt'].attrs['units'] = 'km'

ds_tides['time']=pd.date_range(start=f'{year}-{month:02d}-{day:02d}', 
                              freq = '1D', 
                              periods = (len(infile_ls)))
for var in ['A12u', 'A12v', 'A24u', 'A24v']:
    temp = ds_tides[var].attrs
    ds_tides[var].attrs['units'] = list(temp.items())[0][1].split('/ ')[-1]
    ds_tides[var].attrs['long_name'] = list(temp.items())[0][0]

# In[ ]:


ds_info['alt_dist'].attrs['long_name'] = 'altitude'
ds_info['alt_dist'].attrs['units'] = 'km'
mean_count=str(np.array(ds_info['alt_dist']).mean().round(decimals=1))
total_counts=str(len(np.array(ds_info['alt_dist'][0])))
alt_count=ds_info['alt_dist'].hvplot.hist(xlim=[60,120],bins=100, invert=True,                                          title=f'Mean altitude: {mean_count}               Total Counts: {total_counts}')
data=dict(lat=np.array(ds_info['geo_lat'][0]),lon=np.array(ds_info['geo_lon'][0]))
df=pd.DataFrame.from_dict(data)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
meteo_loc=gdf.hvplot(geo=True,tiles=True, color='blue', alpha=0.2)
meteo=(alt_count + meteo_loc).cols(2)


# In[ ]:


graph_opts = dict(cmap = 'RdBu_r', symmetric=True, logy = False, colorbar = True)
graph_u=ds_wind['u'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='u').redim.range(u=(-100, 100))
graph_v=ds_wind['v'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts, title='v').redim.range(v=(-100, 100))
row_2=(graph_u + graph_v).cols(2)

graph_opts = dict(cmap = 'viridis', logy = False, colorbar = True,  line_width=2)
graph_u=ds_tides['A24u'].hvplot.contour(x = 'time', y = 'alt',  
                                levels = 21).opts(**graph_opts, title='u').redim.range(A24u=(0, 25))
graph_v=ds_tides['A24v'].hvplot.contour(x = 'time', y = 'alt', levels = 21).opts(**graph_opts, title='v').redim.range(A24v=(0, 25))
row_3=(graph_u + graph_v).cols(2)


graph_opts = dict(cmap = 'viridis', logy = False, colorbar = True,  line_width=2)
graph_u=ds_tides['A12u'].hvplot.contour(x = 'time', y = 'alt',  
                                levels = 21).opts(**graph_opts, title='u').redim.range(A12u=(0, 60))
graph_v=ds_tides['A12v'].hvplot.contour(x = 'time', y = 'alt', levels = 21).opts(**graph_opts, title='v').redim.range(A12v=(0, 60))
row_4=(graph_u + graph_v).cols(2)


#heatmap=(alt_count + meteo_loc+row_2).cols(2)
heatmap = pn.Column(pn.Row(alt_count, meteo_loc),pn.pane.Markdown("#Wind measurements", align="center"), row_2, 
                    pn.pane.Markdown("#Diurnal tide amplitude", align="center"), row_3, 
                    pn.pane.Markdown("#Semidiurnal tide amplitude", align="center"), row_4)
#heatmap


# In[ ]:

outpath=f'{root_path}heatmap_files/{year}/'
outfile = f'{outpath}heatmap_{sdate.strftime(date_format)}-{edate.strftime(date_format)}.html'
print(outfile)
try:
    os.mkdir(outpath)
except OSError as error:
    print(error)
#hvplot.save(heatmap, outfile, resources=INLINE)
heatmap.save(outfile, resources=INLINE)

