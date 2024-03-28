# Reference to this model https://www.youtube.com/watch?v=k46nCvOBllA&t=1559s
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# PID parameters 
ubias =  0
Kp = 5
Ki = 0.1
Kd = 3
# animate plots?
animate=False # True / False

# define model
def vehicle(v,t,u,load):
    # inputs
    #  v    = vehicle velocity (m/s)
    #  t    = time (sec)
    #  u    = gas pedal position (-50% to 100%)
    #  load = passenger load + cargo (kg)
    Cd = 0.005    # drag coefficient
    rho = 1.225  # air density (kg/m^3)
    A = 5.0      # cross-sectional area (m^2)
    Fp = 20      # thrust parameter (N/%pedal)
    m = 500      # vehicle mass (kg)
    # calculate derivative of the velocity
    dv_dt = (1.0/(m+load)) * (Fp*u - 0.5*rho*Cd*A*v**2)
    return dv_dt

tf = 300                 # final time for simulation
nsteps = 10000             # number of time steps
delta_t = tf/(nsteps-1)   # how long is each time step?
ts = np.linspace(0,tf,nsteps) # linearly spaced time vector

# simulate step test operation
step = np.zeros(nsteps) # u = valve % open
# step[11:] = 15      # step up pedal position
# passenger(s) + cargo load
load = 200.0 # kg
# velocity initial condition
v0 = 0.0
# set point
sp = 25.0
# for storing the results
vs = np.zeros(nsteps)
sps = np.zeros(nsteps)

sum_int = 0
es = np.zeros (nsteps)
ies = np.zeros (nsteps)
sp_store = np.zeros (nsteps)

plt.figure(1,figsize=(5,4))
if animate:
    plt.ion()
    plt.show()

# simulate with ODEINT 
# in this model, we can use odeint, integrate directly from 0 to 60 (s) to get the result of velocity. However, we just integrate each interval so that we can implement witht the PID system. 
for i in range(nsteps-1):
    error = sp - v0 
    sum_int += error * delta_t
    if i == 0: 
        u = ubias + Kp*error +Ki *sum_int 
    else:
        u = ubias + Kp*error +Ki *sum_int + Kd*((v[-1]-v[0])/delta_t)
    # clip inputs to -50% to 100%
    if u >= 100.0:
        u = 100.0
        sum_int = sum_int - error * delta_t #windup 

    if u <= -50.0:
        u = -50.0
        sum_int = sum_int - error*delta_t #antiwindup
    # schedule change in set point: to simulate that we change the setpoint 
    # if i == 50:
    #     sp = 0 
    # if i == 100: 
    #     sp = 15 
    # if i == 150:
    #     sp = 20 
    # if i == 200:
    #     sp = 10 
    es [i+1] = error 

    v = odeint(vehicle,v0,[0,delta_t],args=(u,load))
    v0 = v[-1]   # take the last value
    vs[i+1] = v0 # store the velocity for plotting
    sps[i+1] = sp # store the setpoint for plotting => not important 

    step[i+1] = u


    # plot results
    if animate:
        plt.clf()
        plt.subplot(2,1,1)
        plt.plot(ts[0:i+1],vs[0:i+1],'b-',linewidth=3)
        plt.plot(ts[0:i+1],sps[0:i+1],'k--',linewidth=2)
        plt.ylabel('Velocity (m/s)')
        plt.legend(['Velocity','Set Point'],loc=2)
        plt.subplot(2,1,2)
        plt.plot(ts[0:i+1],step[0:i+1],'r--',linewidth=3)
        plt.ylabel('Gas Pedal')    
        plt.legend(['Gas Pedal (%)'])
        plt.xlabel('Time (sec)')
        plt.pause(0.00001)    

if not animate:
    # plot results
    plt.subplot(2,1,1)
    plt.plot(ts,vs,'b-',linewidth=3)
    plt.plot(ts,sps,'k--',linewidth=2)
    plt.ylabel('Velocity (m/s)')
    plt.legend(['Velocity','Set Point'],loc=2)
    plt.subplot(2,1,2)
    plt.plot(ts,step,'r--',linewidth=3)
    plt.ylabel('Gas Pedal')    
    plt.legend(['Gas Pedal (%)'])
    plt.xlabel('Time (sec)')
    plt.show()
