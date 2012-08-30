# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dirzz -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
szzarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-zz-'
GrausDeLib = 3
tini = 0
tmax = 900
lemezz = 20
axzz = [tini, tmax, -abs(lemezz + 25), abs(lemezz + 20)] 
axleme = [tini, tmax, -abs(lemezz + 25), abs(lemezz + 20)] 
#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaZigZag/'
#Dentro de cada diretório quais são as arq?
arq = ('pos.dat', 'leme.dat')
#legendas
ld = (r'$X_{\delta \delta \eta \eta} = 0.0$', 
r'$X_{\delta \delta \eta \eta} = 0.002$', 
r'$X_{\delta \delta \eta \eta} = 0.005$',
r'$X_{\delta \delta \eta \eta} = 0.008$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


dirzz = szzarq + '/figuras/'   
if not os.path.exists(dirzz):
  os.makedirs(dirzz)
  
pos = []
leme = []
for arg in p:
  pos.append(arg + dircomum + arq[0])
for arg in p:
  leme.append(arg + dircomum + arq[1])  

posHis = []
lemeHis = []
for arg in pos:
  posHis.append(np.genfromtxt(arg))
for arg in leme:
  lemeHis.append(np.genfromtxt(arg))

#Curva de Zigzag 20/10
fig = plt.figure()
ax = fig.add_subplot(111)

plt.axis(axzz)
for a in range(len(posHis)):
  ax.plot(posHis[a][:,0], posHis[a][:,6] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
ax.set_ylabel(r'$\psi \quad (graus)$')
ax.set_xlabel(r'$t \quad (segundos)$')

ax1 = ax.twinx() 
ax1.set_ylabel(r'$\delta_R \quad (graus)$')
ax1.axis(axleme)

for a in range(len(lemeHis)):  
  ax1.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi))
  
if save:
    plt.savefig(dirzz + TipoModelo +'curvazz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

