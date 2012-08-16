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
TipoModelo = 'marad'
GrausDeLib = 3
tini = 0
tmax = 4000
lemecg = 35
ForEs = 1e0
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pdb

posHis = np.genfromtxt('pos.dat')
betaHis = np.genfromtxt('beta.dat')
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

if adi:
    xlabel = r't'
    tini = velHis[0, 0]
    tmax = velHis[-1, 0]
else:
    xlabel = r't \ seg'

#Curva de diro

if adi:
    ylabel = r'$x\prime$'
    xposlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xposlabel = r'$y \quad m$'    
    plt.plot(posHis[:,2], posHis[:,1], 'b-')    
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

##Ângulo de deriva

if adi:
    ylabel = r'$\beta$'
    xlabel = r'$t \prime$'
else:
    ylabel = r'$\beta$'
    xlabel = r'$t $'

plt.plot(betaHis[:, 0], betaHis[:, 1]*(180/sp.pi), 'bo', label =
r'$\beta$')
plt.grid(True)
plt.ylabel(r'$\beta(graus)$')
plt.xlabel('$t(segundos)$')
 
if save:
    plt.savefig(dircg + TipoModelo +'beta.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

##Velocidade em Surge        
    
if adi:
    xlabel = r't'
else:
    xlabel = r't \ seg'

plt.plot(velHis[:, 0], velHis[:, 1], 'b-', label = r'$u$')

if adi:
    ylabel = r'$u\prime$'
else:
    ylabel = r'$u \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg + 5), abs(lemecg +5) ])
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
plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg + 5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g-', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', 
label = r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

plt.twinx()
plt.plot(lemeHis[:, 0], lemeHis[:, 1]*(180/sp.pi), 'g--', label =
r'$\delta_R$')
plt.grid(True)
plt.axis([tini, tmax, -abs(lemecg +5), abs(lemecg +5) ])
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

if save:
    plt.savefig(dircg + TipoModelo +'pltetat.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
