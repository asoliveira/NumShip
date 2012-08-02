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
#Qual o titulo do gráfico?
titulo = 'Curva de Giro'

import os

import scipy as sp
import matplotlib.pyplot as plt


        
poshis = sp.genfromtxt('entrada/padrao/CurvaGiro/pos.dat')
poshis2 = sp.genfromtxt('entrada/leme/saida1.1/CurvaGiro/pos.dat')
poshis3 = sp.genfromtxt('entrada/leme/saida1.2/CurvaGiro/pos.dat')
poshis4 = sp.genfromtxt('entrada/leme/saida1.3/CurvaGiro/pos.dat')

axl = [-10, 1100, 0, 1000]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$x\prime$'
    xposlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xposlabel = r'$y \quad m$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
plt.plot(poshis[:, 2],  poshis[:, 1],  'b-', 
label=ur'padrão')
plt.plot(poshis2[:, 2],  poshis2[:, 1],  'g-',
label=ur'1.1leme')
plt.plot(poshis3[:, 2],  poshis3[:, 1],  'r-',
label=ur'1.2leme')
plt.plot(poshis4[:, 2],  poshis4[:, 1],  'k-',
label=ur'1.3leme')
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
