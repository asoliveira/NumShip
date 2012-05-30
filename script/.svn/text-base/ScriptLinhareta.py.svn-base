# -*- coding: iso-8859-1 -*-
   
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
passo = 0.7
tmax = 1500
tini =  0
metodo = 'euler'
TipoModelo = 'MARAD'
GrausDeLib = 3
LemeCom= sp.array(10.)
Proa = sp.array(10.)
ForEs = 1e-6
Overshoot = 35
escala = '0.7'
Rot = sp.array(1.24)


"""
Plota curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'
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



In = ('Navioteste','./dados/MarAdinputder.dat', 'inputtab.dat')
io = es(entrada = In)
################################
DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )

navio1.MudaLemeCom(sp.array(0.))

a = navio1.simula(met = metodo, t = tmax, t0 = tini, dt=passo,  GrausDeLib = GrausDeLib,    tipo ='',  RotCom=Rot)
dirzz = './figuras/Linha_reta/' + TipoModelo + '/' 
os.makedirs(dirzz)


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
plt.ylabel(r'$u \quad m\times s^{-1}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')


####################################
##
##       Velocidade em Sway
##
####################################


if GrausDeLib == 4:
    plt.subplot(4, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 2)
    
plt.plot(a[0][:, 0],  a[0][:, 2],  'b-',  label=r'$v \quad m\times s^{-1}$')
plt.ylabel(r'$v \quad m\times s^{-1}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--',  label=r'$\delta_r$')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')

####################################
##
##       Velocidade de yaw
##
####################################   

if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)
    
plt.plot(a[0][:, 0],  a[0][:, 6]*(180/sp.pi),  'b-',  label=r'$r \quad s^{-1}$')
plt.ylabel(r'$r \quad s^{-1}$')
plt.xlabel(r'$t$ seg')


plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--',  label=r'$\delta_r$')
plt.axis([tini,  tmax,  -abs(LemeCom + 5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')    

####################################
##
##       Velocidade de roll
##
####################################   
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)
    
    plt.plot(a[0][:, 0],  a[0][:, 4],  'b-')
    plt.ylabel(r'$p \quad s^{-1}$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')
    


if save:
    plt.savefig(dirzz + TipoModelo +'Velo.' + formato,  format=formato)
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
plt.ylabel(r'$y\quad m $')
plt.xlabel(r'$x\quad m $')
 

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
plt.xlabel(r'$t$ seg')
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])
plt.ylabel(r'$\delta_r$')   
### ###################################
####
####       orientação roll
####
######################################   
if GrausDeLib == 4:
    plt.subplot(3, 1, 3)
    plt.plot(a[1][:, 0],  a[1][:, 4],   'b-')
    plt.ylabel(r'$\psi$')
    plt.xlabel(r'$t$ seg')
    
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')   


if save:
    plt.savefig(dirzz + TipoModelo +'PosOri.' + formato,  format=formato)
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
plt.ylabel(r'$\dot u \quad m\times s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
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
plt.ylabel(r'$\dot v \quad m\times s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####      Acerleração Yaw
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)
    
plt.plot(a[2][:, 0],  a[2][:, 6]*(180/sp.pi),  'b-')
plt.ylabel(r'$\dot r \quad s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Aceleração Roll
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)

    plt.plot(a[2][:, 0],  a[2][:, 4]*(180/sp.pi),  'b-')
    plt.ylabel(r'$\dot u \quad m\times s^{-2}$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dirzz + TipoModelo +'Acel.' + formato,  format=formato)
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
plt.ylabel(r'$F_x \quad N$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
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
plt.ylabel(r'$F_y \quad N $')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
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
plt.ylabel(r'$N \quad N \times m$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Momento de Roll
####
######################################   

if GrausDeLib == 4:
    plt.subplot(5, 1, 4)
   
    plt.plot(a[3][:, 0],  a[3][:, 3]*ForEs,  'b-')
    plt.ylabel(r'$K \quad N \times m$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  a[5][:, 0],  a[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dirzz + TipoModelo +'ForMom.' + formato,  format=formato)
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

plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(r'$t$ seg')


if save:
    plt.savefig(dirzz + TipoModelo +'pltnt.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 





