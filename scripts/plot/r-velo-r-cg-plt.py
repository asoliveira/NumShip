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
nome = 'r-velo-r-cg'
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
        
velohis = sp.genfromtxt('../entrada/padrao/CurvaGiro/velo.dat')
velohis2 = sp.genfromtxt('../entrada/r/saida1.1/CurvaGiro/velo.dat')
velohis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/velo.dat')
velohis4 = sp.genfromtxt('../entrada/r/saida1.3/CurvaGiro/velo.dat')

axl = [0, 1000, 0, 0.8]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xveloabel = r'$r\prime$'
else:
    ylabel = r'$r \quad graus/s$'    
    xveloabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(velohis[:, 0],  velohis[:, 6] * (180 / sp.pi),  color = pc, 
linestyle = ps, linewidth = 1, label=ur'padrão')

plt.plot(velohis2[:, 0],  velohis2[:, 6] * (180 / sp.pi),  color = r1c,
linestyle= r1s, linewidth = 1, label=ur'1.1r')

plt.plot(velohis3[:, 0], velohis3[:, 6] * (180 / sp.pi), color = r2c, 
linewidth = 1, linestyle = r2s, label=ur'1.2r')

plt.plot(velohis4[:, 0], velohis4[:, 6] * (180 / sp.pi),color = r3c, 
linestyle = r3s, linewidth = 1, label=ur'1.3r')
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
