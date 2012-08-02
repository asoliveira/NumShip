#!/usr/bin/env python
# -*- coding: utf-8 -*-

#É adimensional?
adi = False
#É para salvar as figuras(True|False)?
save = True
#Caso seja para salvar, qual é o formato desejado?
formato = 'jpg'
#Caso seja para salvar, qual é o diretório que devo salvar?
dircg = 'fig-sen'
#Caso seja para salvar, qual é o nome do arquivo?
nome = 'brl-zz'
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
        
poshis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/pos.dat')
poshis2 = sp.genfromtxt('../entrada/brl/saida1.1/CurvaZigZag/pos.dat')
poshis3 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaZigZag/pos.dat')
poshis4 = sp.genfromtxt('../entrada/brl/saida1.3/CurvaZigZag/pos.dat')

lemehis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/leme.dat')
lemehis2 = sp.genfromtxt('../entrada/brl/saida1.1/CurvaZigZag/leme.dat')
lemehis3 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaZigZag/leme.dat')
lemehis4 = sp.genfromtxt('../entrada/brl/saida1.3/CurvaZigZag/leme.dat')

axl = [00, 1000, -40, 40]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$\psi\prime$'
    xposlabel = r'$t\prime$'
else:
    ylabel = r'$\psi \quad graus$'    
    xposlabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(poshis[:, 0],  poshis[:, 6] * (180/sp.pi),  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(lemehis[:, 0],  lemehis[:, 1] * (180/sp.pi),  color = pc, linestyle = "--",
linewidth = 1, label=ur'leme--padrão')

plt.plot(poshis2[:, 0],  poshis2[:, 6] * (180/sp.pi),  color = r1c,linestyle = r1s,
linewidth = 1, label=ur'1.1$brl$')
plt.plot(lemehis2[:, 0],  lemehis2[:, 1] * (180/sp.pi),  color = r1c, linestyle = "--",
linewidth = 1, label=ur'leme--1.1$brl$')

plt.plot(poshis3[:, 0], poshis3[:, 6] * (180/sp.pi), color = r2c, linestyle = r2s, 
linewidth = 1, label = ur'1.2$brl$')
plt.plot(lemehis3[:, 0],  lemehis3[:, 1] * (180/sp.pi),  color = r2c, linestyle = "--",
linewidth = 1, label=ur'leme--1.2$brl$')

plt.plot(poshis4[:, 0], poshis4[:, 6] * (180/sp.pi), color = r3c, linestyle = r3s, 
linewidth = 1, label= ur'1.3$brl$')
plt.plot(lemehis4[:, 0],  lemehis4[:, 1] * (180/sp.pi),  color = r3c, linestyle = "--",
linewidth = 1, label=ur'leme--1.3$brl$')

plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
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
