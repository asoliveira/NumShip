# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-cg-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'pos.dat',
#legendas
ld = (r'$X_{\delta \delta \eta \eta} = 0.0$', 
r'$X_{\delta \delta \eta \eta} = 0.002$', 
r'$X_{\delta \delta \eta \eta} = 0.005$',
r'$X_{\delta \delta \eta \eta} = 0.008$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


dircg = scgarq + '/figuras/'   
if not os.path.exists(dircg):
  os.makedirs(dircg)
  
pos = []
for arg in p:
  pos.append(arg + dircomum + arq[0])

posHis = []

for arg in pos:
  posHis.append(np.genfromtxt(arg))


#Curva de giro
fig = plt.figure()
ax = fig.add_subplot(111)
if adi:
    ylabel = r'$x\prime$'
    xposlabel = r'$y\prime$'
else:
    ylabel = r'$x \quad m$'    
    xposlabel = r'$y \quad m$'    

for a in range(len(posHis)):
  ax.plot(posHis[a][:,2], posHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xposlabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

