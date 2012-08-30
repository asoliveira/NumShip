#!/usr/bin/env python
# -*- coding: utf-8 -*-

#É adimensional?
adi = False
#É para salvar as figuras(True|False)?
save = True
#Caso seja para salvar, qual é o formato desejado?
formato = 'pdf'
#Caso seja para salvar, qual é o diretório que devo salvar?
dircg = 'fig-sen'
#Caso seja para salvar, qual é o nome do arquivo?
nome = 'velo-u-cg'
#Qual título colocar no gráficos?
titulo = ''#'Curva de Giro'
#Qual a cor dos gráficos?
pc = 'r'
bc = 'g'
lc = 'b'
brlc = 'y'
rc = 'm'
#Estilo de linha
ps = '-'
bs = '-'
rs = '-'
ls = '-'
brls = '-'

import os

import scipy as sp
import matplotlib.pyplot as plt

from libplot import *
        
velohis = sp.genfromtxt('../entrada/padrao/CurvaGiro/velo.dat')
velohis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/velo.dat')
velohis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/velo.dat')
velohis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/velo.dat')
velohis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaGiro/velo.dat')

axl = [0, 800, 1, 9]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$u\prime$'
    xvelolabel = r'$t\prime$'
else:
    ylabel = r'$u \quad m/s$'    
    xvelolabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(velohis[:, 0],  velohis[:, 1],  color = pc, linestyle = ps,
linewidth = 1, label=ur'$M1$')
plt.plot(velohis2[:, 0],  velohis2[:, 1],  color = bc,linestyle = bs,
linewidth = 1, label=ur'1.2$\beta$')
plt.plot(velohis3[:, 0], velohis3[:, 1], 
color = rc, linestyle = rs, label=ur'1.2r')
plt.plot(velohis4[:, 0], velohis4[:, 1], 
color = lc, linestyle = ls,  label=ur'1.2$\delta_R$')
plt.plot(velohis5[:, 0], velohis5[:, 1], 
color = brlc, linestyle = brls, label=ur'1.2brl')
plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xvelolabel)
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
