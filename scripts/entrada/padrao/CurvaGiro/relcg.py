# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
GrausDeLib = 3
tini = 0
tmax = 4000
lemecg = 35
ForEs = 1e0
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pdb

posHis = np.genfromtxt('pos.dat')
#betaHis = np.genfromtxt('beta.dat')
velHis = np.genfromtxt('velo.dat')
#lemeHis = np.genfromtxt('leme.dat')
#acelHis = np.genfromtxt('acel.dat')
#forHis = np.genfromtxt('.forcas.dat')
#etaHis = np.genfromtxt('eta.dat')
#propHis = np.genfromtxt('propulsor.dat')

i = 0
while posHis[i,6] <= sp.pi/2: i += 1

j=i
while posHis[j,6] <= sp.pi: j += 1  

k=j
while (velHis[k,6] != velHis[k-1,6]) and (velHis[k,2] != velHis[k-1,2]): 
  k += 1

print 'Tempo para mudara a proa {0:.2f} \
{1:.0f}'.format(posHis[i,6]*(180/sp.pi), posHis[i,0])
print 'Tempo para mudara a proa {0:.2f} \
 {1:.0f}'.format(posHis[j,6]*(180/sp.pi), posHis[j,0])
print 'Avanço {0:.2f}'.format(posHis[i,1])
print 'Transferência {0:.2f}'.format(posHis[i,2])
print 'Diâmetro tático {0:.2f}'.format(posHis[j,2])
print 'Raio da Curva de Giro no Equilíbrio \
{0:.2f}'.format(sp.sqrt(velHis[k,2]**2 + velHis[k,1]**2)/velHis[k,6])