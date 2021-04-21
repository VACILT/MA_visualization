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
import panel as pn
import hvplot.xarray
import holoviews as hv
import glob
import param
import numpy as np
hv.extension('bokeh')
pn.extension()

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

date_selec   =  pn.widgets.Select(name='date', options=dates[0:11], inline=True)

ds_wind = ds_wind.rename({'phony_dim_6': 'time', 'phony_dim_7': 'alt'})
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

con_err_u

graph_opts = dict(cmap = 'RdBu_r', symmetric=True, logy = False, colorbar = True)
graph_top=ds_wind['u'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts)
graph_bottom=ds_wind['v'].hvplot.quadmesh(x = 'time', y = 'alt' ).opts(**graph_opts)


@pn.depends(date_sel=date_selec.param.value)
def choise(date_sel):
    first_column = pn.pane.Markdown(f'#### Testtext')
    hv_panel_top[1][0][0].value=date_sel
    hv_panel_bottom[1][0][0].value=date_sel
    box = pn.WidgetBox(date_selec, width=390)
    return (box)


# +
#plot_wind=ds_wind[['u','v']].to_array().plot(row="variable", x="time")
# -


hv_panel_top = pn.panel(graph_top*con_err_v)
hv_panel_bottom = pn.panel(graph_bottom*con_err_u)
gspec = pn.GridSpec(width=800, height=600, margin=5)
gspec[0:4, 0] = hv_panel_top[0]
gspec[0:4, 1] = hv_panel_bottom[0]
gspec[4, 0] = choise
#hv_panel_bottom.pprint()
gspec


