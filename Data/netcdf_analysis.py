
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

#Making classes
class ds2018:
    def __init__(self):
        self.x = []
        self.y = []
        self.v = []
        self.vx = []

#A function to extract data
def extract(filename,ds_out):
    fn = filename + '.nc'    
    ds = nc.Dataset(fn)      #importing the file
    print(ds)                #checking datasets
    ds_out.filename = filename
    ds_out.x = ds['x'][:]           #x location [m]
    ds_out.y = ds['y'][:]           #y location [m]
    ds_out.v = ds['v'][:]           #absolute velocity [m/yr]
    ds_out.vx = ds['vx'][:]         #x velocity [m/yr]
    ds_out.vy = ds['vy'][:]         #y velocity [m/yr]
    ds_out.v_err  = ds['v_err'][:]  #absolute velocity error [m/yr]
    ds_out.vx_err = ds['vx_err'][:] #x velocity error [m/yr]
    ds_out.vy_err = ds['vy_err'][:] #y velocity error [m/yr]
    ds_out.date = ds['date'][:]     #Effective date since 01 Jan 0000
    ds_out.dt   = ds['dt'][:]       #Effective image pair date separation
    ds_out.count= ds['count'][:]    #Number of velocitites in the weighted average
    ds_out.chip_size= ds['chip_size_max'][:] #Maxium accepted search chip size
    ds_out.ocean= ds['ocean'][:]    #Ocean mask
    ds_out.rock = ds['rock'][:]     #Rock mask
    ds_out.ice  = ds['ice'][:]      #Ice mask
    
    #Making a meshgrid
    ds_out.X,ds_out.Y = np.meshgrid(ds2018.x,ds2018.y)
    
    return ds_out

#A function to extract data
def plotting(ds_out):
    #Absolute velocity
    print('Max velocity', np.max(ds_out.v[~np.isnan(ds_out.v)]),    'm/yr \n',\
          'Min velocity', np.min(ds_out.v[~np.isnan(ds_out.v)]),    'm/yr \n',\
          'Avg velocity', np.average(ds_out.v[~np.isnan(ds_out.v)]),'m/yr \n')
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X, ds_out.Y, ds_out.v,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Velocity (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_velocity.pdf',bbox_inches='tight', dpi = 600)
    
    #Absolute velocity error
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.v_err,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Velocity error (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_velocity_error.pdf',bbox_inches='tight', dpi = 600)
    
    #X velocity
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.vx,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'X - Velocity (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_Xvelocity.pdf',bbox_inches='tight', dpi = 600)
    
    #Y velocity
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.vy,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Y - Velocity (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_Yvelocity.pdf',bbox_inches='tight', dpi = 600)


#Extracting the data into a structure
ds2018 = extract('HMA_G0240_2018',ds2018)

#Plotting the data
plotting(ds2018)




