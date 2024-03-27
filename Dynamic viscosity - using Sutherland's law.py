import matplotlib.pyplot as plt 
import math 
def creating_data (points,data_range): # input: points, range of data  => output: list of data points 
    data = [] 
    a = data_range[0]
    for i in range (points): 
        data.append (a)
        a += (data_range[1]- data_range[0])/points
    return data 
def viscosity1 (h): 
    viscosity = 1.77 * 10 ** (-5) * ((288.04-0.00649*h)/(288.04))** (1.5) * ((394.44-0.00649*h)/(398.44))
    return viscosity
def viscosity2 (h): 
    viscosity = 1.77 * 10 ** (-5) * ((216.54)/(288.04))** (1.5) * ((326.94)/(398.44))
    return viscosity
def viscosity3 (h): 
    viscosity = 1.77 * 10 ** (-5) * ((141.79+0.00299 *h)/(288.04))** (1.5) * ((252.19 + 0.00299 *h)/(398.44))
    return viscosity


# Website of physical constants -  https://www.foehnwall.at/meteo/isa.html 


# data for drawing graph 
points = 30  
data_range1 = [0,11000]
data_range2 = [11000,25000]
data_range3 = [25000,35000]



# data = list of altitude 
data1 = creating_data(points = points,data_range=data_range1)
data2 = creating_data(points = points,data_range=data_range2)
data3 = creating_data(points = points,data_range=data_range3)

data_Viscosity1 =  [] 
data_Viscosity2 =  [] 
data_Viscosity3 =  [] 



# creating list of density, based on the derived function 



# def derived_pressure2 (P_i,M,g0,R,T1,height):
# creating list of preesure, based on the NASA function 

# drawing graph 
for i in range (points):
    data_Viscosity1.append (viscosity1(data1[i]))
    data_Viscosity2.append (viscosity2(data2[i]))
    data_Viscosity3.append (viscosity3(data3[i]))
# R  = R_0 * V ^ (1/3) 
data_altitude = data1 + data2 + data3 
data_viscosity  = data_Viscosity1 + data_Viscosity2 + data_Viscosity3 

plt.plot (data_altitude,data_viscosity)

plt.legend ()
plt.show () 
