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
nome = 'r-acel-v-cg'
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
        
acehis = sp.genfromtxt('../entrada/padrao/CurvaGiro/acel.dat')
acehis2 = sp.genfromtxt('../entrada/r/saida1.1/CurvaGiro/acel.dat')
acehis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/acel.dat')
acehis4 = sp.genfromtxt('../entrada/r/saida1.3/CurvaGiro/acel.dat')

axl = [0, 1000, -0.04, 0.007]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xacelabel = r'$\dot v\prime$'
else:
    ylabel = r'$\dot v \quad m/s^2$'    
    xacelabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acehis[:, 0],  acehis[:, 2],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(acehis2[:, 0],  acehis2[:, 2],  color = r1c,linestyle = r1s,
linewidth = 1, label=ur'1.1r')
plt.plot(acehis3[:, 0], acehis3[:, 2], color = r2c, linewidth = 1, 
linestyle = r2s, label=ur'1.2r')
plt.plot(acehis4[:, 0], acehis4[:, 2],color = r3c, linestyle = r3s, 
linewidth = 1, label=ur'1.3r')
plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xacelabel)
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
