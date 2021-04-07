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
ds_info['alt']

ds_test = xr.open_dataset(f'{root_path}MR_wind_2021_01_07.h5')


