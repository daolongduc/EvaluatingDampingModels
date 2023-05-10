# -*- coding: utf-8 -*-
#==============================================================================
# This module includes functions for other files. It cannot be self executed.
#==============================================================================
from scipy.integrate import odeint
import numpy as np

# linear system
def fl(u,x,g,L,c_m):
    return (u[1],-c_m*u[1]-g/L*u[0])
def linear_system(g,L,c_m,theta0,thetadot0,t):
    sol = odeint(fl,[theta0,thetadot0],t,args=(g,L,c_m))
    return sol
# nonlinear system, linearly proportional damping
def f1(u,x,g,L,c_m):
    return (u[1],-c_m*u[1]-g/L*np.sin(u[0]))
def nonlinear_system_vel1(g,L,c_m,theta0,thetadot0,t):
    sol = odeint(f1,[theta0,thetadot0],t,args=(g,L,c_m))
    return sol
# nonlinear system, squared-vel proportional damping
def f2(u,x,g,L,cL_m):
    return (u[1],-cL_m*u[1]**2*np.sign(u[1])-g/L*np.sin(u[0]))
def nonlinear_system_vel2(g,L,cL_m,theta0,thetadot0,t):
    sol = odeint(f2,[theta0,thetadot0],t,args=(g,L,cL_m))
    return sol
# nonlinear system, quadratic damping
def fquad(u,x,g,L,c_m,cL_m):
    return (u[1],-c_m*u[1]-cL_m*u[1]**2*np.sign(u[1])-g/L*np.sin(u[0]))
def nonlinear_system_quad(g,L,c_m,cL_m,theta0,thetadot0,t):
    sol = odeint(fquad,[theta0,thetadot0],t,args=(g,L,c_m,cL_m))
    return sol
# find peaks
def peaks(res):
    dis, vel = res[:,0],res[:,1]
    D = np.empty(0)
    for iChay in range(vel.shape[0]-1):
        if (vel[iChay]*vel[iChay+1] <= 0.0) and (dis[iChay]*dis[0] > 0):
            if np.abs(dis[iChay]) > np.abs(dis[iChay+1]):
                D = np.append(D, dis[iChay])
            else:
                D = np.append(D, dis[iChay+1])
    return D
# find times at peaks
def tpeaks(res,dt):
    dis, vel = res[:,0],res[:,1]
    Tp = np.empty(0)
    for iChay in range(vel.shape[0]-1):
        if (vel[iChay]*vel[iChay+1] <= 0.0) and (dis[iChay]*dis[0] > 0):
            if np.abs(dis[iChay]) > np.abs(dis[iChay+1]):
                Tp = np.append(Tp, iChay*dt)
            else:
                Tp = np.append(Tp, (iChay+1)*dt)
    return Tp