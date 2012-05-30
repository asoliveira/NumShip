# -*- coding: utf-8 -*-
   
import sys

sys.path.append('./source/')
#sys.path.append('/home/alex/.MySys/lib/python')

import scipy as sp
from Es import *
from Leme import  *
from Prop import *
from Casco import *
from Navio import *


nome = 'B MarAd'
save = True
formato = 'eps'
passo = 0.7
tmax = 3000
tini =  0
metodo = 'rk4'
TipoModelo = 'MARAD'
GrausDeLib = 3
LemeCom= sp.array(35.)
ForEs = 1e0#Multiplicador da força
Overshoot = 35
escala = '0.7'
Rot = sp.array(0.62)
tipoc = 'starboard'
saida = 'txt'
adi = False



Multbeta = 1.*sp.array([1., 1.,1.]) 
Multr =  1.*sp.array([1., 1.,1. ])
Multl = 1.*sp.array([1.,1.,1. ]) 
Multbrl = 1.*sp.array([1.,1.,1. ])

##############################################
##
##
##
##
##
####################################################################

print 'Curva de Giro'

execfile('./script/inteCurvaGiro.py',  locals())

print 'Integracao Realizada'

#execfile('./script/plotCurvaGiro.py',  locals())

#print'plotagem realizada'


execfile('./script/relatoriocg.py',  locals())

print'Relatório feito'

print 'Terminado a simulação da curva de Giro'
