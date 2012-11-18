# -*- coding: utf-8 -*-

#nome do arquivo em que será salvo
nome_arq = 'logzz'
#É para salvar arq=True ou mostra na tela arq=False
salvar = True

import pickle #modulo pickle
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from config import *

pos = np.genfromtxt('pos.dat')
#betaHis = np.genfromtxt('beta.dat')
vel = np.genfromtxt('velo.dat')
#lemeHis = np.genfromtxt('leme.dat')
#acelHis = np.genfromtxt('acel.dat')
#forHis = np.genfromtxt('.forcas.dat')
#etaHis = np.genfromtxt('eta.dat')
#propHis = np.genfromtxt('propulsor.dat')

#i indexa o momento em que a proa atinge execução
i = 0
execucao = 0
while (abs(pos[i,6] - pos[0,6]) <= abs((sp.pi/180)*(proazz))): i += 1
execucao += 1

o1 = i
#o1 indexa o momento em que a proa alcança o primeiro overshoot
while abs(pos[o1 + 1,6]) > abs(pos[o1,6]): o1 += 1  

#r  indexa o reach
r = o1 
if pos[r,6] > 0:
  while pos[r,6] >= pos[0,6]: r += 1
else:
  while pos[r,6] <= pos[0,6]: r += 1

#i2 indexa o momento em que a proa atinge a segunda execução
i2 = r
while (abs(pos[i2,6] - pos[0,6]) <= abs((sp.pi/180)*(proazz))): i2 += 1
execucao += 1
  
#indexa o momento em que a proa alcança o segundo overshoot
o2 = i2
while abs(pos[o2 + 1,6]) > abs(pos[o2,6]): o2 += 1  

#i indexa o momento em que a proa atinge a terceira execução
i3 = o2
while (abs(pos[i3,6] - pos[0,6]) >= abs((sp.pi/180)*(proazz))): i3 += 1  
while (abs(pos[i3,6] - pos[0,6]) <= abs((sp.pi/180)*(proazz))): i3 += 1
execucao += 1
#indexa o momento em que a proa alcança o terceiro overshoot
o3 = i3
while abs(pos[o3 + 1,6]) > abs(pos[o3,6]): o3 += 1 
  
##Overshoot path  
#p1 indexa o momento em que a proa alcança o primeiro overshoot
p1 = i
while abs(pos[p1 + 1,2]) > abs(pos[p1,2]): p1 += 1  

dici = {}
dici['dl1e'] = pos[i,2]#distância lateral na primeira execução
dici['os1e'] = abs(pos[p1,2] - pos[i,2])#overshoot lateral na primeira execução

#mudança de proa na primeira execução
dici['proa1ex'] = pos[i,6]
#tempo para mudar a proa na primeira execução
dici['t1ex'] = pos[i,0]

dici['reach'] = pos[r,0]
#primeiro overshoot
dici['o1'] = (abs(pos[o1,6]) * 180/sp.pi) - proazz
#segundo overshoot
dici['o2'] = (abs(pos[o2,6]) * 180/sp.pi) - proazz
#terceiro overshoot
dici['o3'] = (abs(pos[o3,6]) * 180/sp.pi) - proazz

arq = open('log.bin','wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
pickle.dump(dici,arq) #Grava uma stream do objeto "dic" para o arquivo.
arq.close() #fechar o arquivo
#
#Imprimindo

if salvar:
  log = open(nome_arq, 'w')
  log.write('Distancia lateral percorrida no \n\
  momento da primeira execução {0:.2f}m ou {1:.2f}ft\n'.format(dici['dl1e'], dici['dl1e']*3.28))
  log.write('Overshoot da distancia lateral  percorrida \n\
   {0:.2f} ou {1:.2f}ft\n'.format(dici['os1e'],dici['os1e']*3.28))
   
  log.write('Tempo para mudara a proa {0:.2f} \
  {1:.0f}\n'.format(dici['proa1ex']*180/sp.pi, dici['t1ex']))

  log.write('Tempo para alcançar o Reach \
  {0:.2f}\n'.format(dici['reach']))

  log.write('Overshoot 1 {0:.2f}\n'.format(dici['o1']))

  log.write('Overshoot 2 {0:.2f}\n'.format(dici['o2'])) 

  log.write('Overshoot 3 {0:.2f}\n'.format(dici['o3']))
elif not salvar:
  print 'Distancia lateral percorrida no \n\
  momento da primeira execução {0:.2f}m ou {1:.2f}ft\n'.format(dici['dl1e'], dici['dl1e']*3.28)
  
  print 'Overshoot da distancia lateral  percorrida \n\
   {0:.2f} ou {1:.2f}ft\n'.format(dici['os1e'],dici['os1e']*3.28)
   
  print 'Tempo para mudara a proa {0:.2f} \
  {1:.0f}\n'.format(dici['proa1ex']*180/sp.pi, dici['t1ex'])

  print 'Tempo para alcançar o Reach \
  {0:.2f}\n'.format(dici['reach'])

  print 'Overshoot 1 {0:.2f}\n'.format(dici['o1'])

  print 'Overshoot 2 {0:.2f}\n'.format(dici['o2']) 

  print 'Overshoot 3 {0:.2f}\n'.format(dici['o3'])