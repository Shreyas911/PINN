
"""
Analyzing the Himalaya data from Its live NASA (https://nsidc.org/apps/itslive/)
Mohammad Afzal Shadab and Shreyas Gaikwad
Date modified: 01/22/22
Email: mashadab@utexas.edu
"""

#Importing packages
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

fn = 'HMA_G0240_2018.nc' #importing the file
ds = nc.Dataset(fn)      #making datasets
print(ds)                #checking datasets

x = ds['x'][:]           #x location [m]
y = ds['y'][:]           #y location [m]
v = np.shape(ds['v'][:]) #absolute velocity [m/yr]


X,Y = np.meshgrid(x,y)

fig = plt.figure(figsize=(15,7.5) , dpi=100)
plot = plt.contourf(X, Y, v)#,cmap="Blues",vmin = np.min(v), vmax = np.max(v))]
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
plt.ylabel(r'$z$')
plt.xlabel(r'$x$')
#plt.xlim([Grid.xmin, Grid.xmax])
#plt.ylim([Grid.ymax,Grid.ymin])
#plt.axis('scaled')
plt.savefig(f'HMA_G0240_2018_velocity.pdf',bbox_inches='tight', dpi = 600)