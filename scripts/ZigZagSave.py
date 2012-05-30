# -*- coding: iso-8859-1 -*-
"""
Plota curva de ZigZag
____________________
Variáveis de entrada:

save (True/False) -- Opção para salvar as figuras ou somente mostrar os gráficos, utilizar somente True até o momento;
formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura;
passo (float) -- Paso de tempo da integração;
tmax  (integer) -- Tempo  máximo;
tini (integer) -- Tempo inicial;
metodo ('euler') -- Método de integração;

____________________

Salva as figuras  no diretório './figuras/Curva_de_Giro/curva_de_giro'
"""        
import sys

sys.path.append('./source/')

import scipy as sp
from Es import *
from Leme import  *
from Prop import *
from Casco import *
from Navio import *

nome = 'B MarAd'
save = True
formato = 'png'
passo = 0.5
tmax = 500
tini =  0
metodo = 'euler'
TipoModelo = 'MARAD'
GrausDeLib = 3
LemeCom= sp.array(10.)
Proa = sp.array(10.)





#
#Classes
#

In = ('Navioteste','./dados/MarAdinputder.dat', 'inputtab.dat')
io = es(entrada = In)
################################
DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )


a = navio1.simula(met = metodo, t = tmax, t0 = tini, dt=passo,  GrausDeLib = GrausDeLib,    tipo ='ZigZag', leme = LemeCom,  proa = Proa)
dir = './figuras/Zig_Zag/' + TipoModelo + '/' 
os.makedirs(dir)
####################################
##
##       Velocidade em Surge
##
####################################        
plt.figure(1)
plt.subplot(511)

plt.plot(a[0][:, 0],  a[0][:, 1],  '.')
plt.xlabel('time (s)')
plt.ylabel(r'$u$')

plt.twinx()
plt.plot(a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
plt.ylabel(r'$\delta_R$')


####################################
##
##       Velocidade em Sway
##
####################################
fig = plt.figure()
plt.subplot(512)

plt.plot(a[0][:, 0],  a[0][:, 2],  '.')
plt.xlabel('time (s)')
plt.ylabel(r'$v$')

plt.twinx()
plt.plot(a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
plt.ylabel(r'$\delta_R$')

####################################
##
##       Velocidade de yaw
##
####################################   
plt.subplot(513)

plt.plot(a[0][:, 0],  a[0][:, 6],  '.')
plt.xlabel('time (s)')
plt.ylabel(r'$r$')

plt.twinx()
plt.plot(a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
plt.ylabel(r'$\delta_R$')    
    
####################################
##
##       Velocidade de roll
##
####################################   
plt.subplot(514)

plt.plot(a[0][:, 0],  a[0][:, 4],  '.')
plt.xlabel('time (s)')
plt.ylabel(r'$\dot\phi$')

plt.twinx()
plt.plot(a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
plt.ylabel(r'$\delta_R$')

if save:
    plt.savefig(dir + TipoModelo +'vel',  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 


#####################################
###
###       Posição 
###
#####################################        
#plt.plot(a[1][:, 0],  a[1][:, 1],  '--')
#plt.ylabel(r'$x$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltxt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#####################################
###
###       Posição y
###
#####################################
#plt.plot(a[1][:, 0],  a[1][:, 2],  'g^')#v 
#
#plt.ylabel(r'$y$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltyt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#
### ###################################
####
####       Posição Psi
####
######################################   
#plt.plot(a[1][:, 0],  a[1][:, 6]*(180/sp.pi),  'o-',   a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
#
#plt.ylabel(r'$\psi$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltyawt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()        
#    
### ###################################
####
####       orientação roll
####
######################################   
#plt.plot(a[1][:, 0],  a[1][:, 4],  'o-')
#
#plt.ylabel(r'$\phi$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltrollt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf() 
###
###
###       Aceleração
###
###
#
#
#
#####################################
###
###       dotu
###
#####################################        
#plt.plot(a[2][:, 0],  a[2][:, 1],  '--')
#plt.ylabel(r'$\dot u$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltdotut',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#####################################
###
###       dot v
###
#####################################
#plt.plot(a[2][:, 0],  a[2][:, 2],  'g^')#v 
#
#plt.ylabel(r'$\dot v$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltdotvt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#
### ###################################
####
####      Acerleração Yaw
####
######################################   
#plt.plot(a[2][:, 0],  a[2][:, 6]*(sp.array([180])/sp.pi))#,  'o-',   a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
#
#plt.ylabel(r'$\dot r$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltdotrt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()        
#    
### ###################################
####
####       Aceleração Roll
####
######################################   
#plt.plot(a[2][:, 0],  a[2][:, 4]*(sp.array([180])/sp.pi),  'o-')#r 
#
#plt.ylabel(r'$\dot p$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltdotpt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf() 
#    
#    
###
###
###       Força
###
###
#
#
#
#####################################
###
###       Força de Surge
###
#####################################        
#plt.plot(a[3][:, 0],  a[3][:, 1],  '--')
#plt.ylabel(r'$F_x$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltforsurget',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#####################################
###
###       Força de Yaw
###
#####################################
#plt.plot(a[3][:, 0],  a[3][:, 2],  'g^')#v 
#
#plt.ylabel(r'$F_y$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltforswayt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()
#
### ###################################
####
####      Momento de Yaw
####
######################################   
#plt.plot(a[3][:, 0],  a[3][:, 4],  'o-')#,   a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
#
#plt.ylabel(r'$N$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltNt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf()        
#    
### ###################################
####
####       Momento de Roll
####
######################################   
#plt.plot(a[3][:, 0],  a[3][:, 3],  'o-')#r 
#
#plt.ylabel(r'$K$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltKt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf() 
#
#
#
### ###################################
####
####       Rotação da Máquina
####
######################################   
#plt.plot(a[6][:, 0],  a[6][:, 1],  'o-')#r 
#
#plt.ylabel(r'$n$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltnt',  format=formato)
#    plt.clf()
#else:
#    plt.show()
#    plt.clf() 
#    
### ###################################
####
####       Leme
####
######################################   
#plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  '-.')
#
#plt.ylabel(r'$\delta_R$')
#plt.xlabel(r'$t$')
#plt.title ('ZigZag10/10')
#
#if save:
#    plt.savefig(dir + TipoModelo +'pltlemet',  format=formato)
#    plt.clf()
#else: 
#    plt.show()
#    plt.clf() 
#
#
#####################################################
##
##   Relatório
##
#####################################################
#
#f = open('./dados/rel.tex', 'w')
#
#f.write('\chapter{Relatório da Curva Zig-Zag Navio '+ nome +' }\n\n\t')
#
##
##   Primeira Execução
##
#f.write('\section{Primera Execução}')
#f.write('\n\t')
#f.write('\\begin{center}')
#f.write('\n\t')
#f.write('\\begin{tabular}{ll}')
#f.write('\\ \n\t\t')
#
#f.write('execução = & ' + str(a[7][0]['exeNummber']))
#f.write('\\\ \n\t\t')
#
#f.write('Tempo até a execução (segundos) = & ' + str(a[7][0]['time']) )
#f.write('\\\ \n\t\t')
#
#f.write('ângulo de \emph{overshoot} = & '+ str(a[7][0]['osangle']*(180/sp.pi)))
#f.write('\\\ \n\t\t')
#
#f.write('\emph{overshoot path}= & '+ str(a[7][0]['ospath']) )
#f.write('\\\ \n\t\t')
#
##f.write('\emph{reach} = & '+ str(a[7][0]['reach']*(180/sp.pi)) )
##f.write('\\\ \n\t')
#
#f.write('\end{tabular}')
#f.write('\n\t')
#f.write('\end{center}')
#
#
##
##   Segunda Execução
##
#
#f.write('\section{Segunda Execução}')
#f.write('\n\t')
#f.write('\\begin{center}')
#f.write('\n\t')
#f.write('\\begin{tabular}{ll}')
#f.write('\\ \n\t\t')
#
#f.write('execução = & ' + str(a[7][1]['exeNummber']))
#f.write('\\\ \n\t\t')
#
#f.write('Tempo até a execução (segundos) = & ' + str(a[7][1]['time']) )
#f.write('\\\ \n\t\t')
#
#f.write('ângulo de \emph{overshoot} = & '+ str(a[7][1]['osangle']*(180/sp.pi)))
#f.write('\\\ \n\t\t')
#
#f.write('\emph{overshoot path}= & '+ str(a[7][1]['ospath']) )
#f.write('\\\ \n\t\t')
#
##f.write('\emph{reach} = & '+ str(a[7][1]['reach']*(180/sp.pi)) )
##f.write('\\\ \n\t')
#
#f.write('\end{tabular}')
#f.write('\n\t')
#f.write('\end{center}')
#
#
##
##   Terceira Execução
##
#
#f.write('\section{Terceira Execução}')
#f.write('\n\t')
#f.write('\\begin{center}')
#f.write('\n\t')
#f.write('\\begin{tabular}{ll}')
#f.write('\\ \n\t\t')
#
#f.write('execução = & ' + str(a[7][2]['exeNummber']))
#f.write('\\\ \n\t\t')
#
#f.write('Tempo até a execução (segundos) = & ' + str(a[7][2]['time']) )
#f.write('\\\ \n\t\t')
#
#f.write('ângulo de \emph{overshoot} = & '+ str(a[7][2]['osangle']*(180/sp.pi)))
#f.write('\\\ \n\t\t')
#
#f.write('\emph{overshoot path}= & '+ str(a[7][2]['ospath']) )
#f.write('\\\ \n\t\t')
#
##f.write('\emph{reach} = & '+ str(a[7][2]['reach']*(180/sp.pi)) )
##f.write('\\\ \n\t')
#
#f.write('\end{tabular}')
#f.write('\n\t')
#f.write('\end{center}')
#f.close()
