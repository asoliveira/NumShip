#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '------------------'

import os
import sys


#Coloque aqui todos os diretórios em os módulos estam.
sys.path.insert(0, os.path.abspath('source'))
sys.path.insert(0, os.path.abspath('script'))

#Constantes que serão enviadas para o arquivo padrão
DIRETORIO=()
SIMULACOES=()

#Inicio do script
print 'Os diretórios no sys.path(não constam aqui os diretórios padrões):'
for i in range(3):
   print sys.path[i], '\n'

men1='Deseja adicionar mais algum diretório?[s/n]\n'
r1=raw_input(men1)

while (r1 == 's') :
  inputdir=raw_input('Digite ele...\n')
  inputdir=os.path.abspath(inputdir)
  
  while (not os.path.exists(inputdir)) and (inputdir!='n'):
    mensagem='Este diretório consta como inexistente.\nTente confirmar \
a digitação e colocar o caminho absoluto do diretório (desde da \
raiz).\nDigite n caso não queira colocar mais outro diretório.\n'
    inputdir=raw_input(mensagem)
    del mensagem
   
    
  if ((not ((inputdir in sys.path) or (inputdir in DIRETORIO)))and 
  (not (inputdir == 'n'))):
    tinputdir=inputdir,
    DIRETORIO=DIRETORIO + tinputdir
    print 'Diretório ' + inputdir + ' acrescentado.'
  else:
    if inputdir != 'n':
      print 'Não se preocupe! O diretório\n' + inputdir + '\njá está no \n\
sys.path ou foi inserido por você como diretório a ser colocado por meio\n\
deste script.'
  
  r1=raw_input(men1)

  
#Sobre as simulações que serão rodadas
r=raw_input('Quais são as simulações que devem ser rodadas?\n\
[1] Curva de Giro, [2] Curva de ZigZag\n\
Coloque a sua resposta separada por virgulas. Exemplo:\n\
1,2,3\n')

#Esta variável somente será verdadeira quando a resposta estiver
#nos padrões exigidos
aprovar=False
while not aprovar:
  r=r.split(',')
  for i in r:
    if not i.isdigit():
      r=raw_input('Estamos detectando que você:\nDigitou letras ao invés dos \
números indicados;Ou \nEsqueceu de colocar a vírgula entre as suas \
escolhas.\nTente digitar novamente as opções:\n\
[1] Curva de Giro, [2] Curva de ZigZag\n\
Coloque a sua resposta separada por vírgulas. Exemplo:\n\
1,2,3\n')
    else:
      aprovar=True

SIMULACOES=tuple(r)

del men1,r1,r,aprovar


#Saida
print 'Simulações=' + str(SIMULACOES), 'DIRETORIO=' + str(DIRETORIO)


for i in DIRETORIO:
  print i, 
  sys.path.insert(0,i)

if '1' in SIMULACOES:
  import simulaCurvaGiro

if '2' in SIMULACOES:
  import simulaZigZag

#execfile(os.path.abspath('simulaTeste.py'))
