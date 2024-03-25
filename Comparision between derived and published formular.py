def creating_data (points,data_range): # input: points, range of data  #output: list of data points 
    data = [] 
    for i in range (0,data_range, int (data_range/points)):
        data.append(i)
    return data 

def derived_pressure (P0, a,b,M,g0,R,height): 
    h = height
    P = P0 * ((a+b*h)/a) ** ( -(M*g0)/(R*b))
    return P
def NASA_pressure (height): 
    h = height 
    P = 101290 * ( (288.08 - 0.00649 *h) / 288.08) ** 5.256
    return P 
# https://www.foehnwall.at/meteo/isa.html 
P0 = 101325 #pascal 
g0 = 9.80665 #(m/s^2)
R = 8.31423 # ( J/mol*K) universal constant 
M = 28.6944 * (0.001) # (g/mol) - molar mass of dried gas 
# https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html 
# from  0 <= h <= 11000 
a = 288.04 # Kelvin 
b = -0.00649 # (1/m)


points = 100
data_range = 11000

pressure_derived = []
pressure_NASA = [] 
data = creating_data(points = points,data_range=data_range)
for i in range (points):
    pressure_derived.append (derived_pressure (P0= P0, a = a, b = b, M=M,g0 = g0, R= R, height = data[i]))

import matplotlib.pyplot as plt 
#plt.scatter ( data,pressure_derived, s = 1 )
plt.plot (data,pressure_derived, color = 'red', label = 'derived function')

for i in range (points):
    pressure_NASA.append (NASA_pressure (height = data[i]))
#plt.plot (data, pressure_NASA)
plt.scatter (data,pressure_NASA,s = 5, label = 'NASA function')
plt.title ('Derived function vs NASA curve-fitting function')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Pressure (Pa)')
plt.yticks(range(0, 100001, 10000))
plt.legend ()
plt.show () 
