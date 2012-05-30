# -*- coding: iso-8859-1 -*-
   
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
formato = 'png'
TipoModelo = 'MARAD'
GrausDeLib = 3

#################3

MultFx = sp.array(1.3)
MultFy = sp.array(1.3)
MultK = sp.array(1.3)
MultN = sp.array(1.3)
######################3
##
##
##
##
##
#####################

if TipoModelo== 'MARAD':
    Arq =  './dados/MarAdinputder.dat'
elif   TipoModelo== 'TP':  
    Arq =  './dados/TPinputder.dat'



In = ('Navioteste', Arq, 'inputtab.dat')
io = es(entrada = In)

DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )

saida = navio1.simulaTestb()

dir= './figuras/testes/' + TipoModelo + '/' 
os.makedirs(dir)

plt.plot(saida[:,0]*180/sp.pi,  MultFx*saida[:,1])
plt.ylabel(r'$F_x$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Fxbeta' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
    
    
plt.plot(saida[:,0]*180/sp.pi,  MultFy*saida[:,2])
plt.ylabel(r'$F_y$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Fybeta' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()     
    
    
    
plt.plot(saida[:,0]*180/sp.pi,  MultK*saida[:,3])
plt.ylabel(r'$K$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Kbeta' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()     

plt.plot(saida[:,0]*180/sp.pi,  MultN*saida[:,4])
plt.ylabel(r'$N$')
plt.xlabel(r'$\beta$ graus')

if save:
    plt.savefig(dir + TipoModelo +'Nbeta' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
