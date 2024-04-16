
import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
#This program will plot the graph of dynamic viscosity in the range : H1 <= h <=  H2

H1 = 0 
H2 = 35000
# data_points that you want to make
data_points = 1000
# list of data to draw a plot 
volume_isothermal_data = []
radius_isothermal_data= [] 
data = np.linspace (H1,H2,data_points)

for i in range (data_points):
    volume_isothermal_data.append(Volume_isothermal(data[i]))
    radius_isothermal_data.append (Radius_isothermal (data[i]))

fig,axes = plt.subplots (2,1)
axes[0].plot (data,volume_isothermal_data )
axes[0].set_title ('Volume')
axes[0].grid (True)
axes[1].plot (data,radius_isothermal_data)
axes[1].set_title ('Radius')
axes[1].grid (True)

plt.tight_layout
plt.legend ()
plt.show () 