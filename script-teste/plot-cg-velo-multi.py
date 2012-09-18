# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#acelHis
adi = False
save = True #Salva a figura?
scgarq = 'plot'
formato = 'pdf'
TipoModelo = 'beta-velo-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
axu = [tini, tmax, 2., 9]
axv = [tini, tmax, -2.5, 0]
axr = [tini, tmax, 0.0, 0.9]

#Quais são as pastas?
p = ('padrao', 'beta/beta-10', 'beta/beta-20', 'beta/beta-30')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'velo.dat',
#legendas
ld = (r'$S1$', 
r'$10\% \ B$', 
r'$20\% \ B$',
r'$30\% \ B$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


dircg = scgarq + '/figuras/'   
if not os.path.exists(dircg):
  os.makedirs(dircg)
  
acel = []
for arg in p:
  acel.append(arg + dircomum + arq[0])

acelHis = []
for arg in acel:
  acelHis.append(np.genfromtxt(arg))

#Curva de giro
#Velocidade em surge
fig1 = plt.figure(1)
ax = fig1.add_subplot(111)
if adi:
    xlabel = r'$t\prime$'
else:   
    xlabel = r'$t \quad segundos$'    
    ylabel = r'$u (m/s)$'
plt.axis(axu)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'u-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em sway    
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)
if adi:
    ylabel = r'$v\prime$'
    xlabel = r'$t\prime$'
else:
    ylabel = r'$v (m/s)$'    
    xlabel = r'$t \quad segundos$'    

plt.axis(axv)
for a in range(len(acelHis)):
  ax.plot(acelHis[a][:,0], acelHis[a][:,2])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'v-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    
#Velocidade do yaw
fig3 = plt.figure(3)
ax = fig3.add_subplot(111)
if adi:
    ylabel = r'$r\prime$'
    xlabel = r'$t\prime$'
else:
    ylabel = r'$r \quad (graus/segundos)$'    
    xlabel = r'$t \quad segundos$'    
plt.axis(axr)
for a in range(len(acelHis)):
  ax.plot(acelHis[a][:,0], acelHis[a][:,6] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'r-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()    
