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
nome = 'velo-u-zz'
#Qual título colocar no gráficos?
titulo = ''#'Curva de ZigZag'
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
        
velohis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/velo.dat')
velohis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaZigZag/velo.dat')
velohis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaZigZag/velo.dat')
velohis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaZigZag/velo.dat')
velohis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaZigZag/velo.dat')

axl = [0, 1500, 4, 8.5]

#Plotando a Curva de ZigZag      
if adi:
    ylabel = r'$u\prime$'
    xvelolabel = r'$t\prime$'
else:
    ylabel = r'$u \quad m/s$'    
    xvelolabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(velohis[:, 0],  velohis[:, 1],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(velohis2[:, 0],  velohis2[:, 1],  color = bc,linestyle = bs,
linewidth = 2, label=ur'1.2beta')
plt.scatter(somep(velohis3[:, 0], num = 200), somep(velohis3[:, 1], num =
200), 
color = rc, marker = rs, s = 8, label=ur'1.2r')
plt.scatter(somep(velohis4[:, 0], num = 100),  somep(velohis4[:, 1], num =
100), 
color = lc, marker = ls, s = 20, label=ur'1.2leme')
plt.scatter(somep(velohis5[:, 0], num = 100), somep(velohis5[:, 1], num =
100), 
color = brlc, marker = brls, s = 14, label=ur'1.2brl')
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
