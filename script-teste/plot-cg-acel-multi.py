# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#acelHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-cg-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
axu = [tini, tmax, -0.04, 0.02]
axv = [tini, tmax, -0.035, 0.005]
axr = [tini, tmax, -0.003, 0.02]

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'acel.dat',
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
    xlabel = r'$t \quad (segundos)$'    

plt.axis(axu)
for a in range(len(acelHis)):  
  ax.plot(acelHis[a][:,0], acelHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$\dot u (metros/segundos^2)$')
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'du-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em sway    
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)
if adi:
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    

plt.axis(axv)
for a in range(len(acelHis)):
  ax.plot(acelHis[a][:,0], acelHis[a][:,2])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$\dot v (metros/segundos^2)$')
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'dv-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    
#Velocidade do yaw
fig3 = plt.figure(3)
ax = fig3.add_subplot(111)
if adi:
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    
plt.axis(axr)
for a in range(len(acelHis)):
  ax.plot(acelHis[a][:,0], acelHis[a][:,6] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$\dot r\quad (graus/segundos^2)$')
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'dr-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()    