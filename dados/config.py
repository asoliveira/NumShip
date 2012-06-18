# -*- coding: utf-8 -*-

#Configurações para a curva de giro
# -*- coding: utf-8 -*-

import scipy as sp

nome = 'B MarAd'
save = True
formato = 'eps'
passo = 0.7
tmax = 1000
tini =  0
metodo = 'rk4'
TipoModelo = 'MARAD'
GrausDeLib = 3
LemeCom = sp.array(35.)
ForEs = 1e0 #multiplicador da força
Overshoot = 35 #em graus
escala = '0.7'
Rot = sp.array(0.62)
tipoc = 'starboard' #tipo  de curva que será realizada 'starboard' ou 'port'
saida = 'txt' #Fimal do arquivo de saída
adi = False  #Valor booleano. Dados de entrada Adimensionais ou não
fdata = "%d-%m-%Y_%H:%M" #formato da data para ser usado em alguns momentos
#como para nomear a pasta de saída
plot = True #plotar?

#Fator multiplicador da força
Multbeta=1.*sp.array([1., 1.,1.]) 
Multr=1.*sp.array([1., 1.,1. ])
Multl=1.*sp.array([1.,1.,1. ]) 
Multbrl=1.*sp.array([1.,1.,1. ])