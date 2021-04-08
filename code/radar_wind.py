# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

#root_path = '/projekt1/radar/webtool/'
root_path = '/project/MA_vis/MA_visualization/data/'

ds_info = xr.open_dataset(f'{root_path}MR_wind_2021_01_07.h5', group = 'info')
#ds_info

# ## Getting Metadata

year = int(ds_info['date'].values[0,0])
month =int(ds_info['date'].values[1,0])
day =int(ds_info['date'].values[2,0])
date = str(day)+"."+str(month)+"."+str(year)
date

ds_wind = xr.open_dataset(f'{root_path}MR_wind_2021_01_07.h5', group = 'wind')
ds_wind

ds_wind['u']
ds_wind.rename({'phony_dim_6': 'alt', 'phony_dim_7': 'time'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'

ds_wind['u'].plot(x= 'phony_dim_6', y = 'phony_dim_7')

# ## 2d plot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ds_wind_sel = ds_wind.isel(phony_dim_6=0)
ds_wind_sel['u'].plot(y = 'phony_dim_7', label='u')
ds_wind_sel['v'].plot(y = 'phony_dim_7', label='v')
#ds_wind_sel['w'].plot(y = 'phony_dim_7')
ax.set_title('Collm zonal and merdional wind on '+ date)
plt.legend()
plt.show()


