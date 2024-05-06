# New discover: plt.plot (np.linspace(0,11000,100),derived_pressure1(np.linspace(0,11000,100))) works well 
# This program is written as module to ensure that we can reuse and modify the program easier 
import math 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 
# I. Pressure function

g0 = 9.80665 #(m/s^2)
R = 8314.13# ( J/mol*K) universal constant 
M = 28.6944  # (g/mol) - molar mass of dried gas 
mu_0 = 1.77 * 10 ** (-5) # Dynamic density (Pa-s)
#constant of adiabatic process 
gamma = 1.4 
# from  0 <= h <= 11000:  T = a1 +b1h 
a1 = 288.04 # Kelvin 
b1 = -0.00649 # (1/m)
# from 11000 < h < 25000: T = 216.54 (K)
a2 = 216.54 
b2 = 0 
# from 25000 < h < 35000: T = a3 + b3h 
a3 = 141.79
b3 = 0.00299
P0 = 101325 # preesure at sea level 

# The range of altitude 
H0 = 0 
H1 = 11000 
H2 = 25000
H3 = 35000  
# Defining the function of Temperature 
def Temperature (h,H0 = H0, H1 = H1, H2 = H2, H3=H3, a1=a1,b1=b1,a2 = a2,b2 = b2,a3=a3,b3=b3):
    if 0 <= h <= 11000: 
        T = a1 +b1*h
    if 11000 < h <= 25000: 
        T = a2 +b2*h
    if 25000 < h <= 35000: 
        T = a3 +b3*h

    return T
# Defining the function pressure 
def Pressure(h,P0 = P0, a=a1,b=b1,M=M,g0=g0,R=R):
    if 0 <= h <= 11000: 
        P =P0 * ((a1+b1*h)/a1) ** ( -(M*g0)/(R*b1))
    if 11000 < h <= 25000:
        P = Pressure (11000) * np.exp(((-M*g0)/(R*a2))* (h-11000))
    if 25000 < h <= 35000: 
        P = Pressure (25000) * ((a3+b3*h)/a2) ** ( -(M*g0)/(R*b3))
   
    return P 
# Defining the function of density 
def Density (h): 
    rho = ((Pressure(h))*(M))/ ((R)*(Temperature(h)))
    return rho 

# Defining the function for viscosity by using Sutherland's equation 

def Viscosity (h,mu_0 = mu_0,T0=a1): 
    v = mu_0 * ((Temperature(h))/(T0)) ** (1.5) * ((Temperature(h)+110.4)/(T0 + 110.4))
    return v 

#Input: the initial value of volume 
def Volume_constant (V0): 
    V = V0 
    return V 
#Input: the volume of the balloon 
def Area_constant (V0):
    A =np.pi * ((3/4) * (Volume_constant(V0)/np.pi))**(2/3)
    return A 
def Radius_constant (V0):
    R = (3/4 * Volume_constant (V0) / np.pi) ** (1/3)
    return R 
# Radius function calculated from the Volume equation 
#Isothermal model (T_in = constant), Input: heigh, initial volume
def Volume_isothermal (h,P0= P0, V0=1,T0=a1):
    V = V0 * ((P0)/(Pressure(h)))
    return V 
def Radius_isothermal (h,V0 = 1): 
    R = Volume_isothermal(h,V0=1) ** (1/3)
    return R 
def Area_isothermal (h,V0):
    A =np.pi * ((3/4) * (Volume_isothermal(h,V0 =V0)/np.pi))**(2/3)
    return A 
def Volume_adiabatic (h,P0=P0,V0=1):
    V = (P0/Pressure(h)) ** (1/gamma)* V0
    return V 
def Area_adiabatic (h,V0):
    A =np.pi * ((3/4) * (Volume_adiabatic(h,V0 =V0)/np.pi))**(2/3)
    return A 
def Radius_adiabatic (h,V0 = 1): 
    R = Volume_adiabatic(h,V0=1) ** (1/3)
    return R 
# this equation is taken from Henrique Yago paper 
def Volume_data (h, rf,constant, ri =Radius_constant(V0=1)):
    V = 4/3 * np.pi * (constant + (ri - rf)/(Pressure(0) - Pressure(25000)) * Pressure(h)) ** (3)
    return V 

def Volume_out (h,P0=P0,V0=1,T0=a1):
    V = V0 * ( (P0)/(Pressure(h)) ) * ( (Temperature(h))/(T0) )
    return V 
def Area_out (h,V0):
    A =np.pi * ((3/4) * (Volume_out(h,V0 =V0)/np.pi))**(2/3)
    return A 
def Radius_out (h,V0 = 1): 
    R = Volume_out (h,V0=1) ** (1/3)
    return R 