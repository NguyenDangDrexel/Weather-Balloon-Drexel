# density3 (): fail, density 1,2: OK 
import matplotlib.pyplot as plt 
import math 
def creating_data (points,data_range): # input: points, range of data  => output: list of data points 
    data = [] 
    a = data_range[0]
    for i in range (points): 
        data.append (a)
        a += (data_range[1]- data_range[0])/points
    return data 
# input: parameters of the function + value of altitude => output: pressure, function for 0 < h < 11000 and 25000 < h < 35000 
def derived_pressure1 (P_i, a1,b1,M,g0,R,height): 
    h = height
    P = P_i * ((a1+b1*h)/a1) ** ( -(M*g0)/(R*b1))
    return P
def derived_pressure2 (P_i,M,g0,R,T2,height):
    P = P2 * math.exp(((-M*g0)/(R*T2))* (height-11000))
    return P 
    pass 
def derived_pressure3 (P_i, a3,b3,T2,M,g0,R,height): 
    h = height
    P = P_i * ((a3+b3*h)/T2) ** ( -(M*g0)/(R*b3))
    return P 


def density1(P_i, a1,b1,M,g0,R,height):
    d = (derived_pressure1(P_i, a1,b1,M,g0,R,height)* M)/ (R* (a1+b1*height))
    return d 

    pass 
def density2 (P_i,M,g0,R,T2,height):
    d = (derived_pressure2(P_i,M,g0,R,T2,height)* M)/ (R* T2)
    return d
    pass 
def density3 (P_i, a3,b3,T2,M,g0,R,height):
    d = (derived_pressure3(P_i, a3,b3,T2,M,g0,R,height)*M)/(R*(a3+b3*height))
    return d 


# Website of physical constants -  https://www.foehnwall.at/meteo/isa.html 

g0 = 9.80665 #(m/s^2)
R = 8314.23 # ( J/mol*K) universal constant 
M = 28.6944  # (g/mol) - molar mass of dried gas 

# from  0 <= h <= 11000:  T = a1 +b1h 
a1 = 288.04 # Kelvin 
b1 = -0.00649 # (1/m)
# from 11000 < h < 25000: T = 216.54 (K)
T2 = 216.54 
# from 25000 < h < 35000: T = a3 + b3h 
a3 = 141.79
b3 = 0.00299
P1 = 101325 # preesure at sea level 
P2 = derived_pressure1 (P_i= P1, a1 = a1, b1 = b1, M=M,g0 = g0, R= R, height =11000)
P3 = derived_pressure2 (P_i= P2, M = M, g0 = g0,R = R, T2 = T2, height = 25000)

# data for drawing graph 
points = 30  
data_range1 = [0,11000]
data_range2 = [11000,25000]
data_range3 = [25000,35000]

data_density1 = [] 
data_density2 = [] 
data_density3 = [] 

# data = list of altitude 
data1 = creating_data(points = points,data_range=data_range1)
data2 = creating_data(points = points,data_range=data_range2)
data3 = creating_data(points = points,data_range=data_range3)


# creating list of density, based on the derived function 



# def derived_pressure2 (P_i,M,g0,R,T1,height):
# creating list of preesure, based on the NASA function 

# drawing graph 
for i in range (points): 
    data_density1.append (density1(P_i = P1, a1 = a1,b1 = b1,M = M,g0 = g0,R = R,height = data1[i]))
    data_density2.append (density2 (P_i = P2,M = M,g0 = g0,T2 = T2,R= R,height = data2[i]))
    data_density3.append (density3 (P_i = P3, a3 = a3,b3= b3,T2= T2,M=M,g0=g0,R =R,height = data3[i]))
plt.plot (data1+data2+data3,data_density1+data_density2+data_density3)
print ()
#labelling + showing the graph
plt.title ('Derived function vs NASA curve-fitting function')
plt.xlabel ('Altitude (m)')
plt.ylabel ('Density kg/m^3')
plt.legend ()
plt.show () 

