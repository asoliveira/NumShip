# -*- coding: utf-8 -*-


print '------------------'

import os
import sys

os.chdir(sys.path[0])
os.chdir('..')

import sys

sys.path.append('./AnalisaNavio/')

import scipy as sp
from Es import *
from Navio import *

TipoModelo = 'MARAD'
umin = 2
passo = 40
uc = None
nome = 'tete'
if TipoModelo== 'MARAD':
    Arq =  './dados/MarAdinputder.dat'
elif   TipoModelo== 'TP':  
    Arq =  './dados/TPinputder.dat'



In = ('Navioteste', Arq, 'inputtab.dat')
io = es(entrada = In)

DicionarioDerivadas = io.lerarqder()
del io,  In,  Arq

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )





##
##
##  criando o arquivo de sa�da
##
######################
os.makedirs('./saida/')
os.chdir('./saida')
propDina = open('DinaRT2D.dat',  'w')#historico do leme
propDina.write('#Navio ' + nome + '\n' +  '#Manobra de Curva Giro\n#\n') 
propDina.write('#Dinamica do Propulsor\n')
propDina.write('#'+'uc=' +  str(uc)+ '\n' )
propDina.write('#u'.rjust(5) + 'eta'.rjust(5) + 'FX'.rjust(8) + 'FY'.rjust(8) + 'N'.rjust(8) + '\n')  

if uc == None:
  uc = DicionarioDerivadas['unom']
uc = sp.array([uc])
umax = DicionarioDerivadas['unom']
navio1.MudaVelCom(uc)

for u in sp.linspace(umin,  umax,  passo ):
    navio1.MudaVel(sp.array([[u],  [0], [0], [0], [0], [0]]))
    eta = uc/u
    propDina.write('%.2f'.rjust(5)%(u) + ' ')
    propDina.write('%.2f'.rjust(5)%(eta) + ' ')
    propDina.write('%.2f'.rjust(8)%(navio1.prop.Fx()))
    propDina.write('%.2f'.rjust(8)%(navio1.prop.Fy()))
    propDina.write('%.2f'.rjust(8)%(navio1.prop.N()) )
    propDina.write('\n')
  
propDina.close()
