# -*- coding: utf-8 -*-
#===========================
# DIFFERENTIAL EQUATION
# (theta\ddot) + c2*abs(theta\dot)*(theta\dot) + g/L sin(theta) = 0
# subjected to (theta0, theta0dot)
#===========================
import numpy as np
import FreeVibrationModule as fb

g = 9.79 # gravitational acceleration (m/s^2)
L = 1.085 # effective length (m)
nCycles = 50 # number of cycles to analyze
c2 = 0.05449 # normalized damping coefficient
theta0 = 1.1973 # intial angle (rad)
theta0dot = 0.0 # inital angular velocity (rad/s)
#---------------------------
Tn = 2*np.pi*(L/g)**0.5
t = np.linspace(0,nCycles*Tn,1000*nCycles)
res = fb.nonlinear_system_vel2(g, L, c2, theta0, theta0dot, t)
D = fb.peaks(res)
Tp = fb.tpeaks(res,t[1])
import matplotlib.pyplot as plt
plt.plot(t,res[:,0],label='Time history')
plt.plot(Tp,D,label='Envelope')
plt.legend()
plt.show()
