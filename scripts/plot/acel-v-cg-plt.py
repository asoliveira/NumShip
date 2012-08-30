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
nome = 'acel-v-cg'
#Qual título colocar no gráficos?
titulo = ''#'Curva de Giro'
#Qual a cor dos gráficos?
pc = 'r'
bc = 'g'
lc = 'b'
brlc ='y'
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
        
acelhis = sp.genfromtxt('../entrada/padrao/CurvaGiro/acel.dat')
acelhis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/acel.dat')
acelhis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/acel.dat')
acelhis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/acel.dat')
acelhis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaGiro/acel.dat')

axl = [0, 800, 0, -0.04]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$v\prime$'
    xacellabel = r'$t\prime$'
else:
    ylabel = r'$\dot v \quad m/s^2$'    
    xacellabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acelhis[:, 0],  acelhis[:, 2],  color = pc, linestyle = ps,
linewidth = 1, label=ur'$M1$')
plt.plot(acelhis2[:, 0],  acelhis2[:, 2],  color = bc,linestyle = bs,
linewidth = 1, label=ur'1.2$\beta$')
plt.plot(acelhis3[:, 0], acelhis3[:, 2], 
color = rc, linestyle = rs, label=ur'1.2r')
plt.plot(acelhis4[:, 0], acelhis4[:, 2], 
color = lc, linestyle = ls,  label=ur'1.2$\delta_R$')
plt.plot(acelhis5[:, 0], acelhis5[:, 2], 
color = brlc, linestyle = brls, label=ur'1.2brl')
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
