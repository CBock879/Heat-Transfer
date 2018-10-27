# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:51:31 2018

@author: Chris
"""

import numpy as np
import matplotlib.pyplot as pyp


xsize = 30
ysize = 30 


#mesh
temperature = np.zeros([xsize,ysize])
conductivity = np.full([xsize,ysize],0.01)
specific_heat = np.ones([xsize,ysize])



conductivity[13][:] =  0.96

temperature[int(xsize/2),int(ysize/2)] = 1.1
           
            
            
time_steps = 300
dt = 0.05

#law of heat transfer
r = lambda dT,dx,k: (-k) * (dT/dx)

for t in range(0,time_steps):
    temp_0 = temperature
    for i in range(0,xsize):
        for j in range(0,ysize):
            if (i > 0):
                delta_T = temp_0[i][j]-temp_0[i-1][j]
                delta_x = 1
                k = (conductivity[i][j]+conductivity[i-1][j])/2
                
                q = r(delta_T,delta_x,k)
                
                temperature[i][j] += dt*q*specific_heat[i][j]
                
            if (j > 0):
                delta_T = temp_0[i][j]-temp_0[i][j-1]
                delta_x = 1
                k = (conductivity[i][j]+conductivity[i-1][j-1])/2
                
                q = r(delta_T,delta_x,k)
                
                temperature[i][j] += dt*q*specific_heat[i][j]
                           
            if (i < xsize-1):
                delta_T = temp_0[i][j]-temp_0[i+1][j]
                delta_x = 1
                k = (conductivity[i][j]+conductivity[i+1][j])/2
                
                q = r(delta_T,delta_x,k)
                
                temperature[i][j] += dt*q*specific_heat[i][j]
                
            if (j < ysize-1):
                delta_T = temp_0[i][j]-temp_0[i][j+1]
                delta_x = 1
                k = (conductivity[i][j]+conductivity[i][j+1])/2
                
                q = r(delta_T,delta_x,k)
                
                temperature[i][j] += dt*q*specific_heat[i][j]
                
                
            
pyp.contourf(temperature)
