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
nome = 'eta-cg'
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
        
etahis = sp.genfromtxt('../entrada/padrao/CurvaGiro/eta.dat')
etahis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/eta.dat')
etahis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/eta.dat')
etahis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/eta.dat')
etahis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaGiro/eta.dat')

axl = [0, 800, 1, 5]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$\eta\prime$'
    xetalabel = r'$t\prime$'
else:
    ylabel = r'$\eta$'    
    xetalabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(etahis[:, 0],  etahis[:, 1],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(etahis2[:, 0],  etahis2[:, 1],  color = bc,linestyle = bs,
linewidth = 2, label=ur'1.2beta')
plt.scatter(somep(etahis3[:, 0], num = 200), somep(etahis3[:, 1], num =
200), 
color = rc, marker = rs, s = 8, label=ur'1.2r')
plt.scatter(somep(etahis4[:, 0], num = 100),  somep(etahis4[:, 1], num =
100), 
color = lc, marker = ls, s = 20, label=ur'1.2leme')
plt.scatter(somep(etahis5[:, 0], num = 100), somep(etahis5[:, 1], num =
100), 
color = brlc, marker = brls, s = 14, label=ur'1.2brl')
plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xetalabel)
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
