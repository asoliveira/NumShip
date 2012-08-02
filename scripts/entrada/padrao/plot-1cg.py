#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import scipy as sp
#Nome do arquivo em que está os dados da posição
arq = 'CurvaGiro/pos.dat'
#Limites dos eixos
v = [-10,1000, 0, 1000]
#Título eixo x
xl = r'y metros'
#Título do eixo y
yl = r'x metros'

x = sp.genfromtxt('CurvaGiro/pos.dat')

a = plt.plot(x[:,2], x[:,1], 'k-')
plt.grid(True, 'both', color = '0.8', linestyle = '--', linewidth = 1)
plt.axis(v)
plt.xlabel(xl)
plt.ylabel(yl)
plt.show(a)
