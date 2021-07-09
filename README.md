# Middle-atmosphere data processing and visualization

The main goal is to prepare new website visulization of meteor-radar station in Collm solely in python (see [here](https://meteo.physgeo.uni-leipzig.de/de/wetterdaten/radar.php)).

Click on this Badge to get access to Binder. Binder sets up an environment without the need of an python-installation. It is possible to explore this project independent of the system!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VACILT/MA_visualization.git/HEAD)

## Roadmap
- [ ] visualization of preprocessed meteor-radar files
  - [x] wind measurements
  - [x] tides
  - [ ] daily temperatures derived from the decay of in-dividual underdense meteor trails (Hocking, 1999; Hockinget al., 2001; [Stober et al., 2008](https://www.sciencedirect.com/science/article/abs/pii/S0273117707010629?via%3Dihub); [Jacobi et al. (2016)](https://ars.copernicus.org/articles/14/169/2016/))
  - [ ] long-term characteristics (trends, climatology etc.)
- [ ] processing of mdp files 
- [ ] add visualization of other datasets
  - [ ] ICON@DWD (see [here](https://github.com/VACILT/PV_characteristics_ICON-NWP)) up to 80 km
  - [ ] [GFSv16 up to 0.01 hPa](https://twitter.com/SimonLeeWx/status/1374297378891706370)
  - [ ] [GEOS-5 FP](https://gmao.gsfc.nasa.gov/GMAO_products/) up to 0.01 hPa 
