# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-zz-'
GrausDeLib = 3
tini = 0
tmax = 1000
lemezz = 20
ForEs = 1e0
uini = 4 
umax = 9
vini = -2
vmax = 2
rini = -0.7
rmax = 0.6
duini = -0.02
dumax = 0.01
dvini = -0.02 
dvmax = 0.02
drini = -0.03
drmax = 0.03
fuini = -1000000
fumax = 1000
fvini = 1000 
fvmax = 1000000
nini =  -4000
nmax = 1000000
rotini = 0
rotmax = 2
etaini = 1
etamax = 1.8

import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pdb

posHis = np.genfromtxt('pos.dat')
velHis = np.genfromtxt('velo.dat')
lemeHis = np.genfromtxt('leme.dat')
acelHis = np.genfromtxt('acel.dat')
forHis = np.genfromtxt('forcas.dat')
etaHis = np.genfromtxt('eta.dat')
propHis = np.genfromtxt('propulsor.dat')

try:
  dircg = scgarq + '/figuras/' 
  os.makedirs(dircg)
except NameError:
  print 'houve algum problema na criação do diretório ' + dircg

xlabel = r't  (segundos)'

#Curva de Zigzag
fig = plt.figure()
ax = fig.add_subplot(111)

if adi:
    ylabel = r'$graus$'
    xposlabel = r'$t\prime$'
else:
    ylabel = r'$graus$'    
    xposlabel = r'$t \quad (segundos)$'    

plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
plt.axis([tini, tmax,-abs(lemezz + 20), abs(lemezz + 20)])
ax.plot(posHis[:,0], posHis[:,6]*(180/sp.pi), 'b-',
lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-')
leg = ax.legend((r'$\psi$', r'$\delta_R$'), loc = 'upper right')
 
if save:
    plt.savefig(dircg + TipoModelo +'zz.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em Surge        
    
if adi:
    xlabel = r't $\prime$'
else:
    xlabel = r't (segundos)'

plt.plot(velHis[:, 0], velHis[:, 1], 'b-', label = r'$u$')

if adi:
    ylabel = r'$u\prime$'
else:
    ylabel = r'$u \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.axis([tini, tmax, uini, umax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz + 5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'u.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade em sway
    
plt.plot(velHis[:, 0], velHis[:, 2], 'b-', label = r'$v$')

if adi:
    ylabel = r'$v\prime$'
else:
    ylabel = r'$v \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.axis([tini, tmax, vini, vmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'v.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Velocidade de yaw
    
plt.plot(velHis[:, 0], velHis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot\psi$')
plt.grid(True)
if adi:
    ylabel = r'$r\prime$'
else:
    ylabel = r'$r \quad (graus/s)$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, rini, rmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz + 5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')    

if save:
    plt.savefig(dircg + TipoModelo +'r.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#Aceleração
#dot u

if adi:
    ylabel = r'$\dot u \prime$'
else:
    ylabel = r'$\dot u \quad m\times s^{-2}$'
    
plt.plot(acelHis[:, 0], acelHis[:, 1], 'b-', label = r'$\dot u$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, duini, dumax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'acel-u.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 


#Dot v

if adi:
    ylabel = r'$\dot v \prime$'
else:
    ylabel = r'$\dot v \quad m\times s^{-2}$'

plt.plot(acelHis[:, 0], acelHis[:, 2], 'b-', label = r'$\dot v$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, dvini, dvmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')
if save:
    plt.savefig(dircg + TipoModelo +'acel-v.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 


#Aceleração de yaw

if adi:
    ylabel = r'$\dot r \prime$'
else:
    ylabel = r'$\dot r \quad graus\times s^{-2}$'

plt.plot(acelHis[:, 0], acelHis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot r$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, drini, drmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'acel-r.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#Forças

#Forças em surge

if adi:
    ylabel = r'$F_x \prime$'
else:
    ylabel = r'$F_x \quad N$'

plt.plot(forHis[:, 0], forHis[:, 1]*ForEs, 'b-', label = r'$F_x$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, fuini, fumax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')


if save:
    plt.savefig(dircg + TipoModelo +'for-u.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#Força em Sway
if adi:
    ylabel = r'$F_y \prime$'
else:
    ylabel = r'$F_y \quad N $'
    
plt.plot(forHis[:, 0], forHis[:, 2]*ForEs, 'b-', label = r'$F_y$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, fvini, fvmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'for-y.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#Momento de yaw

    
if adi:
    ylabel = r'$N \prime$'
else:
    ylabel = r'$N \quad N \times m$'

plt.plot(forHis[:, 0], forHis[:, 4]*ForEs, 'b-', label = r'$N$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.axis([tini, tmax, nini, nmax])

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemezz +5), abs(lemezz +5) ])
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dircg + TipoModelo +'for-n.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#Rotação da máquina

plt.plot(propHis[:, 0], propHis[:, 1], 'o-', label = r'$rot$')
plt.grid(True)
plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(xlabel)
plt.axis([tini, tmax, rotini, rotmax])

if save:
    plt.savefig(dircg + TipoModelo +'pltnt.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#eta

plt.plot(etaHis[:, 0], etaHis[:, 1], '--', label = r'$\eta$')
plt.grid(True)
plt.ylabel(r'$\eta$ ')
plt.xlabel(xlabel)
plt.axis([tini, tmax, etaini, etamax])

if save:
    plt.savefig(dircg + TipoModelo +'pltetat.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
