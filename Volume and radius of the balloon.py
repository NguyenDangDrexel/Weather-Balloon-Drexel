
import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
#This program will plot the graph of dynamic viscosity in the range : H1 <= h <=  H2
# case = 1 constant volume 
# case = 2 isothermal process 
# case = 3 adiabatic

case = 4
H1 = 0 
H2 = 35000
#Initial volume 
V0 = 1 
# data_points that you want to make
data_points = 1000
# list of data to draw a plot 

volume_data = []
radius_data= [] 
data = np.linspace (H1,H2,data_points)

for i in range (data_points):
    if case ==  1: 
        volume_data.append(Volume_constant(V0 = V0))
        radius_data.append (Radius_constant (V0 = V0))
    elif case == 2: 
        volume_data.append(Volume_isothermal(data[i], V0 = V0))
        radius_data.append (Radius_isothermal (data[i],V0 = V0))
    elif case == 3: 
        volume_data.append(Volume_adiabatic(data[i],V0=V0))
        radius_data.append (Radius_adiabatic (data[i],V0=V0))
    elif case == 4:
        volume_data.append(Volume_out(data[i],V0 = V0 )) 
        radius_data.append (i)
fig,axes = plt.subplots (2,1)
axes[0].plot (data,volume_data )
axes[0].set_title ('Volume')
axes[0].grid (True)
axes[1].plot (data,radius_data)
axes[1].set_title ('Radius')
axes[1].grid (True)

plt.tight_layout
plt.legend ()
plt.show () 