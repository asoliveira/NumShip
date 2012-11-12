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
TipoModelo = 'velo-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
axu = [tini, tmax, 2., 9]
axv = [tini, tmax, -2.5, 0]
axr = [tini, tmax, 0.0, 0.9]

#Quais são as pastas?
p = ('padrao',
'saida-xddee/saida-xddee0'
'saida-xddee/saida-xddee0.002', 
'saida-xddee/saida-xddee0.005', 
'saida-xddee/saida-xddee0.008',
'saida-xddee/saida-xddee-5e-5',
'saida-xddee/saida-xddee-0.005')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'velo.dat',
#legendas
ld = (r'$x_{\delta_R\delta_R \eta \eta}=0$', 
r'$x_{\delta_R\delta_R \eta \eta}=2e-3$', 
r'$x_{\delta_R\delta_R \eta \eta}=5e-3$',
r'$x_{\delta_R\delta_R \eta \eta}=8e-3$',
r'$x_{\delta_R\delta_R \eta \eta}=-5e-5$',
r'$x_{\delta_R\delta_R \eta \eta}=-5e-3$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


dircg = scgarq + dircomum
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
