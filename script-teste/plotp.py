# -*- coding: utf-8 -*-


#Dados de entrada
formato = 'pdf'
dire = 'fig'

###############################
import os
import sys
import pickle
import matplotlib.pyplot as plt
import scipy as sp
if os.path.abspath('../source') not in sys.path:
  sys.path.append(os.path.abspath('../source'))
from Es import *

#
#funções
#
def f(arq,dic):
  listarq = os.listdir(arq) 
  if 'log.bin' in listarq:
    sys.path.insert(0, os.path.abspath(arq))
    arq = open(arq + '/log.bin','rb') #abrir o arquivo para leitura - o "b" significa que o arquivo é binário
    dic[pasta] = pickle.load(arq)#Ler a stream a partir do arquivo e reconstroi o objeto original.
    arq.close() #fechar o arquivo
    
def svplt(lista, string, listnavio, formato = formato):
  """Salva as plotagem"""
  comp = len(listnavio)
  
  #Coloca os nomes embaixo do eixo x  
  plt.xticks(range(comp),listnavio) 
  
  #plota  
  markerline, stemlines, baseline = plt.stem(range(comp), lista, '-.')
  plt.setp(markerline, 'markerfacecolor', 'b')
  plt.setp(baseline, 'color','r', 'linewidth', 2)
  plt.setp(stemlines, 'color', 'b')
  #colocando o tamanho dos eixos a serem plotados
  mi = lista.min()
  ma = lista.max()
  plt.axis([-0.1*comp, 1.1*comp, 0.2*mi + mi , 0.2*ma+ma])
  #Salva figuras
  plt.savefig(dire + '/' + string+'.'+ formato, format=formato)
  plt.clf()

  
  
#
#código
#  
girodic = {}
zzdic = {}
girodatain = {}
zzdatain = {}
  
if not os.path.exists(dire):
  os.mkdir(dire)    
listnavio = os.listdir('.')
for navio in listnavio:
  if os.path.isfile(navio):
    listnavio.remove(navio)

for pasta in listnavio:
  arqgiro = pasta + '/giro'
  if os.path.isdir(arqgiro):
    #faz a leitura do dicionario no arq 'relcg.py'
    f(arqgiro, girodic)
    
    datain = ('',arqgiro + '/' + pasta + '_cg.dat' , '')
    datain = es(datain)
    girodatain[pasta] = datain.lerarqder()    
  
  arqzz = pasta + '/zigzag'
  if os.path.isdir(arqzz):
    #faz a leitura do dicionario no arq 'relzz.py'
    f(arqzz, zzdic)

listnavio = girodic.keys()
comp = len(listnavio)

listav = sp.zeros(comp)
listtrans = sp.zeros(comp)
listdiamt = sp.zeros(comp)

list1oversh = sp.zeros(comp)
list2oversh = sp.zeros(comp)
list3oversh = sp.zeros(comp)
#listdit1ex  = sp.zeros(comp)
#listdist1os = sp.zeros(comp)
listtemp1os = sp.zeros(comp)
listtempreach = sp.zeros(comp)

#Criando lista para os dados utilizados como benchmark
if len(girodatain.keys()) != 0:  
  lnav_per = girodatain.keys()
  comp_in = len(lnav_per) 
  lav_per = sp.zeros(comp_in)
  ltrans_per = sp.zeros(comp_in)
  ldiamt_per = sp.zeros(comp_in) 

if len(zzdatain.keys()) != 0:
  zznav_per = zzdatain.keys()
  compzz_in = len(zznav_per)
  l1o_per = sp.zeros(compzz_in)
  l2o_per = sp.zeros(compzz_in)  
  l3o_per = sp.zeros(compzz_in)
  lt1o_per = sp.zeros(compzz_in)
  ltr_per = sp.zeros(compzz_in)
  #ldist1ex_per = sp.zeros(compzz_in)
  #ldist1os_per = sp.zeros(compzz_in)
#
#Plotando a curva de giro
if len(girodic.keys())!=0:
  for ind in range(comp):
    listav[ind] = girodic[listnavio[ind]]['avanco']
    listtrans[ind] = girodic[listnavio[ind]]['trans']    
    listdiamt[ind] = girodic[listnavio[ind]]['dt']
    
    if len(girodatain.keys()) != 0: 
      if listnavio[ind] in lnav_per:
        y = lnav_per.index(listnavio[ind])
        lav_per[y] = (girodatain[lnav_per[y]]['avanco'] - 
        girodic[listnavio[ind]]['avanco'])/girodic[listnavio[ind]]['avanco']
        
        ltrans_per[y] = (girodatain[lnav_per[y]]['trans'] - 
        girodic[listnavio[ind]]['trans'])/girodic[listnavio[ind]]['trans']    
        
        ldiamt_per[y] = (girodatain[lnav_per[y]]['dt'] - 
        girodic[listnavio[ind]]['dt'])/girodic[listnavio[ind]]['dt']
      

  #Plotar os resultados simulados  
  svplt(listav, 'avanco', listnavio)    
  svplt(listtrans, 'transferenia', listnavio)    
  svplt(listdiamt, 'diametro_tat', listnavio)  
  
  #Plotar a diferença resultados simulados com o benchmark
  if len(girodatain.keys()) != 0:
    svplt(lav_per, 'avanco_per', lnav_per)    
    svplt(ltrans_per, 'transferenia_per', lnav_per)    
    svplt(ldiamt_per, 'diametro_tat_per', lnav_per)   

#
#Plotando a curva de zigzag  
if len(zzdic.keys())!=0:
  for ind in range(comp):
    list1oversh[ind] = zzdic[listnavio[ind]]['o1']
    list2oversh[ind] = zzdic[listnavio[ind]]['o2']
    list3oversh[ind] = zzdic[listnavio[ind]]['o3']
    
    #Verificar se vou programar
    #listdist1ex[ind] = zzdic[listnavio[ind]]['dl1e']
    #listdist1os[ind] = zzdic[listnavio[ind]]['os1e']
    listtemp1os[ind] = zzdic[listnavio[ind]]['t1ex']
    listtempreach[ind] = zzdic[listnavio[ind]]['1reach']

    if len(zzdatain.keys()) != 0: 
      if listnavio[ind] in zznav_per:
        y = zznav_per.index(listnavio[ind])
        l1o_per[y] = (zzdatain[zznav_per[y]]['o1'] - 
        zzdic[listnavio[ind]]['o1'])/zzdic[listnavio[ind]]['o1']
        
        l2o_per[y] = (zzdatain[zznav_per[y]]['o2'] - 
        zzdic[listnavio[ind]]['o2'])/zzdic[listnavio[ind]]['o2']    
        
        l3o_per[y] = (zzdatain[zznav_per[y]]['o3'] - 
        zzdic[listnavio[ind]]['o3'])/zzdic[listnavio[ind]]['o3']

        lt1o_per[y] = (zzdatain[zznav_per[y]]['o3'] - 
        zzdic[listnavio[ind]]['o3'])/zzdic[listnavio[ind]]['o3']                  

        ltr_per[y] = (zzdatain[zznav_per[y]]['o3'] - 
        zzdic[listnavio[ind]]['o3'])/zzdic[listnavio[ind]]['o3'] 
        
                 
  #Plotar os resultados simulados  
  svplt(list1oversh, '1overshoot', listnavio)  
  svplt(list2oversh, '2overshoot', listnavio)    
  svplt(list3oversh, '3overshoot', listnavio)

  svplt(listtemp1os, 't1ex', listnavio)      
  svplt(listtempreach, 'reach', listnavio)  

  if len(zzdatain.keys()) != 0:
    svplt(l1o_per, '1overshoot_per', zznav_per)    
    svplt(l2o_per, '2overshoot_per', zznav_per)    
    svplt(l3o_per, '3overshoot_per', zznav_per)
    
    svplt(lt1o_per, 't1ex_per', zznav_per)     
    svplt(ltr_per, 'reach_per', zznav_per)