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
import matplotlib.pyplot as plt
import panel as pn
import hvplot.xarray
import glob
import param
import numpy as np

#root_path = '/projekt1/radar/webtool/'
root_path = '/project/MA_vis/MA_visualization/data/'

cascade_infiles = sorted(glob.glob(f'{root_path}*.h5'))
ds_wind = xr.open_mfdataset(cascade_infiles[0:11], concat_dim=['date'],group ='wind', combine = 'nested')
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info')
dates=[]
for i in cascade_infiles:
    dates.append(i[-13:-3])
ds_wind['date'] = dates[0:11]

# ## Prepare Dateset

# +
#ds_wind = xr.open_dataset(cascade_infiles[i_file], group = 'wind')
#ds_tides= xr.open_dataset(cascade_infiles[i_file], group = 'tides')
#ds_wind
# -

ds_wind = ds_wind.rename({'phony_dim_7': 'time', 'phony_dim_8': 'alt'})
ds_wind['alt'] = ds_info['alt'].squeeze().values
ds_wind['alt'].attrs['long_name'] = 'altitude'
ds_wind['alt'].attrs['units'] = 'km'
ds_wind['time'].attrs['units'] = 'h'
ds_wind['time']=np.arange(1,25,1)
#ds_wind

# +
hvc_opts = dict(x = 'time', y = 'alt')

con_err_v = ds_wind['v_err'].hvplot.contour(**hvc_opts)
con_err_u = ds_wind['u_err'].hvplot.contour(**hvc_opts)
# -

bars = ds_wind.hvplot.scatter(y=['u','v'], symmetric =True, hover=False, ylim=[-100,100]) \
*ds_wind.hvplot.errorbars(y='u', yerr1='u_err') \
*ds_wind.hvplot.errorbars(y='v', yerr1='v_err').opts(toolbar=None)


bars

# +
#hvplot.help('scatter')
