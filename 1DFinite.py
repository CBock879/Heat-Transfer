# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:36:57 2018

@author: Chris
"""


import numpy as np
import matplotlib.pyplot as pyp
from sympy import Symbol
from sympy.solvers import solve
import sympy as sp




#inital conditions
x = np.linspace(0,1)
u = np.sin(x*np.pi)
L = 1;

xsteps = x.size
dx = L/xsteps
beta = 0
alpha = 0.005

#boundry conditions
B1 = 0;
u[0]= B1
B2 = 0;
u[xsteps-1] = B2

time_steps = 1000
dt = 0.01


#solving for "zeta"
z = Symbol('z')
e0 = u[20]

tout = 0;
pyp.hold(True)
pyp.plot(x,u)

#divergence factor number of times simulation performs unexpectly
divergence = np.zeros(xsteps)

#looks at element wise behavior
e  = [u[20]]  

        
for j in range(0,time_steps):
    t0 = u.copy()
    for i in range(0,xsteps):
         
         if (i < 1):
             #print("H")
             u[i] = B1
             
         elif(i==xsteps-1):
             
             u[i] = B2
              
         else:
             u[i] = ((t0[i+1] -(2* t0[i]) + t0[i-1]) *((dt) * alpha/ (dx**2)) + t0[i]) - beta*(t0[i] - tout)
             
             
             
             
             #tests for divergence 
             de = np.abs(u[i]-((u[i+1]+u[i]+u[i-1])/3))
             divergence[i] = de
    
    #element of interest for solving for zeta
    e.append(u[20])
    
    
#print(np.mean(divergence))
t = time_steps*dt

#print(solve(u0*sp.exp(t*z)-e[time_steps],z))

t  = time_steps*dt
pyp.plot(x,u)   
#pyp.plot(e)
#pyp.plot(divergence)
pyp.hold(False) 
