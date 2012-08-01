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
nome = 'r-acel-u-zz'
#Qual título colocar no gráficos?
titulo = ''#'Curva de ZigZag'
titulo2=''
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
        
acelhis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/acel.dat')
acelhis2 = sp.genfromtxt('../entrada/r/saida1.1/CurvaZigZag/acel.dat')
acelhis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaZigZag/acel.dat')
acelhis4 = sp.genfromtxt('../entrada/r/saida1.3/CurvaZigZag/acel.dat')

lemehis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/leme.dat')
lemehis2 = sp.genfromtxt('../entrada/r/saida1.1/CurvaZigZag/leme.dat')
lemehis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaZigZag/leme.dat')
lemehis4 = sp.genfromtxt('../entrada/r/saida1.3/CurvaZigZag/leme.dat')

axl = [0, 1000, -0.025, 0.01]
axl2 = [0, 1000, -25, 25]#do leme
#Plotando a Curva de Giro      
if adi:
    ylabel = r'$t\prime$'
    xacellabel = r'$\dot u\prime$'
else:
    ylabel = r'$\dot u \quad m/s^2$'    
    xacellabel = r'$t \quad segundos$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
#Padrao
plt.plot(acelhis[:, 0],  acelhis[:, 1],  color = pc, linestyle = ps,
linewidth = 2, label=ur'padrão')

plt.plot(acelhis2[:, 0],  acelhis2[:, 1],  color = r1c,linestyle = r1s,
linewidth = 2, label=ur'1.1--$r$')

plt.plot(acelhis3[:, 0], acelhis3[:, 1], color = r2c, linestyle = r2s,
linewidth = 2, label=ur'1.2--$r$')

plt.plot(acelhis4[:, 0], acelhis4[:, 1], color = r3c, linestyle = r3s,
linewidth = 2, label=ur'1.3--$r$')

plt.title(titulo)
plt.legend(bbox_to_anchor=(1.1, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xacellabel)
plt.axis(axl)
plt.grid(True)

plt.twinx()
plt.plot(lemehis[:, 0],  lemehis[:, 1] * (180/sp.pi),  color = pc, linestyle = "--",
linewidth = 1, label=ur'leme--padrão')
plt.plot(lemehis2[:, 0],  lemehis2[:, 1] * (180/sp.pi),  color = r1c, linestyle = "--",
linewidth = 1, label=ur'leme--1.1$r$')
plt.plot(lemehis3[:, 0],  lemehis3[:, 1] * (180/sp.pi),  color = r2c, linestyle = "--",
linewidth = 1, label=ur'leme--1.2$r$')
plt.plot(lemehis4[:, 0],  lemehis4[:, 1] * (180/sp.pi),  color = r3c, linestyle = "--",
linewidth = 1, label=ur'leme--1.3$r$')

plt.title(titulo2)
plt.legend(bbox_to_anchor=(1.1, 0), loc=3, borderaxespad=0.)
plt.ylabel(r"$\delta_R$")
plt.axis(axl2)
plt.grid(False)

if save:
    if not os.path.exists(dircg):
        os.makedirs(dircg)
    if os.path.exists(dircg + '/' + nome + '.' + formato):
        os.remove(dircg + '/' + nome + '.' + formato)
    plt.savefig(dircg + '/' + nome + '.' + formato ,  format=formato)
else:    
    plt.show()           
