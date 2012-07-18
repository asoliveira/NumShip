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
nome = 'beta-velo-u-cg'
#Qual título colocar no gráficos?
titulo = ''#'Curva de Giro'
#Qual a cor dos gráficos?
pc = 'k'
r1c = 'k'
r2c = 'k'
r3c = 'k'
#Estilo de linha
ps = '-'
r1s = '-.'
r2s = '.'
r3s = '+'

import os

import scipy as sp
import matplotlib.pyplot as plt

from libplot import *
        
velohis = sp.genfromtxt('../entrada/padrao/CurvaGiro/velo.dat')
velohis2 = sp.genfromtxt('../entrada/beta/saida1.1/CurvaGiro/velo.dat')
velohis3 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/velo.dat')
velohis4 = sp.genfromtxt('../entrada/beta/saida1.3/CurvaGiro/velo.dat')

axl = [0, 1000, 1, 9]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xvelolabel = r'$u\prime$'
else:
    ylabel = r'$u \quad m/s$'    
    xvelolabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(velohis[:, 0],  velohis[:, 1],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(velohis2[:, 0],  velohis2[:, 1],  color = r1c,linestyle = r1s,
linewidth = 2, label=ur'1.1beta')
plt.scatter(somep(velohis3[:, 0], num = 200), somep(velohis3[:, 1], num =
200), 
color = r2c, marker = r2s, s = 8, label=ur'1.2beta')
plt.scatter(somep(velohis4[:, 0], num = 100), somep(velohis4[:, 1], num =
100), 
color = r3c, marker = r3s, s = 20, label=ur'1.3beta')
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
