#!/usr/bin/env python
# -*- coding: utf-8 -*--

#Script para plotar o balanço (1-t)T-R vs eta

import os
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.abspath('../source'))
sys.path.insert(0, os.path.abspath('../dados'))
from Es import *
from config import *
from Navio import navio

#É para salvar o plot save=True
#ou somente mostrar na tela save=False
save = False
#Caso seja para salva salvar coloque o nome em "nome"
#e formato em 'formato'
nome = 'eta_fprop'
formato = 'pdf'

#caminho do arquivo de derivadas
entrada = '../dados/derivada.dat'

#legendas
ld = (r'\eta')

#label x e y
xlabel = r'$\eta$'
ylabel = r'$\frac{\rho \ l^2 u^2}{2}(a_ic+b_i \eta + c_i \eta^2)$'

dados = es(('',entrada, ''))
dadosf = dados.lerarqder()
emb = navio(dadosf, tipo = TipoModelo)

eta = []
fx = []
etav = sp.linspace(-2, -0.5,100)
for etai in etav:
  if eta == 0:
    break
  u = dadosf['unom']/etai
  emb.MudaVel(sp.array([u, 0, 0, 0, 0, 0]))
  fxi = emb.prop.Fx()
  eta.append(etai)
  fx.append(fxi)

fig = plt.figure()
ax = fig.add_subplot(111)  
ax.plot(eta, fx)
#leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
 
if save:
    plt.savefig(nome, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
