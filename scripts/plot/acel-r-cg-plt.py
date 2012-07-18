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
nome = 'acel-r-cg'
#Qual título colocar no gráficos?velo
titulo = ''#'Curva de Giro'
#Qual a cor dos gráficos?
pc = 'k'
bc = 'k'
lc = 'k'
brlc = 'k'
rc = 'k'
#Estilo de linha
ps = '-'
bs = '-.'
rs = '.'
ls = '+'
brls = '^'

import os

import scipy as sp
import matplotlib.pyplot as plt

from libplot import *
        
acelhis = sp.genfromtxt('../entrada/padrao/CurvaGiro/acel.dat')
acelhis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/acel.dat')
acelhis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/acel.dat')
acelhis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/acel.dat')
acelhis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaGiro/acel.dat')

axl = [0, 800, -0.004, 0.025]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$\dot v\prime$'
    xacellabel = r'$t\prime$'
else:
    ylabel = r'$\dot r \quad graus/s^2$'    
    xacellabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acelhis[:, 0],  acelhis[:, 6] * (180 / sp.pi),  color = pc, linestyle
= ps,
linewidth = 1, label=ur'padrão')
plt.plot(acelhis2[:, 0],  acelhis2[:, 6] * (180 / sp.pi),  color = bc,linestyle
= bs,
linewidth = 2, label=ur'1.2beta')
plt.scatter(somep(acelhis3[:, 0], num = 200), somep(acelhis3[:, 6] * (180 /
sp.pi), num =
200), 
color = rc, marker = rs, s = 8, label=ur'1.2r')
plt.scatter(somep(acelhis4[:, 0], num = 100),  somep(acelhis4[:, 6] * (180 /
sp.pi), num =
100), 
color = lc, marker = ls, s = 20, label=ur'1.2leme')
plt.scatter(somep(acelhis5[:, 0], num = 100), somep(acelhis5[:, 6] * (180 /
sp.pi), num =
100), 
color = brlc, marker = brls, s = 14, label=ur'1.2brl')
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
