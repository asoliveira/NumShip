#! /usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

B = array([0, 1.1, 1.2, 1.3])
A = array([908.44, 879.98, 854.81, 833.00])

def res (p, A, B):
    a, b = p
    err = A - (a + b*B)
    return err

def eval (B , p):
    s = p[0] + p[1]*B 
    return s

p0 = (500, 500)
plsq = leastsq(res, p0, args=(A, B))
print plsq[0] 
plt.plot(B, A, 'go', B, eval(B, plsq[0]), 'b-')
plt.legend(['real', 'Fit'])
plt.show()
