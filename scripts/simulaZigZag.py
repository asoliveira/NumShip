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
scgarq_raiz= scgarq[2:]

if not os.path.exists(scgarq):
  os.mkdir(scgarq)
  
def qtd2 (arq, scgarq, diretorio, perce=None, i=None):
  """Esta função faz a simulação em si"""
  if '~' in arq:
    return
         
  if perce != None:
    arqrel =  perce + '/' + str(i) + arq.split('.')[0] 
  else:
    arqrel = arq.split('.')[0]
    
  scgarq += '/' + arqrel + '/zigzag'
  scgarq = os.path.abspath(scgarq) 
         
  #Arquivo de derivadas hidrodinâmicas
  arq = os.path.abspath(diretorio + arq)

  execfile('./scripts/inteZigZag.py', globals(), locals())
  print 'simulado dados do arquivo'
  print arq
  print arqrel
  
  os.chdir(os.getcwd().split(scgarq_raiz)[0])
  if plot:
    print 'Plotando ' + arqrel
    execfile('./scripts/plotZigZag.py', globals(), locals())
    print'Plotagem realizada'

    
  #Copiando alguns arquivos de configuração e dados para registro
  shutil.copyfile('./script-teste/relzz.py', scgarq + '/relzz.py')
  shutil.copyfile(arq, scgarq + '/../' + arq.split('/')[-1])
  shutil.copyfile('./dados/config.py', scgarq + '/config.py')
  i = '/' + arq.split('/')[-1].split('.')[0] + '_zz.dat'

  if os.path.exists(benchpasta+i):
    shutil.copyfile(benchpasta + i, scgarq + i)
  
  os.chdir(scgarq)  
  execfile('relzz.py')
  os.chdir(os.getcwd().split(scgarq_raiz)[0])

print 'Início da simulação da Curva de Giro ...'
if qtd == 1:
  qtd2(arq, scgarq, diretorio)
elif qtd == 2:
  for arq in os.listdir(diretorio):
    #if len(multiplicador) != 0 and len(multiplicador) != None:
      #for i in multiplicador:
        #for derivada in ele:
          #qtd2(arq, scgarq, diretorio, derivada, i)
    #else:
    qtd2(arq, scgarq, diretorio)

    
    
print 'Integração Realizada.\n'

if 'derivada' in dir():
  for derivada in ele:
    os.chdir(os.getcwd().split(scgarq_raiz)[0])
    if not os.path.isfile(derivada + '/plotp.py'):
      shutil.copyfile('./script-teste/plotp.py', scgarq_raiz + '/' + derivada + '/plotp.py')
    os.chdir(os.getcwd().split(scgarq_raiz)[0] + '/' +scgarq_raiz + '/' + derivada)  
    execfile('plotp.py')
else:
  os.chdir(os.getcwd().split(scgarq_raiz)[0])
  if not os.path.isfile('plotp.py'):
    shutil.copyfile('./script-teste/plotp.py', scgarq_raiz + '/plotp.py')
  os.chdir(os.getcwd().split(scgarq_raiz)[0] + '/' + scgarq_raiz)  
  execfile('plotp.py')
    
os.chdir(os.getcwd().split(scgarq_raiz)[0])

#if plot:
  #execfile('./scripts/plotZigZag.py',  locals())
  #print'Plotagem realizada.'
#print'Fazendo o relatório...'
#execfile('./scripts/relatoriozz.py',  locals())
#print'Relatório feito.'
#print 'Simulação e relatório realizados. Dê uma olhada na pasta \
#"saida<data_hora>".\n'