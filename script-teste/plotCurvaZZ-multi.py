# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dirzz -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
szzarq = 'plot'
formato = 'pdf'
TipoModelo = 'leme-'
GrausDeLib = 3
tini = 0
tmax = 900
lemezz = 20
axzz = [tini, tmax, -abs(lemezz + 25), abs(lemezz + 20)] 
axleme = [tini, tmax, -abs(lemezz + 25), abs(lemezz + 20)] 
#Quais são as pastas?
p = ('padrao', 'leme/leme-10', 'leme/leme-20', 'leme/leme-30')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaZigZag/'
#Dentro de cada diretório quais são as arq?
arq = ('pos.dat', 'leme.dat')
#legendas
ld = (ur'S1', 
r'$10 \% D$', 
r'$20 \% D$',
r'$30 \% D$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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


#Curva de Zigzag 20/20
fig = plt.figure()

gs = gridspec.GridSpec(2, 1, width_ratios=[1,0], height_ratios=[1,4])
ax = fig.add_subplot(gs[1])

plt.axis(axzz)

for a in range(len(posHis)):
  (ax.plot(posHis[a][:,0], posHis[a][:,6] * (180/sp.pi)))

l1 = plt.legend(ld, bbox_to_anchor=(.0, 1.1, 0.45, 0.2), loc=3, ncol=2, mode="none", borderaxespad=0.)
plt.grid(True)
ax.set_ylabel(r'$\psi \quad (graus)$')
ax.set_xlabel(r'$t \quad (segundos)$')

ax1 = ax.twinx() 
ax1.set_ylabel(r'$\delta_R \quad (graus)$') 
ax1.axis(axleme)

for a in range(len(lemeHis)):
  ax1.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi), '--')

l2 = plt.legend(ld, bbox_to_anchor=(.55, 1.1, .45, .2), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.gca().add_artist(l1)  
if save:
    plt.savefig(dirzz + TipoModelo +'zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()


