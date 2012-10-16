#!/usr/bin/env python
# -*- coding: utf-8 -*--

#Script para calcular e plotar a força em y

import os
import sys
sys.path.insert(0, os.path.abspath('../source'))

import scipy as sp
import matplotlib.pyplot as plt

import Es

entrada = ('NavioTeste', '../dados/derivada.dat', 'inputtab.dat')
en = Es.es(entrada)

a = en.fydertotab()
print a

plt.clf()
plt.plot(a[:,0], a[:,1])
#plt.show()
plt.savefig('teste.eps', format='eps')