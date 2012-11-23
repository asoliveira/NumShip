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

def qtdf (arq, scgarq, diretorio, qtd=1, derivada = None, multi=None):
  """Esta função faz a simulação em si"""
  if '~' in arq:
    return
         
  if qtd == 1 or qtd == 2:
    arqrel = arq.split('.')[0]
  elif qtd == 3:
    arqrel =  derivada + '/' + arq.split('.')[0] + '/' + str(multi) 
  elif qtd == 4:
    arqrel =  str(multi) + '/' + arq.split('.')[0] + '/' + derivada    
  elif qtd == 5:
    arqrel = arq.split('.')[0] + '_bench'
  scgarq += '/' + arqrel + '/giro'
  scgarq = os.path.abspath(scgarq) 
         
  #Arquivo de derivadas hidrodinâmicas
  arq = os.path.abspath(diretorio + arq)

  execfile('./scripts/inteCurvaGiro.py', globals(), locals())
  print 'simulado dados da curva de Giro do arquivo'
  print arq
  print arqrel
  
  os.chdir(os.getcwd().split(scgarq_raiz)[0])
  if plot:
    print 'Plotando ' + arqrel
    execfile('./scripts/plotCurvaGiro.py', globals(), locals())
    print'Plotagem realizada'

    
  #Copiando alguns arquivos de configuração e dados para registro
  shutil.copyfile('./script-teste/relcg.py', scgarq + '/relcg.py')
  shutil.copyfile(arq, scgarq + '/../' + arq.split('/')[-1])
  shutil.copyfile('./dados/config.py', scgarq + '/config.py')
  
  if qtd != 4:
    i = '/' + arq.split('/')[-1].split('.')[0] + '_cg.dat'
    if os.path.exists(benchpasta+i):
      shutil.copyfile(benchpasta + i, scgarq + i)
  
  if qtd ==3 or qtd==4:
    bench = scgarq.split(arqrel)[0] + '/' + arq.split('/')[-1].split('.')[0]+'_bench'
    bench = bench.replace('//', '/')
    if os.path.exists(bench):
      if os.path.exists(scgarq +  '/../../' + 
      arq.split('/')[-1].split('.')[0] + '_bench'):
        if not os.path.exists(scgarq +  '/../../' + 
        arq.split('/')[-1].split('.')[0] + '_bench/giro'):        
          shutil.copytree(bench + '/giro' ,scgarq + '/../../' + 
          arq.split('/')[-1].split('.')[0] + '_bench/giro')
      else:
        shutil.copytree(bench, scgarq + '/../../' + 
        arq.split('/')[-1].split('.')[0] + '_bench')
    
  os.chdir(scgarq)  
  execfile('relcg.py')
  os.chdir(os.getcwd().split(scgarq_raiz)[0])
  
    
print 'Início da simulação da Curva de Giro ...'
if qtd == 1:
  qtdf(arq, scgarq, diretorio, qtd)
elif qtd == 2:
  for arq in os.listdir(diretorio):
    qtdf(arq, scgarq, diretorio, qtd)
elif qtd == 3 or qtd == 4:
  lder = os.listdir(diretorio)
  for arq in lder:
    qtdf(arq, scgarq, diretorio, qtd=5)
    for multi in multiplicador:
      for derivada in ele:
        qtdf(arq, scgarq, diretorio, qtd, derivada, multi)
    
print 'Integração Realizada.\n'

#cwd '/home/alex/estudo/ufrj/mestrado/dissertacao/WorkingCopy/branches'
os.chdir(os.getcwd().split(scgarq_raiz)[0])
if qtd == 3 or qtd == 4:
  ldir = os.listdir('./'+scgarq_raiz)
  for sdir in ldir:
    #no qtd=3 ou 4 não existem estas pastas do 'diretorio' na pasta raiz. 
    #A não o benchmak.
    if sdir + '.dat' in os.listdir(diretorio):
      ldir.remove(sdir)
  for sdir in ldir:
    if 'bench' not in sdir:
      ldir2 = os.listdir('./'+scgarq_raiz+ '/' +sdir)
      for sdir2 in ldir2:
        caminhosdir = './' + scgarq_raiz + '/' + sdir + '/' + sdir2
        if os.path.isdir(caminhosdir):
          shutil.copyfile('./script-teste/plotp.py',caminhosdir + '/plotp.py')
          os.chdir(caminhosdir)
          if plot:
            execfile('plotp.py')
        os.chdir(os.getcwd().split(scgarq_raiz)[0])
elif qtd == 1 or qtd == 2:
  os.chdir(os.getcwd().split(scgarq_raiz)[0])
  if not os.path.isfile('plotp.py'):
    shutil.copyfile('./script-teste/plotp.py', scgarq_raiz + '/plotp.py')
  os.chdir(scgarq_raiz)  
  if plot:
    execfile('plotp.py')
    
os.chdir(os.getcwd().split(scgarq_raiz)[0])


#print'Fazendo o relatório..'
#execfile('./scripts/relatoriocg.py',  locals())
#print'Relatório feito.'
#print 'Simulação e relatório realizados. Dê uma olhada na pasta \
#"saida<data_hora>".\n'
