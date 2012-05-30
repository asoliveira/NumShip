# -*- coding: utf-8 -*-
   
import sys

sys.path.append('./source/')

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
LemeCom= sp.array(20.)
Proa = sp.array(20.)
ForEs = 1e0
Overshoot = 35
Rot = sp.array(0.62)
saida = 'txt'
tipoc = 'starboard'
adi = False
escala = '0.7'

####################################################




Multbeta = 1.1*sp.array([1., 1.,1. ]) 
Multr =  1.*sp.array([1., 1.,1. ])
Multl = 1.*sp.array([1.,1.,1. ]) 
Multbrl = 1.*sp.array([1.,1.,1. ])

###################################################


print  'Curva de ZigZag'

execfile('./script/inteZigZag.py',  locals())

print 'Integração Realizada'

#execfile('./script/plotZigZag.py',  locals())

#print'plotagem realizada'

execfile('./script/relatoriozz.py',  locals())

print'Relatório feito'

print 'Terminado a simulação da curva de ZigZag'
