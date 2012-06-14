#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#This file is part of a program called NumShip

#Copyright (C) 2011,2012  Alex Sandro Oliveira

#NumShip is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


print '------------------'
print"NumShip  Copyright (C) 2011, 2012  Alex Sandro Oliveira\n\
This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.\n\
This is free software, and you are welcome to redistribute it\n\
under certain conditions.\n"

#Imports
import os
import sys


r1=raw_input("aperte ENTER para continuar\n")

if r1 == "show w":
  arq=open("COPYING", "r")
  sys.stdout.write(arq.read())
  r1=raw_input("aperte ENTER para continuar\n")
  del arq, r1
 

#Coloque aqui todos os diretórios em os módulos estam.
sys.path.insert(0, os.path.abspath('source'))
sys.path.insert(0, os.path.abspath('scripts'))
sys.path.insert(0, os.path.abspath('dados'))

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
Coloque a sua resposta separada por vírgulas. Exemplo:\n\
1,2,3\n')

#Esta variável somente será verdadeira quando a resposta estiver
#nos padrões exigidos
aprovar=False
while not aprovar:
  r=r.split(',')
  for i in r:
    if not i.isdigit():
      r=raw_input('Estamos detectando que você:\nDigitou letras ao invés \
dos números indicados;Ou \nEsqueceu de colocar a vírgula entre as \
suas escolhas.\nTente digitar novamente as opções:\n\
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


