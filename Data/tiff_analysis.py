
"""
Analyzing the Himalaya data from Ice velocity and thickness of the world’s glaciers, Nature (2022)
Paper link: https://www.nature.com/articles/s41561-021-00885-z
Data link: https://www.sedoo.fr/theia-publication-products/?uuid=55acbdd5-3982-4eac-89b2-46703557938c
RGI: 13-15
Mohammad Afzal Shadab and Shreyas Gaikwad
Date modified: 03/15/22
Email: mashadab@utexas.edu
"""

#Importing packages
#import netCDF4 as nc
import numpy as np
import netCDF4 as nc
from osgeo import gdal, ogr
import matplotlib.pyplot as plt

#Making classes
class dataset:
    def __init__(self):
        self.x = []
        self.y = []
        self.v = []
        self.vx = []

#A function to extract data
def extract(vel_filename,thickness_filename,ds_out):
    fn  = vel_filename + '.tif' 
    t_fn= thickness_filename + '.tif' 
    spatial_resolution = 50 #spatial resolution [m]
    #X  = gdal.Open(f'./RGI-13-15_velocity/X_{data}.tif')
    #Y  = gdal.Open(f'./RGI-13-15_velocity/Y_{data}.tif')

    V_file                  = gdal.Open(f'./RGI-13-15_velocity/V_{fn}')    
    V                       = V_file.GetRasterBand(1) 
    ds_out.V                = np.array(V.ReadAsArray())  #absolute velocity [m/yr]
    VX_file                 = gdal.Open(f'./RGI-13-15_velocity/VX_{fn}')
    VX                      = VX_file.GetRasterBand(1)
    ds_out.VX               = np.array(VX.ReadAsArray()) #x velocity [m/yr]
    VY_file                 = gdal.Open(f'./RGI-13-15_velocity/VY_{fn}')
    VY                      = VY_file.GetRasterBand(1)
    ds_out.VY               = np.array(VY.ReadAsArray()) #y velocity [m/yr]
    VSTDX_file              = gdal.Open(f'./RGI-13-15_velocity/STDX_{fn}')
    VSTDX                   = VSTDX_file.GetRasterBand(1)
    ds_out.VSTDX            = np.array(VSTDX.ReadAsArray()) #x velocity error [m/yr]
    VSTDY_file              = gdal.Open(f'./RGI-13-15_velocity/STDY_{fn}')
    VSTDY                   = VSTDY_file.GetRasterBand(1)
    ds_out.VSTDY            = np.array(VSTDY.ReadAsArray()) #y velocity error [m/yr]
    THICKNESS_file          = gdal.Open(f'./RGI-13-15_thickness/THICKNESS_{t_fn}')
    THICKNESS               = THICKNESS_file.GetRasterBand(1)
    ds_out.THICKNESS        = np.array(THICKNESS.ReadAsArray())     #thickness error [m]
    ERRTHICKNESS_file       = gdal.Open(f'./RGI-13-15_thickness/ERRTHICKNESS_{t_fn}')
    ERRTHICKNESS            = ERRTHICKNESS_file.GetRasterBand(1)
    ds_out.ERRTHICKNESS     = np.array(ERRTHICKNESS.ReadAsArray())  #thickness error [m]
    
    #ds_out.x = ds['x'][:]           #x location [m]
    #ds_out.y = ds['y'][:]           #y location [m]
    ds_out.x = spatial_resolution*np.linspace(0,np.shape(ds_out.VX)[1],np.shape(ds_out.VX)[1]) #x location [m]  
    ds_out.y = spatial_resolution*np.linspace(0,np.shape(ds_out.VX)[0],np.shape(ds_out.VX)[0]) #y location [m]    
    
    #Making a meshgrid
    ds_out.X,ds_out.Y = np.meshgrid(ds_out.x,ds_out.y)
    ds_out.filename = vel_filename
    return  ds_out

#A function to extract data
def plotting(ds_out):
    #Absolute velocity
    print('Max velocity', np.max(ds_out.V[~np.isnan(ds_out.V)]),    'm/yr \n',\
          'Min velocity', np.min(ds_out.V[~np.isnan(ds_out.V)]),    'm/yr \n',\
          'Avg velocity', np.average(ds_out.V[~np.isnan(ds_out.V)]),'m/yr \n')
    ds_out.V[ds_out.V>1e10] = np.nan
    fig = plt.figure(figsize=(15,7.5), dpi=100)
    plot = [plt.contourf(ds_out.X, ds_out.Y, ds_out.V,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Velocity (m/yr)')
    plt.ylabel(r'$y [m]$')
    plt.xlabel(r'$x [m]$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_velocity.pdf',bbox_inches='tight', dpi = 600)

    #Thickness 
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.THICKNESS,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Thickness (m)')
    plt.ylabel(r'$y (m)$')
    plt.xlabel(r'$x (m)$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_thickness.pdf',bbox_inches='tight', dpi = 600)
    
    
    '''
    #X velocity
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.VX,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'X - Velocity (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_Xvelocity.pdf',bbox_inches='tight', dpi = 600)
    
    #Y velocity
    fig = plt.figure(figsize=(15,7.5) , dpi=100)
    plot = [plt.contourf(ds_out.X,ds_out.Y, ds_out.VY,cmap="coolwarm")]
    clb = fig.colorbar(plot[0], orientation='vertical',aspect=50, pad=-0.1)
    clb.set_label(r'Y - Velocity (m/yr)')
    plt.ylabel(r'$y$')
    plt.xlabel(r'$x$')
    plt.axis('scaled')
    plt.savefig(f'{ds_out.filename}_Yvelocity.pdf',bbox_inches='tight', dpi = 600)
    '''

#filenames
data_vel     = 'RGI-13-15.1_2022February09' 
datathick    = 'RGI-13-15.1_2022February10'

#Extracting the data into a structure
dataset = extract(data_vel,datathick,dataset)

#Plotting the data
plotting(dataset)
