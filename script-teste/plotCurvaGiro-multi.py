# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#posHis
adi = False
save = True #Salva a figura?
scgarq = 'plot'
formato = 'pdf'
TipoModelo = 'r-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35

#Quais são as pastas?
p = ('padrao', 'r/r-10', 'r/r-20', 'r/r-30')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'pos.dat',
#legendas
ld = (r'$S1$', 
r'$10\% \ R$', 
r'$20\% \ R$',
r'$30\% \ R$')


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

