import matplotlib.pyplot as plt 
import math 
def creating_data (points,data_range): # input: points, range of data  => output: list of data points 
    data = [] 
    a = data_range[0]
    for i in range (points): 
        data.append (a)
        a += (data_range[1]- data_range[0])/points
    return data 
def Volume1 (h): 
    V = 2.934 * 10 ** 10 * (((288.04-0.00649*h)**(-4.256)))
    return V 
def Volume2(h):
    V = 351.77 * ((216.54)/(22650 * math.exp(1.73-0.000157*h)))
    return V 
def Volume3 (h): 
    V = 2.882 * 10 ** (-28) * (141.79 + 0.00299 *h) **(12.426)
    return V 


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

data_Volume1 =  [] 
data_Volume2 =  [] 
data_Volume3 =  [] 

data_radius1 = [] 
data_radius2 = [] 
data_radius3 = [] 


# creating list of density, based on the derived function 



# def derived_pressure2 (P_i,M,g0,R,T1,height):
# creating list of preesure, based on the NASA function 

# drawing graph 
for i in range (points):
    data_Volume1.append (Volume1(data1[i]))
    data_Volume2.append (Volume2(data2[i]))
    data_Volume3.append (Volume3(data3[i]))
# R  = R_0 * V ^ (1/3) 
for i in range (points):
    data_radius1.append ((Volume1(data1[i]))** (1/3))
    data_radius2.append ((Volume2(data2[i]))** (1/3))
    data_radius3.append ((Volume3(data3[i]))** (1/3)) 
data_altitude = data1 + data2 + data3 
data_volume  = data_Volume1 + data_Volume2 + data_Volume3 
data_radius = data_radius1 + data_radius2 + data_radius3 

fig,axes = plt.subplots (2,1)
axes[0].plot (data_altitude, data_volume)
axes[0].set_title ('Volume')
axes[0].set_yticks (range (0,161,20))
axes[0].grid (True)
axes[1].plot (data_altitude,data_radius)
axes[1].set_title ('Radius')
axes[1].grid (True)

plt.tight_layout
plt.legend ()
plt.show () 

""" 
fig, axes = plt.subplots(2,1, figsize=(10, 5))

# Plot the first graph
axes[0].plot(x1, y1, color='blue')
axes[0].set_title('Sine Function')

# Plot the second graph
axes[1].plot(x2, y2, color='red')
axes[1].set_title('Cosine Function')

# Adjust layout
plt.tight_layout()
 """