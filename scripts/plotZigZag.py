# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis

dirzz = scgarq + '/figuras/'
os.makedirs(dirzz)

#Velocidade em Surge
if adi:
    xlabel = r'$t\prime$'
    tini = velhis[0, 0]
    tmax = velhis[-1, 0]    
else:
    xlabel = r't \ seg'
    
    
plt.figure(1)

if GrausDeLib == 4:
    plt.subplot(4, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 1)

plt.plot(velhis[:, 0],  velhis[:, 1],  'b-')
if adi:
    ylabel = r'$u\prime$'
else:
    ylabel = r'$u \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
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
    
plt.plot(velhis[:, 0],  velhis[:, 2],  'b-')

if adi:
    ylabel = r'$v\prime$'
else:
    ylabel = r'$v \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
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
    
plt.plot(velhis[:, 0],  velhis[:, 6]*(180/sp.pi),  'b-')
if adi:
    ylabel = r'$r\prime$'

else:
    ylabel = r'$r \quad s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)


plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz + 5),  abs(lemezz +5) ])
plt.ylabel(r'$\delta_r$')    

####################################
##
##       Velocidade de roll
##
####################################   
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)
    
    plt.plot(velhis[:, 0],  velhis[:, 4],  'b-')
    
    if adi:
        ylabel = r'$ p\prime$'
    
    else:
        ylabel = r'$p \quad m\times s^{-1}$'
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
    plt.ylabel(r'$\delta_r$')
    


if save:
    plt.savefig(dirzz + TipoModelo +'Velo.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    


#####################################
###
###       Posi��o x
###
#####################################        

if GrausDeLib == 4:
    plt.subplot(3, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(2, 1, 1)
    
if adi:
    ylabel = r'$y\prime$'
    xposlabel = r'$x\prime$'
else:
    ylabel = r'$y \quad m$'    
    xposlabel = r'$x \quad m$'
plt.plot(poshis[:, 1],  poshis[:, 2],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
 

### ###################################
####
####       Posi��o Psi
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(3, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(2, 1, 2)
    
plt.plot(poshis[:, 0],  poshis[:, 6]*(-180/sp.pi),   'b-')
plt.ylabel(r'$-\psi$')
plt.xlabel(xlabel)
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(Overshoot +5),  abs(Overshoot +5) ])
plt.ylabel(r'$\delta_r$')   
### ###################################
####
####       orienta��o roll
####
######################################   
if GrausDeLib == 4:
    plt.subplot(3, 1, 3)
    plt.plot(poshis[:, 0],  poshis[:, 4],   'b-')
    plt.ylabel(r'$\phi$')
    plt.xlabel(xlabel)
    
    
    plt.twinx()
    plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
    plt.ylabel(r'$\delta_r$')   


if save:
    plt.savefig(dirzz + TipoModelo +'PosOri.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
    
    
###
###
###       Acelera��o
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

if adi:
    ylabel = r'$\dot u \prime$'
else:
    ylabel = r'$\dot u \quad m\times s^{-2}$'
plt.plot(acelhis[:, 0],  acelhis[:, 1],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
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




if adi:
    ylabel = r'$\dot v \prime$'
else:
    ylabel = r'$\dot v \quad m\times s^{-2}$'

plt.plot(acelhis[:, 0],  acelhis[:, 2],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####      Acerlera��o Yaw
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 3)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 3)



if adi:
    ylabel = r'$\dot r \prime$'
else:
    ylabel = r'$\dot r \quad m\times s^{-2}$'


plt.plot(acelhis[:, 0],  acelhis[:, 6]*(180/sp.pi),  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Acelera��o Roll
####
######################################   
 
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)

    if adi:
        ylabel = r'$\dot p \prime$'
    else:
        ylabel = r'$\dot p \quad m\times s^{-2}$'

    plt.plot(acelhis[:, 0],  acelhis[:, 4]*(180/sp.pi),  'b-')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dirzz + TipoModelo +'Acel.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
###
###
###       For�a
###
###
#####################################
###
###       For�a de Surge
###
#####################################        

if GrausDeLib == 4:
    plt.subplot(4, 1, 1)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 1)



if adi:
    ylabel = r'$F_x \prime$'
else:
    ylabel = r'$F_x \quad N$'


plt.plot(forhis[:, 0],  forhis[:, 1]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
plt.ylabel(r'$\delta_r$')
#####################################
###
###       For�a de Sway
###
#####################################

if GrausDeLib == 4:
    plt.subplot(4, 1, 2)
elif GrausDeLib == 3:
    plt.subplot(3, 1, 2)

if adi:
    ylabel = r'$F_y \prime$'
else:
    ylabel = r'$F_y \quad N $'
    
plt.plot(forhis[:, 0],  forhis[:, 2]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
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
 

if adi:
    ylabel = r'$N \prime$'
else:
    ylabel = r'$N \quad N \times m$'

plt.plot(forhis[:, 0],  forhis[:, 4]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Momento de Roll
####
######################################   

if GrausDeLib == 4:
    plt.subplot(5, 1, 4)

    if adi:
        ylabel = r'$K \prime$'
    else:
        ylabel = r'$K \quad N \times m$'

    plt.plot(forhis[:, 0],  forhis[:, 3]*ForEs,  'b-')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemehis[:, 0],  lemehis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(lemezz +5),  abs(lemezz +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dirzz + TipoModelo +'ForMom.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
### ###################################
####
####       Rota��o da M�quina
####
######################################   
plt.plot(prophis[:, 0],  prophis[:, 1],  'o-')#r 

plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(xlabel)


if save:
    plt.savefig(dirzz + TipoModelo +'pltnt.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

### ###################################
####
####       Eta 
####
######################################   
plt.plot(etahis[:, 0],  etahis[:, 1],  '--')#r 

plt.ylabel(r'$\eta$ ')
plt.xlabel(xlabel)


if save:
    plt.savefig(dirzz + TipoModelo +'pltetat.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

