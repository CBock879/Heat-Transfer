# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:51:31 2018

@author: Chris
"""

import numpy as np
import matplotlib.pyplot as pyp


xsize = 20
ysize = 50


#mesh
temperature = np.ones([xsize])
conductivity = np.full([xsize],0.02)
specific_heat = np.ones([xsize])

temperature[int(xsize/2)] = 1.1
           
time_steps = 100000

dt = 0.001

#law of heat transfer
r = lambda dT,dx,k: (-k) * (dT/dx)

for t in range(0,time_steps):
    temp_0 = temperature
    for i in range(0,xsize):
        if (i > 0):
            delta_T = temp_0[i]-temp_0[i-1]
            delta_x = 1
            k = (conductivity[i]+conductivity[i-1])/2
            
            q = r(delta_T,delta_x,k)
            
            temperature[i] += dt*q*specific_heat[i]
                       
        if (i < xsize-1):
            delta_T = temp_0[i]-temp_0[i+1]
            delta_x = 1
            k = (conductivity[i]+conductivity[i+1])/2
            
            q = r(delta_T,delta_x,k)
            
            temperature[i] += dt*q*specific_heat[i]

pyp.plot(temperature)
