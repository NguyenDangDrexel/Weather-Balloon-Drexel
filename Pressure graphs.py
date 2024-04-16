import matplotlib.pyplot as plt 
import numpy as np 
from Model import *


#This program will plot the graph of pressure in the range : H1 <= h <=  H2

H1 = 0 
H2 = 1000
# data_points that you want to make
data_points = 1000


pressure_data = []

data = np.linspace (H1,H2,data_points)

for i in range (data_points):
    pressure_data.append(Pressure(data[i]))
plt.plot (data,pressure_data)

plt.title ('Pressure vs altitude')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Pressure kg/m^3')
plt.legend ()
plt.show ()  