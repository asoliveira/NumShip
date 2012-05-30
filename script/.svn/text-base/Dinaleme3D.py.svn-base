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
from Leme import  *
from Navio import *

TipoModelo = 'MARAD'
umin = 2
nmin = 0.3
passo = 40
lemeCom = 1*(sp.pi/180) #rad
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
navio1.leme.MudaLemeDir(sp.array([lemeCom]))

umax = DicionarioDerivadas['unom']
uc = DicionarioDerivadas['unom']
nmax =  DicionarioDerivadas['rotnom']
##
##
##  criando o arquivo de sa�da
##
######################
os.makedirs('./saida/')
os.chdir('./saida')
lemeDina = open('Dinaleme3D.dat',  'w')#historico do leme
lemeDina.write('#Navio ' + nome + '\n' +  '#Manobra de Curva Giro\n#\n') 
lemeDina.write('#Dinamica da do leme\n')
lemeDina.write('#Rot='+  str(DicionarioDerivadas['rotnom']) +  '\t' +  'Dp=' +  str(DicionarioDerivadas['dp'])+ '\n' )
lemeDina.write('#leme=' + str(lemeCom)+ '\n')
lemeDina.write('#u'.rjust(5) + 'Rot'.rjust(5) + 'eta'.rjust(5) + 'FX'.rjust(8) + 'FY'.rjust(8) + 'N'.rjust(8) + '\n')  


for u in sp.linspace(umin,  umax,  passo ):
  for rot in sp.linspace(nmin, nmax, passo):
    navio1.MudaVel(sp.array([[u],  [0], [0], [0], [0], [0]]))
    eta = uc/u
    lemeDina.write('%.2f'.rjust(5)%(u) + ' ')
    lemeDina.write('%.2f'.rjust(5)%(rot) + ' ')
    lemeDina.write('%.2f'.rjust(5)%(eta) + ' ')
    lemeDina.write('%.2f'.rjust(8)%(navio1.leme.Fx(rot, eta)) + ' ')
    lemeDina.write('%.2f'.rjust(8)%(navio1.leme.Fy(rot)) + ' ')
    lemeDina.write('%.2f'.rjust(8)%(navio1.leme.N(rot)) + ' ')
    lemeDina.write('\n')
  
lemeDina.close()
