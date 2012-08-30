# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#veloHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-cg-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
axu = [tini, tmax, 2, 9]
axv = [tini, tmax, -2.5, 0]
axr = [tini, tmax, 0, 0.9]

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'velo.dat',
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
  
velo = []
for arg in p:
  velo.append(arg + dircomum + arq[0])

veloHis = []
for arg in velo:
  veloHis.append(np.genfromtxt(arg))

#Curva de giro
#Velocidade em surge
fig1 = plt.figure(1)
ax = fig1.add_subplot(111)
if adi:
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    

plt.axis(axu)
for a in range(len(veloHis)):  
  ax.plot(veloHis[a][:,0], veloHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$u (metros/segundos)$')
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
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    

plt.axis(axv)
for a in range(len(veloHis)):
  ax.plot(veloHis[a][:,0], veloHis[a][:,2])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$v (metros/segundos)$')
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
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    
plt.axis(axr)
for a in range(len(veloHis)):
  ax.plot(veloHis[a][:,0], veloHis[a][:,6] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(r'$r\quad (graus/segundos)$')
plt.xlabel(xlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'r-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()    