"""
This program solving the dynamic equation by using odeint (). In this program, the following assumptions are made: 
1. Drag coefficient is constant; Cd = 0.44. 
2. Density, Radius change with altitdue 
3. Density of atmosphere and Helium = 1.293 and 0.166 (kg/m^3), respectively 
4. Total mass of balloon: 7 (kg)
5. Initial Radius = 15.05 (m^3) 
# 
"""
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
import math 
from Model import * 
from SteadyStateSolution import * # note that whenever you change case, you need to change case in V_terminal file 

# case 1: constant volume, case 2: isothermal; case 3: adiabatic; case 4: t_in = t_out 
case = 2
# Want to compare with the steady state solution ??? 
compare = False  
#want to include m_air ??? 
include_m_air  = True 
#Drag coefficient  
Cd = 0.44
V0 = 15.05
m = 7
C = 0.5 # m_air = C * rho * V 
g = 9.8 




if case == 1: 
    time_points2 = np.linspace (0,2000,10000) # when h = max 
elif case == 2: 
    time_points2 = np.linspace (0,2960,10000) # when h = 35000 
elif case == 3: 
    time_points2 = np.linspace (0,4400,10000) # when t larger than this value, odeint fails 
elif case ==4: 
    time_points2 = np.linspace (0,3200,10000)

initial_conditions = [0,0] 


# defining the function 
# IMPORTANT: the form of the function matter. we need to put the highest order on left side, and the rest on the right side 
def function (y,t):
    x,xdot = y
    if case == 1: 
        V = Volume_constant (V0) 
        A = Area_constant(V0)
    elif case == 2: 
        V = Volume_isothermal(x,V0=V0) 
        A = Area_isothermal(x,V0)
    elif case == 3: 
        V = Volume_adiabatic (x,V0=V0)
        A = Area_adiabatic (x,V0=V0)
    elif case  == 4: 
        V = Volume_out (x,V0=V0)
        A = Area_out (x,V0=V0)
    if include_m_air:
        m_air = C*Density(x) * V 
    else: 
        m_air = 0 

 
    xddot = (-m*g + Density(x)*V *g)/ (m +m_air)  - 1/2 *Density(x) * xdot**2 * A*Cd /(m + m_air)  
    
    return xdot,xddot 

solution2 = odeint (function, y0= [0,0], t = time_points2) 

x_sol2 = solution2[:,0]
x_dot_sol2 = solution2[:,1]


# Create a figure and axes with 1 row and 2 columns
if compare: 
    fig, axes = plt.subplots(1, 3, figsize=(8, 6))
else: 
    fig, axes = plt.subplots(1, 2, figsize=(8, 6))

if case  == 1:
    fig.suptitle('numerical solution - constant volume balloon')
elif case == 2:
    fig.suptitle('numerical solution - isothermal balloon')

elif case == 3:
    fig.suptitle('numerical solution - adiabatic balloon')

elif case == 4: 
    fig.suptitle('numerical solution - Tin_=T_out balloon')

# First plot
axes[0].plot(time_points2, x_sol2, color='blue')
axes[0].set_title('Altitude - odeint')
axes[0].set_xlabel('t(s)')
axes[0].set_ylabel('h(m/s)')
axes[0].grid(True)

    # Second plot
axes[1].plot(time_points2, x_dot_sol2, color='blue')
axes[1].set_title('Velocity - odeint')
axes[1].set_xlabel('t(s)')
axes[1].set_ylabel('v(m/s)')
axes[1].grid(True)
if compare:
# third plot: comparing numerical solution vs steady-state solution 
    axes[2].plot(x_sol2, x_dot_sol2, color='blue')
    axes[2].scatter(Altitude_data,terminal_velocity_data, color='red', s = 10)
    axes[2].set_title('numerical solution vs steady-state solution')
    axes[2].set_xlabel('h(m)')
    axes[2].set_ylabel('v(m/s)')
    axes[2].grid(True)



plt.tight_layout()

plt.show()


