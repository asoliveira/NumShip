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
nome = 'beta-pos-zz'
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
        
poshis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/pos.dat')
poshis2 = sp.genfromtxt('../entrada/beta/saida1.1/CurvaZigZag/pos.dat')
poshis3 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaZigZag/pos.dat')
poshis4 = sp.genfromtxt('../entrada/beta/saida1.3/CurvaZigZag/pos.dat')

axl = [00, 4000, -50, 600]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$y\prime$'
    xposlabel = r'$x\prime$'
else:
    ylabel = r'$y \quad m$'    
    xposlabel = r'$x \quad m$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(poshis[:, 1],  poshis[:, 2],  color = pc, linestyle = ps,
linewidth = 1, label=ur'padrão')
plt.plot(poshis2[:, 1],  poshis2[:, 2],  color = r1c,linestyle = r1s,
linewidth = 1, label=ur'1.1beta')
plt.plot(poshis3[:, 1], poshis3[:, 2], color = r2c, linestyle = r2s, 
linewidth = 1, label = ur'1.2beta')
plt.plot(poshis4[:, 1], poshis4[:, 2], color = r3c, linestyle = r3s, 
linewidth = 1, label= ur'1.3beta')
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
