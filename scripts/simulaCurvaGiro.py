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

print 'Início da simulação da Curva de Giro ...\n'
execfile('./scripts/inteCurvaGiro.py',  globals())
print 'Integração Realizada.\n'
if plot:
  execfile('./scripts/plotCurvaGiro.py',  locals())
  print'plotagem realizada'
print'Fazendo o relatório...\n'
execfile('./scripts/relatoriocg.py',  locals())
print'Relatório feito.'
print 'Simulação e relatório realizados. Dê uma olhada na pasta \
"saida<data_hora>".\n'
