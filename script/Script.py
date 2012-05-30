# -*- coding: iso-8859-1 -*-
   
import sys

sys.path.append('./AnalisaNavio/')

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
tmax = 100
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

tipoc = 'port'
Lemecg = sp.array(35.)

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

if TipoModelo== 'MARAD':
    Arq =  './dados/MarAdinputder.dat'
elif   TipoModelo== 'TP':  
    Arq =  './dados/TPinputder.dat'

In = ('Navioteste', Arq, 'inputtab.dat')
io = es(entrada = In)
################################
DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )


a = navio1.simula(met = metodo, t = tmax, t0 = tini, dt=passo,  GrausDeLib = GrausDeLib,    tipo ='ZigZag', leme = LemeCom,  proa = Proa,  RotCom=Rot)
dirzz = './figuras/Zig_Zag/' + TipoModelo + '/' 
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
    plt.ylabel(r'$\phi$')
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
    plt.ylabel(r'$\dot p \quad m\times s^{-2}$')
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






















### ###################################
####
####       Curva de Giro
####
###################################### 


"""
Plota curva de Giro
____________________
Variáveis de entrada

save (True/False) -- Opção para salvar as figuras ou somente mostrar os gráficos, utilizar somente True até o momento;
tipoc ('port'/'starboard') -- Opção para o tipo de curva de giro para bombordo o boreste;
formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura;
passo (float) -- Paso de tempo da integração;
tmax  (integer) -- Tempo  máximo;
tini (integer) -- Tempo inicial;
metodo ('euler') -- Método de integração;

____________________

Salva as figuras  no diretório './figuras/Curva_de_Giro/curva_de_giro'
"""

DicionarioDerivadas = io.lerarqder()

navio1 = navio(DicionarioDerivadas, Nome = 'Teste',   Tipo = TipoModelo )


if tipoc == 'port':
    tipoc = 'Curva_de_Giro_port'
else:
    tipoc = 'Curva_de_Giro_starboard'
    
b = navio1.simula(met = metodo, t = tmax, t0 = tini,dt=passo,  tipo= tipoc,  GrausDeLib = GrausDeLib,  leme = Lemecg,  RotCom=Rot)
dircg = './figuras/Curva_de_Giro/' + TipoModelo + '/' 
os.makedirs(dircg)
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
    
plt.plot(b[0][:, 0],  b[0][:, 1],  'b-')
plt.ylabel(r'$u \quad m\times s^{-1}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
plt.plot(b[0][:, 0],  b[0][:, 2],  'b-',  label=r'$v \quad m\times s^{-1}$')
plt.ylabel(r'$v \quad m\times s^{-1}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
plt.plot(b[0][:, 0],  b[0][:, 6]*(180/sp.pi),  'b-',  label=r'$r \quad s^{-1}$')
plt.ylabel(r'$r \quad s^{-1}$')
plt.xlabel(r'$t$ seg')


plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
plt.ylabel(r'$\delta_r$') 

####################################
##
##       Velocidade de roll
##
####################################   
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)
    
    plt.plot(b[0][:, 0],  b[0][:, 4]*(180/sp.pi),  'b-')
    plt.ylabel(r'$p \quad s^{-1}$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
    plt.ylabel(r'$\delta_r$')
    


if save:
    plt.savefig(dircg + TipoModelo +'Velo.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    


#####################################
###
###       Posição x
###
#####################################        

    
plt.plot(b[1][:, 2],  b[1][:, 1],  'b-')
plt.ylabel(r'$x\quad m $')
plt.xlabel(r'$y\quad m $')
 
if save:
    plt.savefig(dircg + TipoModelo +'PosOri.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

#### ###################################
#####
#####       orientação roll
#####
#######################################   
if GrausDeLib == 4:
    plt.plot(b[1][:, 0],  b[1][:, 4]*(180/sp.pi),   'b-')
    plt.ylabel(r'$\phi$')
    plt.xlabel(r'$t$ seg')
    
    
    plt.twinx()
    plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
    plt.ylabel(r'$\delta_r$')  

    if save:
        plt.savefig(dircg + TipoModelo +'Roll.' + formato,  format=formato)
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
    
plt.plot(b[2][:, 0],  b[2][:, 1],  'b-')
plt.ylabel(r'$\dot u \quad m\times s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
plt.plot(b[2][:, 0],  b[2][:, 2],  'b-')
plt.ylabel(r'$\dot v \quad m\times s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
    
plt.plot(b[2][:, 0],  b[2][:, 6]*(180/sp.pi),  'b-')
plt.ylabel(r'$\dot r \quad s^{-2}$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Aceleração Roll
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)

    plt.plot(b[2][:, 0],  b[2][:, 4]*(180/sp.pi),  'b-')
    plt.ylabel(r'$\dot \phi \quad m\times s^{-2}$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dircg + TipoModelo +'Acel.' + formato,  format=formato)
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
    
plt.plot(b[3][:, 0],  b[3][:, 1]*ForEs,  'b-')
plt.ylabel(r'$F_x \quad N$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
plt.plot(b[3][:, 0],  b[3][:, 2]*ForEs,  'b-')
plt.ylabel(r'$F_y \quad N$')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
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
    
plt.plot(b[3][:, 0],  b[3][:, 4]*ForEs,  'b-')
plt.ylabel(r'$N \quad N \times m $')
plt.xlabel(r'$t$ seg')

plt.twinx()
plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Momento de Roll
####
######################################   

if GrausDeLib == 4:
    plt.subplot(5, 1, 4)
   
    plt.plot(b[3][:, 0],  b[3][:, 3]*ForEs,  'b-')
    plt.ylabel(r'$K \quad N \times m$')
    plt.xlabel(r'$t$ seg')
    
    plt.twinx()
    plt.plot(  b[5][:, 0],  b[5][:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(Lemecg +5),  abs(Lemecg +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dircg + TipoModelo +'ForMom.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
### ###################################
####
####       Rotação da Máquina
####
######################################   
plt.plot(b[6][:, 0],  b[6][:, 1],  'o-')#r 

plt.ylabel(r'$n \quad rot \times s^{-1}$ ')
plt.xlabel(r'$t$ seg')


if save:
    plt.savefig(dircg + TipoModelo +'pltnt.' + formato,  format=formato)
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


#####################################################
##
##   Curva De Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'
##
#####################################################
##
##   Primeira Execução
##
f.write('\section{Curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'}')
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

f.write('ângulo de \emph{overshoot}(graus) = & '+ str(a[7][0]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}(metros)= & '+ str(a[7][0]['ospath']) )
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

f.write('ângulo de \emph{overshoot}(graus) = & '+ str(a[7][1]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}(metros)= & '+ str(a[7][1]['ospath']) )
f.write('\\\ \n\t\t')

##f.write('\emph{reach} = & '+ str(a[7][1]['reach']*(180/sp.pi)) )
##f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Terceira Execução1
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

f.write('ângulo de \emph{overshoot}(graus) = & '+ str(a[7][2]['osangle']*(180/sp.pi)))
f.write('\\\ \n\t\t')

f.write('\emph{overshoot path}(metros)= & '+ str(a[7][2]['ospath']) )
f.write('\\\ \n\t\t')

#f.write('\emph{reach} = & '+ str(a[7][2]['reach']*(180/sp.pi)) )
#f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')
f.write('\n\t')

f.write('\n\n\t')


f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'PosOri.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\t')

f.write('\subsection{Velocidades}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Velo.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Acelerações}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Acel.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Forças e Momentos}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'ForMom.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' + str(int(LemeCom))+'/'+str(int(Proa)) +'}. As forças e os mometos estão multiplicados por '+ str(ForEs) + '}')
f.write('\n\t')
f.write('\end{figure}')

f.write('\n\n\t')

















#####################################################
##
##   Curva De Giro
##
#####################################################

##
f.write('\section{Curva de Giro}')
f.write('\n\t')



f.write('\subsection{Dados}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\\begin{tabular}{ll}')
f.write('\\ \n\t\t')

f.write('Diametro tático (metros) = & ' + str(b[7][0]['taticalDiameter']))
f.write('\\\ \n\t\t')

f.write('Avanço (metros) = & ' + str(b[7][0]['advance']) )
f.write('\\\ \n\t\t')

f.write('Tranferência (metros) = & '+ str(b[7][0]['transfer']))
f.write('\\\ \n\t\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')






f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'PosOri.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\t')


if GrausDeLib==4:
    f.write('\\begin{figure}[H]')
    f.write('\n\t\t')
    f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Roll.' + formato + '}')
    f.write('\n\t')
    f.write('\caption{\\textit{Curva de Giro}}')
    f.write('\n\t')
    f.write('\end{figure}')
    f.write('\n\t')

f.write('\subsection{Velocidades}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Velo.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Acelerações}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Acel.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Forças e Momentos}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'ForMom.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}. As forças e os mometos estão multiplicados por '+ str(ForEs) + '}')
f.write('\n\t')
f.write('\end{figure}')







f.close()
