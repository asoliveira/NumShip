#!/usr/bin/env python
# -*- coding: utf-8 -*-

#É adimensional?
adi = False
#É para salvar as figuras(True|False)?
save = True
#Caso seja para salvar, qual é o formato desejado?
formato = 'eps'
#Caso seja para salvar, qual é o diretório que devo salvar?
dircg = 'fig-sen'
#Caso seja para salvar, qual é o nome do arquivo?
nome = 'beta-acel-u-cg'
#Qual título colocar no gráficos?
titulo = ''#'Curva de Giro'
#Qual a cor dos gráficos?
pc = 'k'
r1c = 'b'
r2c = 'y'
r3c = 'r'
#Estilo de linha
ps = '-'
r1s = '-'
r2s = '-'
r3s = '-'

import os

import scipy as sp
import matplotlib.pyplot as plt

from libplot import *
        
acelhis = sp.genfromtxt('../entrada/padrao/CurvaGiro/acel.dat')
acelhis2 = sp.genfromtxt('../entrada/beta/saida1.1/CurvaGiro/acel.dat')
acelhis3 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/acel.dat')
acelhis4 = sp.genfromtxt('../entrada/beta/saida1.3/CurvaGiro/acel.dat')

axl = [0, 1000, -0.04, 0.0]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xacellabel = r'$\dot u\prime$'
else:
    ylabel = r'$\dot u \quad m^2/s$'    
    xacellabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acelhis[:, 0],  acelhis[:, 1],  color = pc, linestyle = ps,
linewidth = 2, label=ur'$M1$')

plt.plot(acelhis2[:, 0],  acelhis2[:, 1],  color = r1c,linestyle = r1s,
linewidth = 2, label=ur'$1.1\beta$')

plt.plot(acelhis3[:, 0], acelhis3[:, 1], color = r2c, linestyle = r2s,
linewidth = 2, label=ur'$1.2\beta$')

plt.plot(acelhis4[:, 0], acelhis4[:, 1], color = r3c, linestyle = r3s,
linewidth = 2, label=ur'$1.3\beta$')

plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xacellabel)
plt.axis(axl)
plt.grid(True)

if save:
    if not os.path.exists(dircg):
        os.makedirs(dircg)
    if os.path.exists(dircg + '/' + nome + '.' + formato):
        os.remove(dircg + '/' + nome + '.' + formato)
    plt.savefig(dircg + '/' + nome + '.' + formato ,  format=formato)
else:    
    plt.show()           
