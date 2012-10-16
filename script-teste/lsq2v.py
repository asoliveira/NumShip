#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


arq = 'BvsR.csv'

tab = np.genfromtxt(arq, delimiter=';')
x = tab[0,2:]
y = tab[2:,0]
tab = tab[2:,2:]
  
def A (x, y):
  xx, yy = np.meshgrid(x,y)
  a1 = np.hstack(xx)
  a2 = np.hstack(yy)
  a0 = np.ones(a1.shape)
  s = np.vstack([a0, a1, a2])
  
  return s.T

a, b, c = np.linalg.lstsq(A(x,y), np.hstack(tab))[0]
print a, b, c
p = (a, b, c)
xx, yy = np.meshgrid(x,y) 

def f (par=p, varx=xx, vary=yy):
  
  return p[0] + p[1]*varx + p[2]*vary

#Plotando
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, f(), rstride=8, cstride=8, alpha=0.3)
ax.scatter(xx, yy, tab, c='r')

plt.show()