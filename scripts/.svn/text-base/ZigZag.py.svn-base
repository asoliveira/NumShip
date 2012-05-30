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
import os
print os.getcwd()
sys.path.append('./AnalisaNavio/')

import scipy as sp
from Es import *
from Leme import  *
from Prop import *
from Casco import *
from Navio import *


nome = 'B-MarAd'
save = True
formato = 'eps'
passo = 0.7
tmax = 100
tini =  0
metodo = 'euler'
TipoModelo = 'MARAD'
GrausDeLib = 3
LemeCom= sp.array(10.)
Proa = sp.array(10.)
ForEs = 1e-6
Overshoot = 25
escala = '0.7'



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

if GrausDeLib == 4:
    plt.subplot(4, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 1)
    
plt.plot(a[0][:, 0],  a[0][:, 1],  'b-')
plt.ylabel(r'$u$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')


####################################
##
##       Velocidade em Sway
##
####################################


if GrausDeLib == 4:
    plt.subplot(4, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 2)
    
plt.plot(a[0][:, 0],  a[0][:, 2],  'b-',  label=r'$v$')
plt.ylabel(r'$v$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--',  label=r'$\delta_R$')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')

####################################
##
##       Velocidade de yaw
##
####################################   

if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)
    
plt.plot(a[0][:, 0],  a[0][:, 6],  'b-',  label=r'$r$')
plt.ylabel(r'$r$')
plt.xlabel(r'$t$')


plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--',  label=r'$\delta_R$')
plt.axis([tini,  tmax,  -abs(LemeCom + 5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')    

####################################
##
##       Velocidade de roll
##
####################################   
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)
    
    plt.plot(a[0][:, 0],  a[0][:, 4],  'b-')
    plt.ylabel(r'$p$')
    plt.xlabel(r'$t$')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_R$')
    


if save:
    plt.savefig(dir + TipoModelo +'Velo.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    


#####################################
###
###       Posição x
###
#####################################        

if GrausDeLib == 4:
    plt.subplot(3, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(2, 1, 1)
    
plt.plot(a[1][:, 1],  a[1][:, 2],  'b-')
plt.ylabel(r'$y$')
plt.xlabel(r'$x$')
 

### ###################################
####
####       Posição Psi
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(3, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(2, 1, 2)
    
plt.plot(a[1][:, 0],  a[1][:, 6]*(180/sp.pi),   'b-')
plt.ylabel(r'$\psi$')
plt.xlabel(r'$t$')
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])
plt.ylabel(r'$\delta_R$')   
### ###################################
####
####       orientação roll
####
######################################   
if GrausDeLib == 4:
    plt.subplot(3, 1, 3)
    plt.plot(a[1][:, 0],  a[1][:, 4],   'b-')
    plt.ylabel(r'$\psi$')
    plt.xlabel(r'$t$')
    
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_R$')   

plt.suptitle ('Zig Zag')

if save:
    plt.savefig(dir + TipoModelo +'PosOri.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
    
    
###
###
###       Aceleração
###
###

#####################################
###
###       dotu
###
#####################################        

if GrausDeLib == 4:
    plt.subplot(4, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 1)
    
plt.plot(a[2][:, 0],  a[2][:, 1],  'b-')
plt.ylabel(r'$\dot u$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
#####################################
###
###       dot v
###
#####################################

if GrausDeLib == 4:
    plt.subplot(4, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 2)
    
plt.plot(a[2][:, 0],  a[2][:, 2],  'b-')
plt.ylabel(r'$\dot v$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
### ###################################
####
####      Acerleração Yaw
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)
    
plt.plot(a[2][:, 0],  a[2][:, 6],  'b-')
plt.ylabel(r'$\dot r$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
### ###################################
####
####       Aceleração Roll
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)

    plt.plot(a[2][:, 0],  a[2][:, 4],  'b-')
    plt.ylabel(r'$\dot u$')
    plt.xlabel(r'$t$')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_R$')


if save:
    plt.savefig(dir + TipoModelo +'Acel.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
###
###
###       Força
###
###
#####################################
###
###       Força de Surge
###
#####################################        

if GrausDeLib == 4:
    plt.subplot(4, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 1)
    
plt.plot(a[3][:, 0],  a[3][:, 1]*ForEs,  'b-')
plt.ylabel(r'$F_x$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
#####################################
###
###       Força de Sway
###
#####################################

if GrausDeLib == 4:
    plt.subplot(4, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 2)
    
plt.plot(a[3][:, 0],  a[3][:, 2]*ForEs,  'b-')
plt.ylabel(r'$F_y$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
### ###################################
####
####      Momento de Yaw
####
######################################   

if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)
    
plt.plot(a[3][:, 0],  a[3][:, 4]*ForEs,  'b-')
plt.ylabel(r'$N$')
plt.xlabel(r'$t$')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_R$')
### ###################################
####
####       Momento de Roll
####
######################################   

if GrausDeLib == 4:
    plt.subplot(5, 1, 4)
   
    plt.plot(a[3][:, 0],  a[3][:, 3]*ForEs,  'b-')
    plt.ylabel(r'$M$')
    plt.xlabel(r'$t$')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_R$')


if save:
    plt.savefig(dir + TipoModelo +'ForMom.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
### ###################################
####
####       Rotação da Máquina
####
######################################   
plt.plot(a[6][:, 0],  a[6][:, 1],  'o-')#r 

plt.ylabel(r'$n$')
plt.xlabel(r'$t$')


if save:
    plt.savefig(dir + TipoModelo +'pltnt.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
    

#####################################################
##
##   Relatório
##
#####################################################

f = open('./dados/rel.tex', 'w')

f.write('\chapter{Relatório Navio '+ nome +' }\n\n\t')

##
##   Primeira Execução
##
f.write('\section{Curva de ZigZag}')
f.write('\n\t')
f.write('\subsection{Primera Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\\begin{tabular}{ll}')
f.write('\\ \n\t\t')

f.write('execução = & ' + str(a[7][0]['exeNummber']))
f.write('\\\ \n\t\t')

f.write('Tempo até a execução (segundos) = & ' + str(a[7][0]['time']) )
f.write('\\\ \n\t\t')

f.write('ângulo de \emph{overshoot} = & '+ str(a[7][0]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}= & '+ str(a[7][0]['ospath']) )
f.write('\\\ \n\t\t')

#f.write('\emph{reach} = & '+ str(a[7][0]['reach']*(180/sp.pi)) )
#f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Segunda Execução
##

f.write('\subsection{Segunda Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\\begin{tabular}{ll}')
f.write('\\ \n\t\t')

f.write('execução = & ' + str(a[7][1]['exeNummber']))
f.write('\\\ \n\t\t')

f.write('Tempo até a execução (segundos) = & ' + str(a[7][1]['time']) )
f.write('\\\ \n\t\t')

f.write('ângulo de \emph{overshoot} = & '+ str(a[7][1]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}= & '+ str(a[7][1]['ospath']) )
f.write('\\\ \n\t\t')

##f.write('\emph{reach} = & '+ str(a[7][1]['reach']*(180/sp.pi)) )
##f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Terceira Execução
##

f.write('\subsection{Terceira Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\\begin{tabular}{ll}')
f.write('\\ \n\t\t')

f.write('execução = & ' + str(a[7][2]['exeNummber']))
f.write('\\\ \n\t\t')

f.write('Tempo até a execução (segundos) = & ' + str(a[7][2]['time']) )
f.write('\\\ \n\t\t')

f.write('ângulo de \emph{overshoot} = & '+ str(a[7][2]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}= & '+ str(a[7][2]['ospath']) )
f.write('\\\ \n\t\t')

#f.write('\emph{reach} = & '+ str(a[7][2]['reach']*(180/sp.pi)) )
#f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')
f.write('\n\t')

f.write('\n\n\t')


f.write('\\begin{figure}[h!]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{./figuras/Zig_Zag/MARAD/MARADPosOri.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de ZigZag}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\t')

f.write('\subsection{Velocidades}')
f.write('\n\n\t')

f.write('\\begin{figure}[h!]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{./figuras/Zig_Zag/MARAD/MARADVelo.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de ZigZag}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Acelerações}')
f.write('\n\t')

f.write('\\begin{figure}[h!]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{./figuras/Zig_Zag/MARAD/MARADAcel.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de ZigZag}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Forças e Momentos}')
f.write('\n\t')

f.write('\\begin{figure}[h!]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{./figuras/Zig_Zag/MARAD/MARADForMom.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de ZigZag}. As forças e os mometos estão multiplicados por '+ str(ForEs) + '}')
f.write('\n\t')
f.write('\end{figure}')


f.close()
