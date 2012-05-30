# -*- coding: utf-8 -*-
   
import sys
import os

sys.path.append('./AnalisaNavio/')

import scipy as sp
import matplotlib.pyplot as plt
from Es import *
from Navio import *


######################3
##
##
##
##
##
#####################

nome = 'B MarAd'
save = True
formato = 'eps'
TipoModelo = 'MARAD'
GrausDeLib = 3
escala = '0.7'
#################3

Multbeta = 1.*sp.array([1., 1.,1. ]) 
Multr =  1.*sp.array([1.,1.,1.]) 
Multl = 1.*sp.array([1.,1.,1. ]) 
Multbrl = 1.*sp.array([1.,1.,1. ])


######################3
##
##
##
##
##
#####################
p = ( Multbeta,  Multr,  Multl,  Multbrl)
if TipoModelo== 'MARAD':
    Arq =  './dados/MarAdinputder.dat'
elif   TipoModelo== 'TP':  
    Arq =  './dados/TPinputder.dat'



In = ('Navioteste', Arq, 'inputtab.dat')
io = es(entrada = In)

DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )

saida = navio1.simulaTestb(p = p)

dir= './figuras/testes/'
os.makedirs(dir)

plt.plot(saida[:,0]*180/sp.pi,  saida[:,1])
plt.ylabel(r'$F_x$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Fxbeta.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
    
    
plt.plot(saida[:,0]*180/sp.pi,  saida[:,2])
plt.ylabel(r'$F_y$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Fybeta.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()     
    
    
    
plt.plot(saida[:,0]*180/sp.pi, saida[:,3])
plt.ylabel(r'$K$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Kbeta.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()     

plt.plot(saida[:,0]*180/sp.pi,  saida[:,4])
plt.ylabel(r'$N$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Nbeta.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

execfile('./script/relatorioteste.py')
