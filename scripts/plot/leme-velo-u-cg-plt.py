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
nome = 'leme-velo-u-cg'
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
        
acehis = sp.genfromtxt('../entrada/padrao/CurvaGiro/velo.dat')
acehis2 = sp.genfromtxt('../entrada/leme/saida1.1/CurvaGiro/velo.dat')
acehis3 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/velo.dat')
acehis4 = sp.genfromtxt('../entrada/leme/saida1.3/CurvaGiro/velo.dat')

axl = [0, 1000, 1, 9]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xveloabel = r'$u \prime$'
else:
    ylabel = r'$u \quad m/s$'    
    xveloabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acehis[:, 0],  acehis[:, 1],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(acehis2[:, 0],  acehis2[:, 1],  color = r1c,linestyle = r1s,
linewidth = 1, label=ur'1.1leme')
plt.plot(acehis3[:, 0], acehis3[:, 1], color = r2c, linewidth = 1, 
linestyle = r2s, label=ur'1.2leme')
plt.plot(acehis4[:, 0], acehis4[:, 1],color = r3c, linestyle = r3s, 
linewidth = 1, label=ur'1.3leme')
plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xveloabel)
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
