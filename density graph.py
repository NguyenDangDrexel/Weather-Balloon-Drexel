import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
#This program will plot the graph: H1 <= h <=  H2

H1 = 0 
H2 = 35000
# data_points that you want to make
data_points = 10000


density_data = []

data = np.linspace (H1,H2,data_points)

for i in range (data_points):
    density_data.append(Density(data[i]))


plt.plot (data,density_data)

plt.title ('Density vs altitude')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Density kg/m^3')
plt.legend ()
plt.show ()  






