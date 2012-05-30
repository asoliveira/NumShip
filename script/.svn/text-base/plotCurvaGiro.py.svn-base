# -*- coding: utf-8 -*-

if adi:
    xlabel = r't'
    tini = velHis[0, 0]
    tmax = velHis[-1, 0]
else:
    xlabel = r't \ seg'


#####################################
###
###       Curva de Giro
###
#####################################   
if adi:
    ylabel = r'$x\prime$'
    xposlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xposlabel = r'$y \quad m$'    
plt.plot(posHis[:, 2],  posHis[:, 1],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'PosOri.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

#####################################
###
###      �ngulo de deriva
###
#####################################   
if adi:
    ylabel = r'$\beta$'
    xlabel = r'$t \prime$'
else:
    ylabel = r'$\beta$'
    xlabel = r'$t $'
plt.plot(betaHis[:, 0],  betaHis[:, 1]*(180/sp.pi),  'b-')
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'beta.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

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
    
if adi:
    xlabel = r't'
else:
    xlabel = r't \ seg'

plt.plot(velHis[:, 0],  velHis[:, 1],  'b-')
if adi:
    ylabel = r'$u\prime$'

else:
    ylabel = r'$u \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
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
    
plt.plot(velHis[:, 0],  velHis[:, 2],  'b-')

if adi:
    ylabel = r'$v\prime$'
else:
    ylabel = r'$v \quad m\times s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
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
    
plt.plot(velHis[:, 0],  velHis[:, 6]*(180/sp.pi),  'b-')
if adi:
    ylabel = r'$r\prime$'

else:
    ylabel = r'$r \quad s^{-1}$'

plt.ylabel(ylabel)
plt.xlabel(xlabel)


plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom + 5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')    

####################################
##
##       Velocidade de roll
##
####################################   
if GrausDeLib == 4:
    plt.subplot(4, 1, 4)
    
    plt.plot(velHis[:, 0],  velHis[:, 4],  'b-')
    
    if adi:
        ylabel = r'$ p\prime$'
    
    else:
        ylabel = r'$p \quad m\times s^{-1}$'
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')
    


if save:
    plt.savefig(dircg + TipoModelo +'Velo.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()
    



### ###################################
####
####       orienta��o roll
####
######################################   
if GrausDeLib == 4:
    plt.plot(posHis[:, 0],  posHis[:, 4],   'b-')
    plt.ylabel(r'$\phi$')
    plt.xlabel(xlabel)
    
    
    plt.twinx()
    plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')   
    
    
    if save:
        plt.savefig(dircg + TipoModelo +'Roll.' + formato,  format=formato)
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
plt.plot(acelHis[:, 0],  acelHis[:, 1],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
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




if adi:
    ylabel = r'$\dot v \prime$'
else:
    ylabel = r'$\dot v \quad m\times s^{-2}$'

plt.plot(acelHis[:, 0],  acelHis[:, 2],  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
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


plt.plot(acelHis[:, 0],  acelHis[:, 6]*(180/sp.pi),  'b--')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
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

    plt.plot(acelHis[:, 0],  acelHis[:, 4]*(180/sp.pi),  'b-')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dircg + TipoModelo +'Acel.' + formato,  format=formato)
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


plt.plot(forHis[:, 0],  forHis[:, 1]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
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
    
plt.plot(forHis[:, 0],  forHis[:, 2]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
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
 

if adi:
    ylabel = r'$N \prime$'
else:
    ylabel = r'$N \quad N \times m$'

plt.plot(forHis[:, 0],  forHis[:, 4]*ForEs,  'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
plt.ylabel(r'$\delta_r$')
### ###################################
####
####       Momento de Roll
####
######################################   

if GrausDeLib == 4:
    plt.subplot(4, 1, 4)

    if adi:
        ylabel = r'$K \prime$'
    else:
        ylabel = r'$K \quad N \times m$'

    plt.plot(forHis[:, 0],  forHis[:, 3]*ForEs,  'b-')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    plt.twinx()
    plt.plot(  lemeHis[:, 0],  lemeHis[:, 1]*(180/sp.pi),  'g--')
    plt.axis([tini,  tmax,  -abs(LemeCom +5),  abs(LemeCom +5) ])
    plt.ylabel(r'$\delta_r$')


if save:
    plt.savefig(dircg + TipoModelo +'ForMom.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 
### ###################################
####
####       Rota��o da M�quina
####
######################################   
plt.plot(propHis[:, 0],  propHis[:, 1],  'o-')#r 

plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(xlabel)


if save:
    plt.savefig(dircg + TipoModelo +'pltnt.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

### ###################################
####
####       Eta 
####
######################################   
plt.plot(etaHis[:, 0],  etaHis[:, 1],  '--')#r 

plt.ylabel(r'$\eta$ ')
plt.xlabel(xlabel)


if save:
    plt.savefig(dircg + TipoModelo +'pltetat.' + formato,  format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf() 

