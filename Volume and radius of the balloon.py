
import matplotlib.pyplot as plt 
import numpy as np 
from Model import *
data = np.concatenate((np.linspace(0,11000,100), np.linspace(11000,25000,100), np.linspace(25000,35000,100)))

volume = np.concatenate((Volume1(np.linspace(0,11000,100)), Volume2(np.linspace(11000,25000,100)), Volume3(np.linspace(25000,35000,100))))
radius = np.concatenate((Radius1(np.linspace(0,11000,100)), Radius2(np.linspace(11000,25000,100)), Radius3(np.linspace(25000,35000,100))))

fig,axes = plt.subplots (2,1)
axes[0].plot (data,volume )
axes[0].set_title ('Volume')
axes[0].grid (True)
axes[1].plot (data,radius)
axes[1].set_title ('Radius')
axes[1].grid (True)

plt.tight_layout
plt.legend ()
plt.show () 