import matplotlib.pyplot as plt 
import numpy as np 
from Model import *

data = np.concatenate((np.linspace(0,11000,100), np.linspace(11000,25000,100), np.linspace(25000,35000,100)))

pressure = np.concatenate((derived_pressure1(np.linspace(0,11000,100)), derived_pressure2(np.linspace(11000,25000,100)), derived_pressure3(np.linspace(25000,35000,100))))

plt.plot (data,pressure)

plt.title ('Derived function vs NASA curve-fitting function')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Pressure kg/m^3')
plt.legend ()
plt.show ()  