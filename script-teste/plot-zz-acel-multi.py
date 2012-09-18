# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dirzz -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#acelHis
adi = False
save = True #Salva a figura?
szzarq = 'plot'
formato = 'pdf'
TipoModelo = 'leme-'
GrausDeLib = 3
tini = 0
tmax = 900
lemezz = 20
axu = [tini, tmax, 4, 9]
axv = [tini, tmax, -2.0, 2.0]
axr = [tini, tmax, -0.7, 0.7]
axleme = [tini, tmax, -abs(lemezz + 5), abs(lemezz + 5)] 

#Quais são as pastas?
p = ('padrao', 'leme/leme-10', 'leme/leme-20', 'leme/leme-30')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaZigZag/'
#Dentro de cada diretório quais são as arq?
arq = ('acel.dat', 'leme.dat')
#legendas
ld = (ur'S1', 
r'$10 \% D$', 
r'$20 \% D$',
r'$30 \% D$')


#import 
import os
import pdb
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

dirzz = szzarq + '/figuras/'   
if not os.path.exists(dirzz):
  os.makedirs(dirzz)
  
acel = []
leme = []
for arg in p:
  acel.append(arg + dircomum + arq[0])
  leme.append(arg + dircomum + arq[1])
  
acelHis = []
lemeHis = []
for arg in acel:
  acelHis.append(np.genfromtxt(arg))
for arg in leme:  
  lemeHis.append(np.genfromtxt(arg))
#Curva de giro
#Aceleracao em surge
fig1 = plt.figure(1)
gs = gridspec.GridSpec(2, 1, width_ratios=[1,0], height_ratios=[1,4])
ax = fig1.add_subplot(gs[1]) 

#plt.axis(axu)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,1])

l1 = plt.legend(ld, bbox_to_anchor=(.0, 1.1, .45, .2), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.grid(True)
ax.set_ylabel(r'$\dot u (metros/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)


for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi), '--')
plt.legend(ld, bbox_to_anchor=(.55, 1.1, .45, .2), loc=3, ncol=2,
mode="expand", borderaxespad=0.)
plt.gca().add_artist(l1)#N�o est� sendo necess�rio
    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-u-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em sway    
fig2 = plt.figure(2)
gs = gridspec.GridSpec(2, 1, width_ratios=[1,0], height_ratios=[1,4])
ax = fig2.add_subplot(gs[1]) 

#plt.axis(axv)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,2])
l1 = plt.legend(ld, bbox_to_anchor=(.0, 1.1, .45, .2), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.grid(True)
ax.set_ylabel(r'$\dot v (metros/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)

for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi), '--')
plt.legend(ld, bbox_to_anchor=(.55, 1.1, .45, .2), loc=3, ncol=2,
mode="expand", borderaxespad=0.)
#plt.gca().add_artist(l1)
    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-v-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()    
#Velocidade do yaw
fig3 = plt.figure(3)
gs = gridspec.GridSpec(2, 1, width_ratios=[1,0], height_ratios=[1,4])
ax = fig3.add_subplot(gs[1]) 

#plt.axis(axr)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,6] * (180/sp.pi))
l1 = plt.legend(ld, bbox_to_anchor=(.0, 1.1, .45, .2), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.grid(True)
ax.set_ylabel(r'$\dot r (graus/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)

for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi), '--')
plt.legend(ld, bbox_to_anchor=(.55, 1.1, .45, .2), loc=3, ncol=2,
mode="expand", borderaxespad=0.)
#plt.gca().add_artist(l1)    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-r-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
