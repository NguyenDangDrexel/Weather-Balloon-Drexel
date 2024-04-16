"""
This program solving the dynamic equation by using odeint (). In this program, the following assumptions are made: 
1. Drag coefficient is constant; Cd = 0.3. We will need different analytical solution if we change Cd 
2. Density, Radius change with altitdue 
3. Density of atmosphere and Helium = 1.293 and 0.166 (kg/m^3), respectively 
4. Total mass of balloon: 1 (kg)
5. Initial Radius = 1 (m^3) 




"""
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
import math 
from Model import * 


initial_conditions = [0,1] 
time_points2 = np.linspace (0,20,1000)

#Drag coefficient 
Cd = 0.3 
# defining the function 
# IMPORTANT: the form of the function matter. we need to put the highest order on left side, and the rest on the right side 

def function (y,t):
    x,xdot = y
    xddot = 33.74 - 1/2 *Density(x) * xdot**2 * np.pi * Radius_isothermal(x,V0=4.2)**2*Cd 
    return xdot,xddot 

solution2 = odeint (function, y0= [0,1], t = time_points2) 



x_sol2 = solution2[:,0]
x_dot_sol2 = solution2[:,1]

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
# labeling the whole graoh 
fig.suptitle ('Analytical solution and odeint ()')

# first plot 
axes[0,0].plot(time_points2, x_sol2, color='blue')
axes[0,0].set_title('Altitude - odeint ') 
axes[0,0].set_xlabel ('t(s)')
axes[0,0].set_ylabel ('h(m/s)')
axes[0,0].grid(True)  
# second plot 
axes[0,1].plot(time_points2, x_dot_sol2, color='blue')
axes[0,1].set_title('Velocity - odeint ') 
axes[0,1].set_xlabel ('t(s)')
axes[0,1].set_ylabel ('v(m/s)')
axes[0,1].grid(True)  

#Analytical solution for the dynamic equation, with the assumptions that pressure, density is constant 
# Function for velocity
def v (t): 
    v = 7.9 * ((np.exp(t/0.1)-1)/(np.exp(t/0.1)+1))
    return v 

def x(t): 
    x = 7.9 * (0.2 * np.log (np.exp (t/0.1)+1)-t) - 1.1
    return x
velocity_data= [] 
altitude_data= [] 
time = []
t = 0 
while t < 20: 
    velocity_data.append (v(t))
    time.append(t)
    altitude_data.append(x(t))
    t+= 20/1000

print (x(1))


axes[1,0].plot(time, altitude_data, color='blue')
axes[1,0].set_title('Altitude - analytical') 
axes[1,0].set_xlabel ('t(s)')
axes[1,0].set_ylabel ('h(m)')
axes[1,0].grid(True) 

axes[1,1].plot(time, velocity_data, color='blue')
axes[1,1].set_title('Velocity - analytical ') 
axes[1,1].set_xlabel ('t(s)')
axes[1,1].set_ylabel ('v(m/s)')
axes[1,1].grid(True) 


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


