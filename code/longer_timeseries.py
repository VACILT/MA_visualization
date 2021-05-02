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
ds_info = xr.open_dataset(cascade_infiles[0], group = 'info')


# ## Prepare Dateset

# +
#ds_wind = xr.open_dataset(cascade_infiles[i_file], group = 'wind')
#ds_tides= xr.open_dataset(cascade_infiles[i_file], group = 'tides')
#ds_wind
# -

def fix_dataset(i):
    ds_wind =xr.open_dataset(cascade_infiles[i],group ='wind')
    ds_wind = ds_wind.rename({'phony_dim_7': 'time', 'phony_dim_8': 'alt'})
    ds_wind['alt'] = ds_info['alt'].squeeze().values
    ds_wind['alt'].attrs['long_name'] = 'altitude'
    ds_wind['alt'].attrs['units'] = 'km'
    ds_wind['time'].attrs['units'] = 'h'
    ds_wind['time']=np.arange(24*i+1,24*i+25,1)
    return ds_wind


array=xr.merge([fix_dataset(0)['u'], fix_dataset(1)['u'], fix_dataset(2)['u'], fix_dataset(3)['u']], compat='no_conflicts', join='outer')
array

plot=array['u'].plot(x='time', size=7)




