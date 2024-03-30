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
mu_0 = 1.77 * 10 ** (-5) 
# from 11000 < h < 25000: T = 216.54 (K)
T2 = 216.54 
# from 25000 < h < 35000: T = a3 + b3h 
a3 = 141.79
b3 = 0.00299
P1 = 101325 # preesure at sea level 
# from  0 <= h <= 11000:  T = a1 +b1h 
a1 = 288.04 # Kelvin 
b1 = -0.00649 # (1/m)
def Temperature1 (h,a1=a1,b1=b1):

    T = a1 +b1*h

    return T 
def Temperature2 (*h,T2=T2): 

    T2 = T2 
    
    return T2
def Temperature3(h,a3=a3,b3=b3):

    T = a3+b3*h
    
    return T 

def derived_pressure1 (h, P_i = P1, a=a1,b=b1,M=M,g0=g0,R=R): 

    P = P_i * ((a+b*h)/a) ** ( -(M*g0)/(R*b))

    return P
    
#preesure at h =11000 
P2 = derived_pressure1 (h =11000)

def derived_pressure2 (h, P_i = P2,M = M,g0=g0,R=R,T2 =T2):
   
    P = P_i * np.exp(((-M*g0)/(R*T2))* (h-11000))
    
    return P
#pressure at h = 25000
P3 = derived_pressure2 (h= 25000)

def derived_pressure3 (h, P_i = P3, a=a3,b=b3,T2=T2,M=M,g0=g0,R=R):
    
    P = P_i * ((a+b*h)/T2) ** ( -(M*g0)/(R*b))
   
    return P 

# defining density functions for three stages 
def density1 (h,M = M): 
    rho = ((derived_pressure1(h))*(M))/ ((R)*(Temperature1(h)))
    return rho 
def density2(h,M=M):
    rho = ((derived_pressure2(h))*(M))/ ((R)*(Temperature2(h)))
    return rho 
def density3(h,M=M):
    rho = ((derived_pressure3(h))*(M))/ ((R)*(Temperature3(h)))
    return rho 

# defining dynamic viscosity functions
def vis1 (h,mu_0 = mu_0,T0=a1): 
    v = mu_0 * ((Temperature1(h))/(T0)) ** (1.5) * ((Temperature1(h)+110.4)/(T0 + 110.4))
    return v 
def vis2 (h,mu_0 = mu_0,T0=a1):
    v = mu_0 * ((Temperature2(h))/(T0)) ** (1.5) * ((Temperature2(h)+110.4)/(T0 + 110.4))
    return v
def vis3 (h,mu_0 = mu_0,T0=a1): 
    v = mu_0 * ((Temperature3(h))/(T0)) ** (1.5) * ((Temperature3(h)+110.4)/(T0 + 110.4))
    return v 

def Volume1 (h,P1= P1, V0=1,T0=a1): # remember to give initial volume when use this function 
    V = ((P1*V0)/(T0)) * ((Temperature1(h))/(derived_pressure1(h)))
    return V 
def Volume2(h,P1=P1,V0=1,T0=a1): 
    V = ((P1*V0)/(T0)) * ((Temperature2(h))/(derived_pressure2(h)))
    return V 
def Volume3(h,P1=P1,V0=1,T0=a1): 
    V = ((P1*V0)/(T0)) * ((Temperature3(h))/(derived_pressure3(h)))
    return V
# Radius functions 
def Radius1 (h): 
    R = Volume1 (h) ** (1/3)
    return R 
def Radius2 (h): 
    R = Volume2 (h) ** (1/3)
    return R 
def Radius3 (h): 
    R = Volume3 (h) ** (1/3)
    return R 


