
"""
Analyzing the Himalaya data from Its live NASA (https://nsidc.org/apps/itslive/)
Mohammad Afzal Shadab and Shreyas Gaikwad
Date modified: 01/22/22
Email: mashadab@utexas.edu
"""

#Packages
import netCDF4 as nc


fn = 'HMA_G0240_2018.nc' #importing the file
ds = nc.Dataset(fn)      #making datasets
print(ds)                #checking datasets

