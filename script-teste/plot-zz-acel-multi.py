# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dirzz -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#acelHis
adi = False
save = True #Salva a figura?
szzarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-zz-'
GrausDeLib = 3
tini = 0
tmax = 900
lemezz = 20
axu = [tini, tmax, 4, 9]
axv = [tini, tmax, -2.0, 2.0]
axr = [tini, tmax, -0.7, 0.7]
axleme = [tini, tmax, -abs(lemezz + 5), abs(lemezz + 5)] 

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaZigZag/'
#Dentro de cada diretório quais são as arq?
arq = ('acel.dat', 'leme.dat')
#legendas
ld = (r'$X_{\delta \delta \eta \eta} = 0.0$', 
r'$X_{\delta \delta \eta \eta} = 0.002$', 
r'$X_{\delta \delta \eta \eta} = 0.005$',
r'$X_{\delta \delta \eta \eta} = 0.008$')


#import 
import os
import pdb
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


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
#Velocidade em surge
fig1 = plt.figure(1)
ax = fig1.add_subplot(111)

#plt.axis(axu)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
ax.set_ylabel(r'$\dot u (metros/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)

for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi))
    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-u-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em sway    
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)

#plt.axis(axv)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,2])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
ax.set_ylabel(r'$\dot v (metros/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)

for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi))
    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-v-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()    
#Velocidade do yaw
fig3 = plt.figure(3)
ax = fig3.add_subplot(111)

#plt.axis(axr)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,6] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
ax.set_ylabel(r'$\dot r (graus/segundos^2)$')
ax.set_xlabel(r'$t \quad segundos$')

ax2 = ax.twinx()
ax2.set_ylabel(r'$\delta_R \quad (graus)$')
ax2.axis(axleme)

for a in range(len(lemeHis)):  
  ax2.plot(lemeHis[a][:,0], lemeHis[a][:,1] * (180/sp.pi))
    
if save:
    plt.savefig(dirzz + TipoModelo +'acel-r-zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()