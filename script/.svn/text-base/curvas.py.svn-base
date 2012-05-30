# -*- coding: utf-8 -*-
import sys
sys.path.append('./source/')

import scipy as sp
from Es import *
from Leme import  *
from Prop import *
from Casco import *
from Navio import *

#IN = ('Navioteste','../dados/TPinputder.dat', 'inputtab.dat')
IN = ('Navioteste','./dados/MarAdinputder.dat', 'inputtab.dat')
io = es(entrada = IN)

io.plotcg(  save = True,  tipoc = 'port',  formato = 'png',  passo = 0.7, tmax = 500, tini =  0,  metodo = 'euler',  TipoModelo = 'MARAD' ,  GrausDeLib = 3)
io.plotzz(save = True,  formato = 'png',  passo = 0.5, tmax = 500, tini =  0,  metodo = 'euler' ,  TipoModelo = 'MARAD' ,  GrausDeLib = 3,  LemeCom= sp.array(20.),  Proa = sp.array(20.))
