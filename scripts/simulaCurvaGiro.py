# -*- coding: utf-8 -*-
   

#Módulos que vem com python
import sys
import shutil
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
scgarq='./saida_' + data.strftime(fdata) 
if not os.path.exists(scgarq):
  os.mkdir(scgarq)
  
if not os.path.isfile(scgarq + '/plotp.py'):
  shutil.copyfile('script-teste/plotp.py', scgarq + '/plotp.py')

def qtd2 (arq, scgarq):
    if '~' in arq:
      return
            
    arqrel = arq
    scgarq += '/' + arq.split('.')[0] + '/giro'
    scgarq = os.path.abspath(scgarq) 
           
    #Arquivo de derivadas hidrodinâmicas
    arq = os.path.abspath('./dados/derivadas/'+ arq)

    execfile('./scripts/inteCurvaGiro.py', globals(), locals())
    os.chdir('..')    
    pass

print 'Início da simulação da Curva de Giro ...'

if qtd == 1:
  arqrel = arq
  scgarq += '/' + arq + '/giro'
  scgarq = os.path.abspath(scgarq)
  #Arquivo de derivadas hidrodinâmicas
  arq = os.path.abspath('./dados/derivadas/'+arq) 

  execfile('./scripts/inteCurvaGiro.py',  globals(), locals())
  os.chdir('..')
elif qtd == 2:
  diretorio = os.path.abspath('./dados/derivadas/')
  for arq in os.listdir(diretorio):
    qtd2(arq, scgarq)

print 'Integração Realizada.\n'

os.chdir(scgarq)
execfile('plotp.py')
os.chdir('..')
#if plot:
  #execfile('./scripts/plotCurvaGiro.py',  locals())
  #print'Plotagem realizada'
#print'Fazendo o relatório..'
#execfile('./scripts/relatoriocg.py',  locals())
#print'Relatório feito.'
#print 'Simulação e relatório realizados. Dê uma olhada na pasta \
#"saida<data_hora>".\n'
