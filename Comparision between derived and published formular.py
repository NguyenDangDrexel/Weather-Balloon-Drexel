import matplotlib.pyplot as plt 
import math 
def creating_data (points,data_range): # input: points, range of data  => output: list of data points 
    data = [] 
    for i in range (data_range[0],data_range[1], int ((data_range[1]- data_range[0])/points)):
        data.append(i)
    return data 
# input: parameters of the function + value of altitude => output: pressure, function for 0 < h < 11000 and 25000 < h < 35000 
def derived_pressure1 (P_i, a,b,M,g0,R,height): 
    h = height
    P = P_i * ((a+b*h)/a) ** ( -(M*g0)/(R*b))
    return P

def derived_pressure3 (P_i, a,b,T2,M,g0,R,height): 
    h = height
    P = P_i * ((a+b*h)/T2) ** ( -(M*g0)/(R*b))
    return P 

def derived_pressure2 (P_i,M,g0,R,T2,height):
    P = P2 * math.exp(((-M*g0)/(R*T2))* (height-11000))
    return P 
    pass 


# Function of NASA https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html  
# 0 < h < 11000 
def NASA_pressure1 (height): 
    h = height 
    P = 101290 * ( (288.08 - 0.00649 *h) / 288.08) ** 5.256
    return P 
# 11000 < h <25000 
def NASA_pressure2(height): 
    P = 22650 * math.exp(1.73 - 0.000157*height)
    return P 
    pass
#25000 < h < 35000 
def NASA_pressure3(height): 
    P = 2480 * ((141.89+0.0029*height)/216.6) ** (-11.388)
    return P 
    pass

# Website of physical constants -  https://www.foehnwall.at/meteo/isa.html 

g0 = 9.80665 #(m/s^2)
R = 8.31423 # ( J/mol*K) universal constant 
M = 28.6944 * (0.001) # (g/mol) - molar mass of dried gas 

# from  0 <= h <= 11000:  T = a1 +b1h 
a1 = 288.04 # Kelvin 
b1 = -0.00649 # (1/m)
# from 11000 < h < 25000: T = 216.54 (K)
T2 = 216.54 
# from 25000 < h < 35000: T = a3 + b3h 
a3 = 141.79
b3 = 0.00299
P1 = 101325 # preesure at sea level 
P2 = derived_pressure1 (P_i= P1, a = a1, b = b1, M=M,g0 = g0, R= R, height =11000)
P3 = derived_pressure2 (P_i= P2, M = M, g0 = g0,R = R, T2 = T2, height = 25000)

# data for drawing graph 
points = 100
data_range1 = [0,11000]
data_range2 = [11000,25000]
data_range3 = [25000,35000]

pressure_derived1 = []
pressure_derived2 = []
pressure_derived3 = []

pressure_NASA1 = [] 
pressure_NASA2 = [] 
pressure_NASA3 = [] 

# data = list of altitude 
data1 = creating_data(points = points,data_range=data_range1)
data2 = creating_data(points = points,data_range=data_range2)
data3 = creating_data(points = points,data_range=data_range3)


# creating list of preesure, based on the derived function 
for i in range (points):
    pressure_derived1.append (derived_pressure1 (P_i= P1, a = a1, b = b1, M=M,g0 = g0, R= R, height = data1[i]))
for i in range (points):
    pressure_derived3.append (derived_pressure3 (P_i= P3, a = a3, b = b3, T2 = T2, M=M,g0 = g0, R= R, height = data3[i]))
for i in range (points):
    pressure_derived2.append (derived_pressure2 (P_i= P2, M = M, g0 = g0,R = R, T2 = T2, height = data2[i]))
# def derived_pressure2 (P_i,M,g0,R,T1,height):
# creating list of preesure, based on the NASA function 
for i in range (points):
    pressure_NASA1.append (NASA_pressure1 (height = data1[i]))
for i in range (points):
    pressure_NASA2.append (NASA_pressure2 (height = data2[i]))
for i in range (points):
    pressure_NASA3.append (NASA_pressure3 (height = data3[i]))

# drawing graph 
plt.plot (data1+data2+data3,pressure_derived1+pressure_derived2+pressure_derived3, color = 'red', label = 'derived function')

plt.scatter (data1+data2+data3,pressure_NASA1 +pressure_NASA2+pressure_NASA3,s = 5, label = 'NASA function')

#labelling + showing the graph
plt.title ('Derived function vs NASA curve-fitting function')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Pressure (Pa)')
plt.yticks(range(0, 100001,10000))
plt.legend ()
plt.show () 

