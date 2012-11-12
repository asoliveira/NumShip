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
#data=datetime.datetime.now()
scgarq='./saida_' + data.strftime(fdata) + '/CurvaZigZag'

#Arquivo de derivadas hidrodinâmicas
arq = os.path.abspath('./dados/'+arq)

print 'Início da simulação da Curva de Zig-Zag ...\n'
execfile('./scripts/inteZigZag.py',  globals())
print 'Integração Realizada.'
#if plot:
  #execfile('./scripts/plotZigZag.py',  locals())
  #print'Plotagem realizada.'
#print'Fazendo o relatório...'
#execfile('./scripts/relatoriozz.py',  locals())
#print'Relatório feito.'
#print 'Simulação e relatório realizados. Dê uma olhada na pasta \
#"saida<data_hora>".\n'