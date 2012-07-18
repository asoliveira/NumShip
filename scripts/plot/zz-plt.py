#!/usr/bin/env python
# -*- coding: utf-8 -*-

#É adimensional?
adi = False
#É para salvar as figuras(True|False)?
save = False
#Caso seja para salvar, qual é o formato desejado?
formato = 'jpg'
#Caso seja para salvar, qual é o diretório que devo salvar?
dircg = 'fig-sen'
#Caso seja para salvar, qual é o nome do arquivo?
nome = 'cg'
#Qual o titulo
titulo = 'Curva de Zig Zag'

import os

import scipy as sp
import matplotlib.pyplot as plt
        
poshis = sp.genfromtxt('../entrada/padrao/CurvaZigZag/pos.dat')
poshis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaZigZag/pos.dat')
poshis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaZigZag/pos.dat')
poshis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaZigZag/pos.dat')
poshis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaZigZag/pos.dat')

axl = [0, 1000, -40, 40]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$\psi$'
    xposlabel = r'$t$'
else:
    ylabel = r'$\psi$'
    xposlabel = r'$t$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
plt.plot(poshis[:, 0],  poshis[:, 6] * (180 / sp.pi),  'b-', 
label=ur'padrão')
plt.plot(poshis2[:, 0],  poshis2[:, 6] * (180 / sp.pi),  'g-',
label=ur'1.2beta')
plt.plot(poshis3[:, 0],  poshis3[:, 6] * (180 / sp.pi),  'r-',
label=ur'1.2r')
plt.plot(poshis4[:, 0],  poshis4[:, 6] * (180 / sp.pi),  'k-',
label=ur'1.2leme')
plt.plot(poshis5[:, 0],  poshis5[:, 6] * (180 / sp.pi),  'm-',
label=ur'1.2brl')
plt.title(titulo)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
plt.axis(axl)
plt.grid(True)

if save:
    try:
        os.makedirs(dircg)
    except NameError:
        print 'houve algum problema na criação do diretório ' + dircg
    plt.savefig(dircg + '/' + nome + '.' + formato ,  format=formato)
else:    
    plt.show()           
