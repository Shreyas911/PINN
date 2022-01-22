
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
v = ds['v'][:]           #absolute velocity [m/yr]
vx = ds['vx'][:]         #x velocity [m/yr]
vy = ds['vy'][:]         #y velocity [m/yr]
v_err  = ds['v_err'][:]  #absolute velocity error [m/yr]
vx_err = ds['vx_err'][:] #x velocity error [m/yr]
vy_err = ds['vy_err'][:] #y velocity error [m/yr]

#Making a meshgrid
X,Y = np.meshgrid(x,y)

#PLOTTING
#Absolute velocity
print('Max velocity', np.max(v[~np.isnan(v)]),    'm/yr \n',\
      'Min velocity', np.min(v[~np.isnan(v)]),    'm/yr \n',\
      'Avg velocity', np.average(v[~np.isnan(v)]),'m/yr \n')
fig = plt.figure(figsize=(15,7.5) , dpi=100)
plot = [plt.contourf(X, Y, v,cmap="Blues")]
clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
plt.ylabel(r'$z$')
plt.xlabel(r'$x$')
plt.axis('scaled')
plt.savefig(f'HMA_G0240_2018_velocity.pdf',bbox_inches='tight', dpi = 600)