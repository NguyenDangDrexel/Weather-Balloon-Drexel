import numpy as np
import matplotlib.pyplot as plt 
import math 
from Model import * 
""" 
This program is done 
This program can: 
    Solve the terminal_velocity at steady-state vs altitude for 4 cases 
        We can change the case by changing parameter case 
    Based on this terminal velocity to plot Re vs altitude 
        Can change this function

Does not affect by the m_virtual as acceleration = 0 
"""

# As I use the data of this file for drawing the graph in DynamicModel. Therefore, the plotting mode is set to be False by default  
plotting = False     
# case 1: constant volume; case 2: isothermal volume; case 3: adiabatic; case 4: T_in = T_out 
case = 2
# Plot 1: only teminal velocity, plot 2: Re, terminal velocity 
plot = 2 
m = 7 # total mass of the balloon: helium + latex + payload  (kg) 
Cd = 0.44 # constant drag coefficient 
g = 9.8 # gravitational accerleration (m/s^2) 
V0 = 15.05 # initial volume of the balloon 
H1 = 0
H2 = 35000 
data_points = 10000
#Area of the balloon 
# This function describe the terminal velocity with altitude for constant volume, input: inital volume, h 
def terminal_velocity (h, V0 = V0 ): 
    if case == 1: 
        V = Volume_constant (V0) 
        A = Area_constant(V0)
    elif case == 2: 
        V = Volume_isothermal(h,V0=V0) 
        A = Area_isothermal(h,V0)
    elif case == 3: 
        V = Volume_adiabatic (h,V0=V0)
        A = Area_adiabatic (h,V0=V0)
    elif case  == 4: 
        V = Volume_out (h,V0=V0)
        A = Area_out (h,V0=V0)

    if (Density(h)*V)/(m) - 1 >0: 
        v = ( ((2*m) / (Cd*A*Density (h))) * g *( (Density(h)*V)/(m) - 1 ) ) ** (1/2)
    else: 
        v = -( ((2*m) / (Cd*A*Density (h))) * g *( 1 - (Density(h)*V)/(m)) ) ** (1/2)
        
    return v 

def Re (h): 
    Re = Density(h) * terminal_velocity (h) * (2 * Radius_constant (V0))/ Viscosity(h) 
    return Re 

Re_data = [] 
Altitude_data = [] 
terminal_velocity_data = [] 
h = H1 

#creating data for plotting 
while h < H2: 
    Re_data.append (Re(h))
    Altitude_data.append (h)
    terminal_velocity_data.append (terminal_velocity(h))
    h += (H2-H1)/data_points 

if plotting == True: 
    #creating yticks 
    yticks = [] 
    ytickstext = [] 
    v_max = round (max(terminal_velocity_data))
    v_min = round (min (terminal_velocity_data))
    if v_max %2 ==0: 
        v_max = v_max 
    elif v_max %2 ==1: 
        v_max = v_max + 1 

    if v_min <0: 
        if v_min %2 == 0:  
            v_min = v_min  
        elif abs (v_min) %2 == 1 : 
            v_min = v_min -1
    else: v_min = 0 
    
    for i in range (v_min,v_max,2): 
        yticks.append (i)
        ytickstext.append (str (i))
    yticks.append (terminal_velocity_data[0])
    ytickstext.append (f'v0 = {terminal_velocity_data[0]:.2f}')

    # plot of terminal velocity vs altitude 
    if plot == 1:
        plt.plot(Altitude_data, terminal_velocity_data, color='blue')
        plt.title('terminal velocity vs altitude')
        plt.xlabel('h(m)')
        plt.ylabel('v0(m/s)')
        plt.yticks (yticks,ytickstext)
        plt.grid(True)
        plt.show ()
        
    # plot of Re vs altitude 
    elif plot ==2: 

        fig, axes = plt.subplots(1, 2, figsize=(8, 6))
        # labeling the whole graoh 
        fig.suptitle ('Analytical solution and odeint ()')

        #first plot     
        axes[0].plot(Altitude_data, Re_data, color='blue')
        axes[0].set_title('Reynold number vs altitude ') 
        axes[0].set_xlabel ('h (m) ')
        axes[0].set_ylabel ('Re')
        axes[0].grid(True)  
        #second plot 
        axes[1].plot(Altitude_data, terminal_velocity_data, color='blue')
        axes[1].set_title('Terminal velocity vs altitude ') 
        axes[1].set_xlabel ('h(m)')
        axes[1].set_ylabel ('v(m/s)')
        axes[1].grid(True)  

        plt.tight_layout()

        # Show the plot
        plt.show()

