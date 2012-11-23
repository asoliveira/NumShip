# -*- coding: utf-8 -*-

#nome do arquivo em que será salvo
nome_arq = 'logcg'
#É para salvar arq=True ou mostra na tela arq=False
salvar = True

import pickle
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

pos = np.genfromtxt('pos.dat')
#betaHis = np.genfromtxt('beta.dat')
vel = np.genfromtxt('velo.dat')
#lemeHis = np.genfromtxt('leme.dat')
#acelHis = np.genfromtxt('acel.dat')
#forHis = np.genfromtxt('.forcas.dat')
#etaHis = np.genfromtxt('eta.dat')
#propHis = np.genfromtxt('propulsor.dat')

#índice da transferência
i = 0
while abs(pos[i,6] - pos[0,6]) < (sp.pi/2): i += 1

#índice do diâmetro tático
j = i
while abs(pos[j,6] - pos[0,6]) < (sp.pi): j += 1

k = j
#índice quando atinge o equilíbrio
while (vel[k,6] != vel[k+100,6]): k += 1
while (vel[k,1] != vel[k+100,1]): k += 1
while (vel[k,2] != vel[k+100,2]): k += 1  

dici = {}
dici['V'] = sp.sqrt(vel[k,1]**2 + vel[k,2]**2)
dici['u'] = vel[k,1]
dici['v'] = vel[k,2]
dici['r'] = vel[k,6]
dici['raio'] = sp.sqrt(vel[-1,2]**2 + vel[-1,1]**2)/vel[-1,6]
dici['dt'] = pos[j,2] #diâmetro tático
dici['trans'] = pos[i,2] #transferência
dici['avanco'] = pos[i,1]
dici['t90'] = pos[i,0]
dici['t180'] = pos[j,0]

#abrir o arquivo para gravação - o "b" significa que o arquivo é binário
arq = open('log.bin','wb') 
pickle.dump(dici,arq) #Grava uma stream do objeto "dic" para o arquivo.
arq.close() #fechar o arquivo


if salvar:
  log = open(nome_arq, 'w') 
  log.write('Tempo para mudara a proa {0:.2f} \
  {1:.0f} \n'.format(pos[i,6]*(180/sp.pi), dici['t90']))
  log.write('Tempo para mudara a proa {0:.2f} \
  {1:.0f} \n'.format(pos[j,6]*(180/sp.pi), dici['t180']))
  log.write('Avanço {0:.2f}m ou {1:.2f}ft \n'.format(dici['avanco'], dici['avanco']*3.28))
  log.write('Transferência {0:.2f}m ou {1:.2f}ft \n'.format(dici['trans'], dici['trans']*3.28))
  log.write('Diâmetro tático {0:.2f}m ou {1:.2f}ft \n'.format(dici['dt'],
  dici['dt']*3.28))
  log.write('Raio da Curva de Giro no Equilíbrio \
  {0:.2f}m ou {1:.2f}ft \n'.format(dici['raio'], dici['raio'] * 3.28))
  log.write('u no equilíbrio {0:.2f} ou {1:.2f}knots \n'.format(dici['u'], dici['u']*1.94))
  log.write('v no equilíbrio {0:.2f} ou {1:.2f}knots \n'.format(dici['v'], dici['v']*1.94))
  log.write('r no equilíbrio {0:.2f} \n'.format(dici['r']))
  log.write('Velocidade total {0:.2f}m/s ou {1:.2f}knots \n'.format(dici['V'] , 
  dici['V'] *1.94))
  log.close()
elif not salvar:
  print 'Tempo para mudara a proa {0:.2f} \
  {1:.0f} \n'.format(pos[i,6]*(180/sp.pi), dici['t90'])
  print 'Tempo para mudara a proa {0:.2f} \
   {1:.0f} \n'.format(pos[j,6]*(180/sp.pi), dici['t180'])
  print 'Avanço {0:.2f}m ou {1:.2f}ft \n'.format(dici['avanco'], dici['avanco']*3.28)
  print 'Transferência {0:.2f}m ou {1:.2f}ft \n'.format(dici['trans'], dici['trans']*3.28)
  print 'Diâmetro tático {0:.2f}m ou {1:.2f}ft \n'.format(dici['dt'],
  dici['dt']*3.28)
  print 'Diâmetro da Curva de Giro no Equilíbrio \
  {0:.2f}m ou {1:.2f}ft \n'.format(2 * dici['raio'], 2 * dici['raio'] * 3.28)
  print 'u no equilíbrio {0:.2f} ou {1:.2f}knots \n'.format(dici['u'], dici['u']*1.94)
  print 'v no equilíbrio {0:.2f} ou {1:.2f}knots \n'.format(dici['v'], dici['v']*1.94)
  print 'r no equilíbrio {0:.2f} ou {1:.2f}knots \n'.format(dici['r'])
  print 'Velocidade total {0:.2f}m/s ou {1:.2f}knots \n'.format(dici['V'] , 
  dici['V'] *1.94)
