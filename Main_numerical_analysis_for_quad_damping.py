# -*- coding: utf-8 -*-
#===========================
# DIFFERENTIAL EQUATION
# (theta\ddot) + (cq1+cq2*abs(theta\dot))*(theta\dot) + g/L sin(theta) = 0
# subjected to (theta0, theta0dot)
#===========================
import numpy as np
import FreeVibrationModule as fb

g = 9.79 # gravitational acceleration (m/s^2)
L = 1.085 # effective length (m)
nCycles = 50 # number of cycles to analyze
cq1 = 0.01310 # normalized damping coefficient (1/s)
cq2 = 0.04170 # normalized damping coefficient
theta0 = 1.1973 # intial angle (rad)
theta0dot = 0.0 # inital angular velocity (rad/s)
#---------------------------
Tn = 2*np.pi*(L/g)**0.5
t = np.linspace(0,nCycles*Tn,1000*nCycles)
res = fb.nonlinear_system_quad(g, L, cq1, cq2, theta0, theta0dot, t)
D = fb.peaks(res)
Tp = fb.tpeaks(res,t[1])
import matplotlib.pyplot as plt
plt.plot(t,res[:,0],label='Time history')
plt.plot(Tp,D,label='Envelope')
plt.legend()
plt.show()
