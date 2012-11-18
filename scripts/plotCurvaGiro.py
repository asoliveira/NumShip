# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis


try:
  dircg = scgarq + '/figuras/' 
  os.makedirs(dircg)
except NameError:
  print 'houve algum problema na criação do diretório ' + dircg

if adi:
    xlabel = r't'
    tini = velHis[0, 0]
    tmax = velHis[-1, 0]
else:
    xlabel = r't \ seg'

    
#Curva de diro
if adi:
    ylabel = r'$x\prime$'
    xlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xlabel = r'$y \quad m$'    
plt.plot(posHis[:, 2], posHis[:, 1], 'b-')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.savefig(dircg + TipoModelo +'_cg.' + formato, format=formato)
plt.clf()

#Ângulo de deriva
if adi:
    ylabel = r'$\beta$'
    xlabel = r'$t \prime$'
else:
    ylabel = r'$\beta$'
    xlabel = r'$t $'

plt.plot(betaHis[:, 0], betaHis[:, 1], 'b-')    
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.ylabel(r'$\beta$ arctan ($\frac{-v}{u}$)')
plt.savefig(dircg + TipoModelo +'_beta.' + formato, format=formato)
plt.clf()

#Velocidade em Surge       
if adi:
    xlabel = r't'
    ylabel = r'$u\prime$'
else:
    xlabel = r't \ seg'
    ylabel = r'$u \quad m\times s^{-1}$'
    
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.plot(velHis[:, 0], velHis[:, 1], 'b-', label = r'$u$')
plt.savefig(dircg + TipoModelo +'_u.' + formato, format=formato)
plt.clf()

#
#Velocidade em sway    

if adi:
    ylabel = r'$v\prime$'
    xlabel = r't'
else:
    ylabel = r'$v \quad m\times s^{-1}$'
    xlabel = r't \ seg'
    
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.plot(velHis[:, 0], velHis[:, 2], 'b-', label = r'$v$')
plt.savefig(dircg + TipoModelo +'_v.' + formato, format=formato)
plt.clf()


#
#Velocidade de yaw

if adi:
    ylabel = r'$r\prime$'
    xlabel = r't'
else:
    ylabel = r'$r \quad s^{-1}$'
    xlabel = r't \ seg'

plt.plot(velHis[:, 0], velHis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot\psi$')
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_r.' + formato, format=formato)
plt.clf()
#
#Velocidade de roll   

if adi:
    ylabel = r'$ p\prime$'   
else:
    ylabel = r'$p \quad m\times s^{-1}$'

plt.plot(velHis[:, 0], velHis[:, 4], 'b-', label = r'$\dot \phi$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_p.' + formato, format=formato)
plt.clf()
    
#orientação roll

plt.plot(posHis[:, 0], posHis[:, 4], 'b-', label = r'$\phi$')
plt.grid(True)
plt.ylabel(r'$\phi$')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_roll.' + formato, format=formato)
plt.clf()
    

#Aceleração
#dot u
if adi:
    ylabel = r'$\dot u \prime$'
else:
    ylabel = r'$\dot u \quad m\times s^{-2}$'
plt.plot(acelHis[:, 0], acelHis[:, 1], 'b-', label = r'$\dot u$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_dotu.' + formato, format=formato)
plt.clf()


#Dot v
if adi:
    ylabel = r'$\dot v \prime$'
else:
    ylabel = r'$\dot v \quad m\times s^{-2}$'

plt.plot(acelHis[:, 0], acelHis[:, 2], 'b-', label = r'$\dot v$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_dotv.' + formato, format=formato)
plt.clf()


#Aceleração de yaw
if adi:
    ylabel = r'$\dot r \prime$'
else:
    ylabel = r'$\dot r \quad m\times s^{-2}$'

plt.plot(acelHis[:, 0], acelHis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot \psi$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_dotr.' + formato, format=formato)
plt.clf()

#Aceleração de roll
if adi:
    ylabel = r'$\dot p \prime$'
else:
    ylabel = r'$\dot p \quad m\times s^{-2}$'

plt.plot(acelHis[:, 0], acelHis[:, 4]*(180/sp.pi), 'b-', label = r'$$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.ylabel(r'$\delta_R$')
plt.savefig(dircg + TipoModelo +'dotp.' + formato, format=formato)
plt.clf()


#Forças
#Forças em surge
if adi:
    ylabel = r'$F_x \prime$'
else:
    ylabel = r'$F_x \quad N$'

plt.plot(forHis[:, 0], forHis[:, 1], 'b-', label = r'$F_x$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_fx.' + formato, format=formato)
plt.clf()


#Força em Sway
if adi:
    ylabel = r'$F_y \prime$'
else:
    ylabel = r'$F_y \quad N $'
    
plt.plot(forHis[:, 0], forHis[:, 2], 'b-', label = r'$F_y$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_fy.' + formato, format=formato)
plt.clf()


#Momento de yaw
if adi:
    ylabel = r'$N \prime$'
else:
    ylabel = r'$N \quad N \times m$'

plt.plot(forHis[:, 0], forHis[:, 6], 'b-', label = r'$N$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo + '_n.' + formato, format=formato)
plt.clf()

#Momento de Roll
if adi:
    ylabel = r'$K \prime$'
else:
    ylabel = r'$K \quad N \times m$'

plt.plot(forHis[:, 0], forHis[:, 4], 'b-', label = r'$K$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo + '_k.' + formato, format=formato)
plt.clf()


#Rotação da máquina
plt.plot(propHis[:, 0], propHis[:, 1], 'o-', label = r'$rot$')
plt.grid(True)
plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_rot.' + formato, format=formato)
plt.clf()


#eta
plt.plot(etaHis[:, 0], etaHis[:, 1], '--', label = r'$\eta$')
plt.grid(True)
plt.ylabel(r'$\eta$ ')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dircg + TipoModelo +'_eta.' + formato, format=formato)
plt.clf()