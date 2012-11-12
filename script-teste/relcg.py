# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis

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

#pdb.set_trace()
i = 0
while sp.sqrt((posHis[i,6] - posHis[0,6])**2) < (sp.pi/2): i += 1

j = i
while sp.sqrt((posHis[j,6] - posHis[0,6])**2) < (sp.pi): j += 1

k = j
while (velHis[k,6] != velHis[k-10,6]): k += 1
while (velHis[k,1] != velHis[k-10,1]): k +=1
while (velHis[k,2] != velHis[k-10,2]): k +=1  

print 'Tempo para mudara a proa {0:.2f} \
{1:.0f}'.format(posHis[i,6]*(180/sp.pi), posHis[i,0])
print 'Tempo para mudara a proa {0:.2f} \
 {1:.0f}'.format(posHis[j,6]*(180/sp.pi), posHis[j,0])
print 'Avanço {0:.2f}m  {1:.2f}ft'.format(posHis[i,1], posHis[i,1]*3.28)
print 'Transferência {0:.2f}m  {1:.2f}ft'.format(posHis[i,2], posHis[i,2]*3.28)
print 'Diâmetro tático {0:.2f}m  {1:.2f}ft'.format(posHis[j,2],
posHis[j,2]*3.28)
print 'Raio da Curva de Giro no Equilíbrio \
{0:.2f}m  {1:.2f}ft'.format(r=sp.sqrt(velHis[k,2]**2 +
velHis[k,1]**2)/velHis[k,6], r*3.28)
print 'u no equilíbrio {0:.2f}'.format(velHis[k,1])
print 'v no equilíbrio {0:.2f}'.format(velHis[k,2])
print 'r no equilíbrio {0:.2f}'.format(velHis[k,6])
print 'Velocidade total {0:.2f}'.format(sp.sqrt(velHis[k,1]**2 + velHis[k,2]**2))
