# This program comparing the difference between using Stoke law and Drag equation to calculate the drag force for the balloon 
# Given the following values: V_0 = 1.5 m^3; rho_0 = 1.225 kg/m^3; rho_He - 0.1785 kg/m^3
# Result: we can't use Stoke's Law as this function would result in a completely wrong result 
# In This program, we I try use the function to calculate Cd (Re) and Re(x,x'), but the model fails. => Solutions: use constant value for drag coefficient/ find a simpler equation
# Update: 30/3/2024 1:35am. Run successfully with no change in code 
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
import math 
from Model import * 


initial_conditions = [0,0] 
time_points = np.linspace (0,65,100000)
time_points2 = np.linspace (0,6000,1000)
# defining the function 
# IMPORTANT: the form of the function matter. we need to put the highest order on left side, and the rest on the right side 
# Volume increase with altitude 

#defining function for Reynold number
def Re (x,xdot):
    Re = (density1(x) * xdot * 2 * Radius1(x)) / vis1(x)
    return Re 

def Cd (x,xdot) :
    #Fail when calculate Cd(Re)
    Cd = 24 / Re (x,xdot) + (2.6 * (Re (x,xdot)/5)) / (1 + (Re (x,xdot)/5)** (1.52)) + (0.411 * (Re (x,xdot)/2.63 * 10 ** (5))** (-7.94))/(1 + (Re (x,xdot)/(2.63 * 10 ** 5))**(-8)) + ((0.25 * Re (x,xdot) / 10**6)/(1 + Re (x,xdot)* 10**6)) - 0.04
   # Cd = 0.12
    return Cd 
    

def function (y,t): 
    x,x_dot = y   
    x_ddot = 5.4 - 6 * np.pi * vis1(x) * Radius1(x) * x_dot
    return x_dot, x_ddot 

# Using drag equation 
def function2 (y,t):
    x,xdot = y
    xddot = 5.4 - 1/2 *density1(x) * xdot**2 * np.pi * Radius1(x)**2 
    #xddot =  1 - 1/2 * 0.3 * xdot**2*density1(x)*Radius1(x)**2
    return xdot,xddot 

solution = odeint (function, y0= [0,0], t = time_points) 
solution2 = odeint (function2, y0= [0,0], t = time_points2) 


x_sol = solution[:,0]
x_dot_sol = solution [:,1]

x_sol2 = solution2[:,0]
x_dot_sol2 = solution2[:,1]

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
# labeling the whole graoh 
fig.suptitle ('Comparing between Drag equation and Stoke law')
# Plot the first graph with customized y-axis ticks
axes[0,0].plot(time_points, x_sol, color='blue')
axes[0,0].set_title('Using Stoke law')
axes[0,0].set_xlabel ('t(s)')
axes[0,0].set_ylabel ('h(m)')
axes[0,0].grid(True)  # Add gridlines
axes[0,0].set_yticks(range(0,11001,1000))  # Customize y-axis ticks

# Plot the second graph with customized y-axis ticks
axes[1,0].plot(time_points, x_dot_sol, color='red')
axes[1,0].set_title('Using Stoke law') 
axes[1,0].set_xlabel ('t(s)')
axes[1,0].set_ylabel ('h(m)')
axes[1,0].grid(True)  
# third plot 
axes[0,1].plot(time_points2, x_sol2, color='blue')
axes[0,1].set_title('Using drag equation') 
axes[0,1].set_xlabel ('t(s)')
axes[0,1].set_ylabel ('h(m/s)')
axes[0,1].grid(True)  
# fourth plot 
axes[1,1].plot(time_points2, x_dot_sol2, color='blue')
axes[1,1].set_title('Using drag equation') 
axes[1,1].set_xlabel ('t(s)')
axes[1,1].set_ylabel ('v(m/s)')
axes[1,1].grid(True)  

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


