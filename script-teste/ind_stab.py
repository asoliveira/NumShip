#!/usr/bin/env python
# -*- coding: utf-8 -*--

#Script para calcular o índice de estabilidade.

import os
import sys
sys.path.insert(0, os.path.abspath('source'))
sys.path.insert(0, os.path.abspath('dados'))
from Es import *
from config import *

#caminho do arquivo de derivadas
entrada = 'dados/derivada.dat'

dados = es(('',entrada, ''))
dadosf = dados.lerarqder()

def calcind(dic):
  u"""Retorna o índice de estabilidade ou uma string de erro dos dados de
entrada
  """
  
  if dados.checkformat() != []:
    return 'problemas na formatação do arquivo ' + entrada
  
  s1 = -Multbeta[1]*dic['yv']*(dic['m']*dic['unom']*dic['xg'] -
  Multr[2]*dic['nr'])
  
  s2 = Multbeta[2]*dic['nv']*(dic['m']*dic['unom'] - Multr[1]*dic['yr'])
  
  #calculo do fator adimencionalisador 
  fadim = dic['unom']*(dic['rho']**2)*(dic['lpp']**5)
  
  return  fadim * (s1 + s2)

print 'O índice é -- %1.2e' %calcind(dadosf)
