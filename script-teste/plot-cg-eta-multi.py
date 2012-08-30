# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#etaHis
adi = False
save = True #Salva a figura?
scgarq = 'saida'
formato = 'pdf'
TipoModelo = 'marad-cg-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
aeta = [tini, tmax, 0, 4]

#Quais são as pastas?
p = ('padrao', 'xddee-0.002', 'xddee-0.005', 'xddee-0.008')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'eta.dat',
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
  
eta = []
for arg in p:
  eta.append(arg + dircomum + arq[0])

etaHis = []

for arg in eta:
  etaHis.append(np.genfromtxt(arg))


#Curva de giro
fig = plt.figure()
ax = fig.add_subplot(111)
if adi:
  ylabel = r'$\eta \prime$'    
  xetalabel = r'$t \quad \prime$'    
else:
  ylabel = r'$\eta (graus)$'    
  xetalabel = r'$t \quad (segundos)$'    

plt.axis(aeta)    
for a in range(len(etaHis)):
  ax.plot(etaHis[a][:,0], etaHis[a][:,1])
leg = ax.legend(ld, loc = 'upper right')
plt.grid(True)
plt.ylabel(ylabel)
plt.xlabel(xetalabel)
 
if save:
    plt.savefig(dircg + TipoModelo +'eta-cg.' + formato, format=formato)
    plt.clf()
else:
    plt.show()
    plt.clf()

