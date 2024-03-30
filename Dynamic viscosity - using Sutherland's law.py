
import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
data = np.concatenate((np.linspace(0,11000,100), np.linspace(11000,25000,100), np.linspace(25000,35000,100)))

Viscosity = np.concatenate((vis1(np.linspace(0,11000,100)), vis2(np.linspace(11000,25000,100)), vis3(np.linspace(25000,35000,100))))

fig,axes = plt.subplots (1,1)
axes[0].plot (data,Viscosity )
axes[0].set_title ('Viscosity')
axes[0].set_xlabel ('Altitude(m)')
axes[0].set_ylabel ('Viscosity')

axes[0].grid (True)


plt.tight_layout
plt.legend ()
plt.show () 