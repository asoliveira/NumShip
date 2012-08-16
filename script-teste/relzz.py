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
lemezz = 20.
proazz = 20. 
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

#i indexa o momento em que a proa atinge execução
i = 0
while ((sp.sqrt(posHis[i,6]**2) - sp.sqrt(posHis[0,6]**2)) <
  (sp.pi/180)*(proazz)): 
  i += 1

o1 = i
#o1 indexa o momento em que a proa alcança o primeiro overshoot
while sp.sqrt(posHis[o1 + 1,6]**2) > sp.sqrt(posHis[o1,6]**2): 
  o1 += 1  

r = o1 
if posHis[r,6] > 0:
  while posHis[r,6] > posHis[0,6]: r += 1
else:
  while posHis[r,6] < posHis[0,6]: r += 1
#r  indexa o reach

o2 = r
#o2 = 0#indexa o momento em que a proa alcança o segundo overshoot
while sp.sqrt(posHis[o2 + 1,6]**2) > sp.sqrt(posHis[o2,6]**2): 
  o2 += 1  
  
o3 = o2
if (posHis[o3,6] - posHis[0,6]) < 0:
  while posHis[o3,6] < posHis[0,6]: o3 += 1
else:
  while posHis[o3,6] > posHis[0,6]: o3 += 1  
  
while sp.sqrt(posHis[o3,6]**2) < sp.sqrt(posHis[o3 + 1,6]**2): 
  o3 += 1
  

#Overshoot path  
 

p1 = i
#p1 indexa o momento em que a proa alcança o primeiro overshoot
while sp.sqrt(posHis[p1 + 1,2]**2) > sp.sqrt(posHis[p1,2]**2): 
  p1 += 1  

  
print 'Distancia lateral percorrida no \n \
momento da primeira execução {0:.2f}'.format(posHis[i,2])
print 'Overshoot da distancia lateral  percorrida  \n \
 {0:.2f}'.format(sp.sqrt((posHis[p1,2] - posHis[i,2])**2))
print 'Tempo para mudara a proa {0:.2f} \
{1:.0f}'.format(posHis[i,6]*(180/sp.pi), posHis[i,0])
print 'Tempo para alcançar o Reach \
{0:.2f}'.format(posHis[r,0])
print 'Overshoot 1 \
{0:.2f}'.format((sp.sqrt(posHis[o1,6]**2) - (sp.pi/180) * proazz) * 
(180/sp.pi))
print 'Overshoot 2 {0:.2f}'.format((sp.sqrt(posHis[o2,6]**2) - 
(sp.pi/180)*proazz)*(180/sp.pi)) 
print 'Overshoot 3 {0:.2f}'.format((sp.sqrt(posHis[o3,6]**2) - 
(sp.pi/180)*proazz)*(180/sp.pi))