# -*- coding: utf-8 -*-

#Configurações para a curva de giro
# -*- coding: utf-8 -*-

import scipy as sp

nome = 'B'
save = True
formato = 'pdf'
passo = 0.7
tmax = 1000
tini =  0
metodo = 'euler'
#Os Tipos de modelos de matemáticos disponíveis são (MARAD, MARAD-L1, MARAD-P)
TipoModelo = 'MARAD'
GrausDeLib = 3
#multiplicador da força
ForEs = 1e0 
Overshoot = 35 #em graus
escala = '0.6'
Rot = sp.array(1.26)
#tipo  de curva que será realizada 'starboard' ou 'port'
tipoc = 'starboard' 
#leme utilizado na curva de Giro
lemecg = sp.array(35) 
#Proa que inicia o comando de leme utilizado na curva de Zig Zag
proazz = sp.array(20) 
#leme utilizado na curva de Zig Zag
lemezz = sp.array(20) 

#O que será utilizado, um arquivo com as derivadas hidrodinâmicas (somente um
#navio)[1] ou uma pasta com vários arquivos(vários navios)[2]?
qtd=1

#Caso a opção qtd seja 1 digite o nome do arquivo de derivadas hidrodinâmicas
#de entrada
arq = 'navioB.dat'

#Final do arquivo de saída
saida = 'txt'
#Valor booleano. Dados de entrada Adimensionais ou não
adi = False  
#formato da data para ser usado em alguns momentos como para nomear a pasta de
#saída
fdata = "%d-%m-%Y_%H:%M" 
plot = True #plotar?

#usar multiplicador
mul = True
#Fator multiplicador da força
Multbeta= 1. * sp.array([1., 1.,1.]) 
Multr=1. * sp.array([1., 1.,1. ])
Multl=1. * sp.array([1.,1.,1. ]) 
Multbrl= 1. * sp.array([1.,1.,1. ])
