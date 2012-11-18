# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dirzz -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velhis -- 
#poshis


try:
  dirzz = scgarq + '/figuras/' 
  os.makedirs(dirzz)
except NameError:
  print 'houve algum problema na criação do diretório ' + dirzz

if adi:
    xlabel = r't'
    tini = velhis[0, 0]
    tmax = velhis[-1, 0]
else:
    xlabel = r't \ seg'

    
#Curva de Zigzag
if adi:
    ylabel = r'$\psi$'
    xlabel = r'$t$'
else:
    ylabel = r'$\psi$'    
    xlabel = r'$yt$'    

ma = sp.array(poshis[:, 6]).max()
mi = sp.array(poshis[:, 6]).min()
        
if abs(mi) > ma:
  mi = mi * 180 / sp.pi
  plt.axis([poshis[0,0], poshis[-1,0], mi, abs(mi) ])
else:
  ma = ma * 180 / sp.pi
  plt.axis([poshis[0,0], poshis[-1,0], -ma, ma ])    
plt.plot(poshis[:, 0], poshis[:, 6] * 180 / sp.pi, 'b-')
plt.ylabel(ylabel)
plt.xlabel(xlabel)

plt.twinx()
plt.plot(lemehis[:, 0], lemehis[:, 1] * 180 / sp.pi, 'r--')
plt.grid(True)
plt.ylabel('$\delta_R$')
if abs(mi) > ma:
  plt.axis([poshis[0,0], poshis[-1,0], mi, abs(mi) ])
else:
  plt.axis([poshis[0,0], poshis[-1,0], -ma, ma ])
plt.savefig(dirzz + TipoModelo +'_zz.' + formato, format=formato)
plt.clf()

#Ângulo de deriva
if adi:
    ylabel = r'$\beta$'
    xlabel = r'$t \prime$'
else:
    ylabel = r'$\beta$'
    xlabel = r'$t $'

plt.plot(betahis[:, 0], betahis[:, 1], 'b-')    
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.ylabel(r'$\beta$ arctan ($\frac{-v}{u}$)')
plt.savefig(dirzz + TipoModelo +'_beta.' + formato, format=formato)
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
plt.plot(velhis[:, 0], velhis[:, 1], 'b-', label = r'$u$')
plt.savefig(dirzz + TipoModelo +'_u.' + formato, format=formato)
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
plt.plot(velhis[:, 0], velhis[:, 2], 'b-', label = r'$v$')
plt.savefig(dirzz + TipoModelo +'_v.' + formato, format=formato)
plt.clf()


#
#Velocidade de yaw

if adi:
    ylabel = r'$r\prime$'
    xlabel = r't'
else:
    ylabel = r'$r \quad s^{-1}$'
    xlabel = r't \ seg'

plt.plot(velhis[:, 0], velhis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot\psi$')
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_r.' + formato, format=formato)
plt.clf()
#
#Velocidade de roll   

if adi:
    ylabel = r'$ p\prime$'   
else:
    ylabel = r'$p \quad m\times s^{-1}$'

plt.plot(velhis[:, 0], velhis[:, 4], 'b-', label = r'$\dot \phi$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_p.' + formato, format=formato)
plt.clf()
    
#orientação roll

plt.plot(poshis[:, 0], poshis[:, 4], 'b-', label = r'$\phi$')
plt.grid(True)
plt.ylabel(r'$\phi$')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_roll.' + formato, format=formato)
plt.clf()
    

#Aceleração
#dot u
if adi:
    ylabel = r'$\dot u \prime$'
else:
    ylabel = r'$\dot u \quad m\times s^{-2}$'
plt.plot(acelhis[:, 0], acelhis[:, 1], 'b-', label = r'$\dot u$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_dotu.' + formato, format=formato)
plt.clf()


#Dot v
if adi:
    ylabel = r'$\dot v \prime$'
else:
    ylabel = r'$\dot v \quad m\times s^{-2}$'

plt.plot(acelhis[:, 0], acelhis[:, 2], 'b-', label = r'$\dot v$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_dotv.' + formato, format=formato)
plt.clf()


#Aceleração de yaw
if adi:
    ylabel = r'$\dot r \prime$'
else:
    ylabel = r'$\dot r \quad m\times s^{-2}$'

plt.plot(acelhis[:, 0], acelhis[:, 6]*(180/sp.pi), 'b-', 
label = r'$\dot \psi$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_dotr.' + formato, format=formato)
plt.clf()

#Aceleração de roll
if adi:
    ylabel = r'$\dot p \prime$'
else:
    ylabel = r'$\dot p \quad m\times s^{-2}$'

plt.plot(acelhis[:, 0], acelhis[:, 4]*(180/sp.pi), 'b-', label = r'$$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.ylabel(r'$\delta_R$')
plt.savefig(dirzz + TipoModelo +'dotp.' + formato, format=formato)
plt.clf()


#Forças
#Forças em surge
if adi:
    ylabel = r'$F_x \prime$'
else:
    ylabel = r'$F_x \quad N$'

plt.plot(forhis[:, 0], forhis[:, 1], 'b-', label = r'$F_x$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_fx.' + formato, format=formato)
plt.clf()


#Força em Sway
if adi:
    ylabel = r'$F_y \prime$'
else:
    ylabel = r'$F_y \quad N $'
    
plt.plot(forhis[:, 0], forhis[:, 2], 'b-', label = r'$F_y$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_fy.' + formato, format=formato)
plt.clf()


#Momento de yaw
if adi:
    ylabel = r'$N \prime$'
else:
    ylabel = r'$N \quad N \times m$'

plt.plot(forhis[:, 0], forhis[:, 6], 'b-', label = r'$N$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo + '_n.' + formato, format=formato)
plt.clf()

#Momento de Roll
if adi:
    ylabel = r'$K \prime$'
else:
    ylabel = r'$K \quad N \times m$'

plt.plot(forhis[:, 0], forhis[:, 4], 'b-', label = r'$K$')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo + '_k.' + formato, format=formato)
plt.clf()


#Rotação da máquina
plt.plot(prophis[:, 0], prophis[:, 1], 'o-', label = r'$rot$')
plt.grid(True)
plt.ylabel(r'$\ \quad rot \times s^{-1}$ ')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_rot.' + formato, format=formato)
plt.clf()


#eta
plt.plot(etahis[:, 0], etahis[:, 1], '--', label = r'$\eta$')
plt.grid(True)
plt.ylabel(r'$\eta$ ')
plt.xlabel(xlabel)
plt.grid(True)
plt.savefig(dirzz + TipoModelo +'_eta.' + formato, format=formato)
plt.clf()