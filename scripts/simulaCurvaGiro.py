# -*- coding: utf-8 -*-
   

#Módulos que vem com python
import sys
#Módulos de terceiros
import scipy as sp
import datetime
#Módulos criados para o NumShip
from Es import *
from Leme import  *
from Prop import *
from Casco import *
from Navio import *
from config import * #parâmetros para configurar a simulação

#Formato do arquivo de saída
data=datetime.datetime.now()
scgarq='./saida_' + data.strftime(fdata) + '/CurvaGiro'

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

execfile('./scripts/inteCurvaGiro.py',  locals())

print 'Integracao Realizada'

#execfile('./scripts/plotCurvaGiro.py',  locals())

#print'plotagem realizada'


execfile('./scripts/relatoriocg.py',  locals())

print'Relatório feito'

print 'Terminado a simulação da curva de Giro'
