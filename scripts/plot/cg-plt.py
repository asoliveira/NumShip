#!/usr/bin/env python
# -*- coding: utf-8 -*-

#É adimensional?
adi = False
#É para salvar as figuras(True|False)?
save = True
#Caso seja para salvar, qual é o formato desejado?
formato = 'pdf'
#Caso seja para salvar, qual é o diretório que devo salvar?
dircg = 'fig-sen'
#Caso seja para salvar, qual é o nome do arquivo?
nome = 'cg'

import os

import scipy as sp
import matplotlib.pyplot as plt

        
poshis = sp.genfromtxt('../entrada/padrao/CurvaGiro/pos.dat')
poshis2 = sp.genfromtxt('../entrada/beta/saida1.2/CurvaGiro/pos.dat')
poshis3 = sp.genfromtxt('../entrada/r/saida1.2/CurvaGiro/pos.dat')
poshis4 = sp.genfromtxt('../entrada/leme/saida1.2/CurvaGiro/pos.dat')
poshis5 = sp.genfromtxt('../entrada/brl/saida1.2/CurvaGiro/pos.dat')

#Qual a cor dos gráficos?
pc = 'r-'
bc = 'g-'
lc = 'b-'
brlc = 'y-'
rc = 'm-'

axl = [0, 1200, -100, 1300]

#Plotando a Curva de Giro      
if adi:
    ylabel = r'$x\prime$'
    xposlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xposlabel = r'$y \quad m$'    

plt.subplot2grid((1,4),(0,0), colspan=3)
plt.plot(poshis[:, 2],  poshis[:, 1],  pc, 
label=ur'$M1$')
plt.plot(poshis2[:, 2],  poshis2[:, 1],  bc,
label=ur'1.2$\beta$')
plt.plot(poshis3[:, 2],  poshis3[:, 1],  rc,
label=ur'1.2r')
plt.plot(poshis4[:, 2],  poshis4[:, 1],  lc,
label=ur'1.2$\delta_R$')
plt.plot(poshis5[:, 2], poshis5[:, 1], 
brlc, label=ur'1.2brl')
plt.title('Curva de Giro')
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
