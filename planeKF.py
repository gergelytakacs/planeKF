# Gergely Takacs, 2022
#
# Python realization of the KF example explained
# by Michel van Biezen in his lecture series on 
# the Kalman filter. See https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT
# for the full lecture series. The example starts at Lecture 27, i.e.
# https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT
#
# WARNING: Do not implement the Pp=diag(diag(Pp)) line outside
# this educational example. This is only to make the hand calculation
# demonstrated easier.

import numpy as np
import matplotlib.pyplot as plt

# Given (initial conditions)
a=2         # (m/s^2) Acceleration (constant)
T=1         # (s) Sampling time
x0 = 4000   # (m) Position init. cond.
v0 = 280    # (m/s) Velocity init. cond.
x=np.array([[x0],[v0]])   # Estimated state vector (to store results)
Xp=x;       # Initialization just for storing predictions later

# Observations (measurements)
xo = np.array([4000, 4260, 4550, 4860, 5110]) # (m) Position observation
vo = np.array([280,  282,  285,  286,  290])  # (m/s) Velocity observation
xo = np.stack((xo, vo))              # Observed states

# Initial state error covariance matrix
dPx = 20                  # (m) Variance guess in position
dPy = 5                   # (m/s) Variance giess in velocity
P= np.diag([dPx**2,dPy**2])  # Initial estimate for state error covariance matrix

# Process noise
Q=np.zeros([2,2]) # No process noise assumed

#Observation errors
dx = 25 # (m)   Error in position measurement
dy = 6  # (m/s) Error in velocity measurement
R=np.diag([dx**2, dy**2]) # Process noise covariance matrix

# State-space formulation
A=np.array([[1., T], [0., 1.]])    # State transition matrix
B=np.array([[1/2*T**2], [T]]) # Input matrix
C=np.eye(2);             # Measurement matrix
H=np.eye(2);             # Measurement to state transformatio 

##Filter in action
run=4

for i in range(run):

    print('Iteration:',i+1)
    # Prediction part (p)
    xp=A.dot(x[:,i:i+1])+B.dot(a) # Predict state
    print('xp=')
    print(xp)
    Pp=A.dot(P.dot(A.T))+Q     # Predict state covariance
    # SIMPLIFICATION FOR HAND CALCULATION, DO NOT USE IN REAL ALGORITHM
    Pp=np.diag(np.diag(Pp))    # Comment out! Leaves out off-diagonals
    print('Pp=')
    print(Pp)

    # Update part
    K=np.dot((Pp.dot(H.T)),np.linalg.inv(H.dot(Pp.dot(H.T))+R)) # Kalman gain
    print('K=')
    print(K)
    y=C.dot(xo[:,i+1:i+2])             # New observation
    x = np.append(x, xp+K.dot((y-H.dot(xp))),axis=1)            # Updated state (current state)
    print('x')
    print(x[:,i+1:i+2])
    P=np.dot(np.eye(2)-(K.dot(H)),Pp)   # Uptated state covariance
    print('P')
    print(P)

  
    print('Close both figures to proceed...')
    Xp=np.append(Xp,xp,axis=1) # Just store predictions for plotting
    plt.figure(1)
    plt.plot(xo[0,0:i+2],"o-", label='Observation')
    plt.plot(Xp[0,0:i+2],"x-", label='Prediction')
    plt.plot(x[0,:],"^-", label='KF')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend(['Observation', 'Prediction','KF'])
    plt.show()
   

    plt.figure(2)
    plt.plot(xo[1,0:i+2],"o-", label='Observation')
    plt.plot(Xp[1,0:i+2],"x-", label='Prediction')
    plt.plot(x[1,:],"^-", label='KF')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend(['Observation', 'Prediction','KF'])
    plt.show()
