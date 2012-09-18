# -*- coding: utf-8 -*-

#Variáveis de entrada:
#dircg -- Diretório onde será salvo as gráfico;
#TipoModelo -- Também ficará como o nome de cada gráfico;
#velHis -- 
#etaHis
adi = False
save = True #Salva a figura?
scgarq = 'plot'
formato = 'pdf'
TipoModelo = 'r-'
GrausDeLib = 3
tini = 0
tmax = 900
lemecg = 35
aeta = [tini, tmax, 0, 4]

#Quais são as pastas?
p = ('padrao', 'r/r-10', 'r/r-20', 'r/r-30')
#Dentro de cada pasta quais são as pastas comuns?
dircomum = '/CurvaGiro/'
#Dentro de cada diretório quais são as arq?
arq = 'eta.dat',
#legendas
ld = (ur'S1', 
r'$10 \% R$', 
r'$20 \% R$',
r'$30 \% R$')


#import 
import os

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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
  ylabel = r'$\eta$'    
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

