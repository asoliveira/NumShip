# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#betaHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-cg-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
abeta = [tini, tmax, 0, 25]

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'beta.dat',
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
  
beta = []
for arg in p:
  beta.append(arg + dircomum + arq[0])

betaHis = []

for arg in beta:
  betaHis.append(np.genfromtxt(arg))


#Curva de giro
fig = plt.figure()
ax = fig.add_subplot(111)
if adi:
  ylabel = r'$\beta \prime$'    
  xbetalabel = r'$t \quad \prime$'    
else:
  ylabel = r'$\beta (graus)$'    
  xbetalabel = r'$t \quad (segundos)$'    

plt.axis(abeta)    
for a in range(len(betaHis)):
  ax.plot(betaHis[a][:,0], betaHis[a][:,1] * (180/sp.pi))
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xbetalabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'beta-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

