import matplotlib.pyplot as plt 
import numpy as np 
from Model import *

data = np.concatenate((np.linspace(0,11000,100), np.linspace(11000,25000,100), np.linspace(25000,35000,100)))

density = np.concatenate((density1(np.linspace(0,11000,100)), density2(np.linspace(11000,25000,100)), density3(np.linspace(25000,35000,100))))

plt.plot (data,density)

plt.title ('Density vs altitude')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Density kg/m^3')
plt.legend ()
plt.show ()  