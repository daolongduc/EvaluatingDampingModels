# -*- coding: utf-8 -*-
#==============================================================================
# This code is for finding the damping coefficients of different damping models
# that best fit the test data
#==============================================================================
import numpy as np
import FreeVibrationModule as fb
from scipy import optimize
#==============================================================================
# INPUTS
g = 9.79 # gravitational acceleration
L = 1.085 # effective length
nCycles = 80 # number of cycles to analyze
nPeak = np.array([0,1,2,3,4,5,6,7,12,17,22,27,32,37,47,67]) # the peak numbers where the peak displacement were recorded
weights = np.array([0,1,1,1,1,1,1,1,5,5,5,5,5,5,10,20]) # weights to the square errors of the peak displacement
ExpDatFile = 'exp_data.dat' # experimental data file
#==============================================================================
# PROCESSING
Tn = 2*np.pi*(L/g)**0.5 # natural period of the system
t = np.linspace(0,nCycles*Tn,1000*nCycles) # time series
exp_dat = np.loadtxt(ExpDatFile,delimiter = '\t')

def error_vel1(c1):
    theta0 = exp_peaks[0]
    res = fb.nonlinear_system_vel1(g, L, c1, theta0, 0.0, t)
    D = fb.peaks(res)
    sqerr = np.sum(np.square(exp_peaks-D[nPeak])*weights)
    return sqerr
def error_vel2(c2):
    theta0 = exp_peaks[0]
    res = fb.nonlinear_system_vel2(g, L, c2, theta0, 0.0, t)
    D = fb.peaks(res)
    sqerr = np.sum(np.square(exp_peaks-D[nPeak])*weights)
    return sqerr
def error_quad(c1c2):
    c1, c2 = c1c2
    theta0 = exp_peaks[0]
    res = fb.nonlinear_system_quad(g, L, c1, c2, theta0, 0.0, t)
    D = fb.peaks(res)
    sqerr = np.sum(np.square(exp_peaks-D[nPeak])*weights)
    return sqerr
print('======================================')
print('Note: the fitted coefficients may be slightly different from different runs.')
for iTest in range(exp_dat.shape[0]):
    exp_peaks = exp_dat[iTest,:]
    print('======================================')
    print('Fitted coefficients for trial ' + str(iTest + 1) + ':')
    res1 = optimize.differential_evolution(error_vel1, [(0.03,0.15)])
    print('+ Linear model, c1 = ' + str(res1.x[0]))
    res2 = optimize.differential_evolution(error_vel2, [(0.03,0.15)])
    print('+ Squared velocity proportional model, c2 = ' + str(res2.x[0]))
    res_quad = optimize.differential_evolution(error_quad, bounds = [(0.008,0.015),(0.03,0.05)])
    print('+ Complete quadratic model, [cq1, cq2] = ' + str(res_quad.x))