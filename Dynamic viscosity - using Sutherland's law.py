
import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
#This program will plot the graph of dynamic viscosity in the range : H1 <= h <=  H2

H1 = 0 
H2 = 35000
# data_points that you want to make
data_points = 1000


viscosity_data = []

data = np.linspace (H1,H2,data_points)

for i in range (data_points):
    viscosity_data.append(Viscosity(data[i]))




plt.plot (data,viscosity_data )
plt.title ('Viscosity')
plt.xlabel ('Altitude(m)')
plt.ylabel ('Viscosity')

plt.grid (True)


plt.legend ()
plt.show () 