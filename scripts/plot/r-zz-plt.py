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
nome = 'zz-r'
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
        
poshis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/pos.dat')
poshis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaZigZag/pos.dat')
poshis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaZigZag/pos.dat')
poshis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaZigZag/pos.dat')
poshis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaZigZag/pos.dat')

axl = [0, 8000, -40, 40]

#Plotando a Curva de ZigZag      
if adi:
    ylabel = r'$\psi \prime$'
    xposlabel = r'$x\prime$'
else:
    ylabel = r'$\psi graus$'    
    xposlabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(poshis[:, 1],  poshis[:, 6] * (180 / sp.pi),  color = pc, linestyle =
ps,
linewidth = 1, label=ur'padrão')
plt.plot(poshis2[:, 1],  poshis2[:, 6] * (180 / sp.pi),  color = bc,linestyle =
bs,
linewidth = 2, label=ur'1.2beta')
plt.scatter(somep(poshis3[:, 1], num = 200), somep(poshis3[:, 6] * (180 /
sp.pi), num = 200), 
color = rc, marker = rs, s = 8, label=ur'1.2r')
plt.scatter(somep(poshis4[:, 1], num = 200),  
somep(poshis4[:, 6] * (180 / sp.pi), num = 200), color = lc, marker = ls, s =
20,
label=ur'1.2leme')
plt.scatter(somep(poshis5[:, 1], num = 200), somep(poshis5[:, 6] * (180 /
sp.pi), num = 200), 
color = brlc, marker = brls, s = 14, label=ur'1.2brl')
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
