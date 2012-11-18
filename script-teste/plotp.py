# -*- coding: utf-8 -*-


#Dados de entrada
formato = 'pdf'
dire = 'fig'
qtd = 2
arq_bin = 'log.bin'

###############################
import os
import sys
import pickle
import matplotlib.pyplot as plt
import scipy as sp
if os.getcwd().split('saida')[-2] not in sys.path:
  caminho = os.getcwd().split('saida')[-2] + '/source'
  sys.path.append(os.path.abspath(caminho))
from Es import *

#
#funções
#
def f(arq,dic):
  """ler arq em formato binário e devolve ele como o dicionário dic"""
  listarq = os.listdir(arq) 
  if arq_bin in listarq:
    sys.path.insert(0, os.path.abspath(arq))
    #abrir o arquivo para leitura - o "b" significa que o arquivo é binário 
    arq = open(arq + '/' + arq_bin,'rb') 
    #Ler a stream a partir do arquivo e reconstrói o objeto original.
    dic[pasta] = pickle.load(arq)
    #fechar o arquivo
    arq.close() 
    
def svplt(lista, string, listnavio, formato = formato):
  """Salva as plotagem"""
  
  #import pdb
  #pdb.set_trace()
  
  comp = len(lista)
  
  #Coloca os nomes embaixo do eixo x  
  plt.xticks(range(comp),listnavio) 
      
  #plota  
  #plt.bar(range(comp), lista)
  markerline, stemlines, baseline = plt.stem(range(comp), lista,  linefmt='b-', markerfmt='bo', basefmt='r-')#, bottom=None, label=None)
  #plt.setp(markerline, 'markerfacecolor', 'b')                  '-.',
  #plt.setp(baseline, 'color','r', 'linewidth', 2)
  #plt.setp(stemlines, 'color', 'b')
  
  #colocando o tamanho dos eixos a serem plotados
  mi = lista.min()
  ma = lista.max()
  
  if abs(mi) < abs(ma):
    maior = abs(ma)
  else:
    maior = abs(mi)
  
  if mi == abs(mi):
    mi = 0.6 * maior
  else:
    mi = -1.4 * maior
  
  if ma == abs(ma):
    ma = 1.4 * maior
  else:
    ma = -0.6 * maior
    
  plt.axis([-0.1*comp, 1.1*comp, mi, ma])  
  
  #Salva figuras
  plt.savefig(dire + '/' + string+'.'+ formato, format=formato)
  plt.clf()

  
  
#
#código
#  
#dicionario que irá receber um suposto dicionário com os dados do do 
#script relatório de parâmetros simulados
girodic = {}
zzdic = {}
#dicionario que irá receber um suposto dicionário com os dados benchmark
girodatain = {}
zzdatain = {}

#cria o diretório para salvar os gráficos  
if not os.path.exists(dire):
  os.mkdir(dire)
  
#procura o caminho onde está localizado os dados      
listnavio = os.listdir('.')
for navio in listnavio:
  if os.path.isfile(navio):
    listnavio.remove(navio)

#salva os parâmetros no dicionário    
for pasta in listnavio:
  arqgiro = pasta + '/giro'
  if os.path.isdir(arqgiro):
    #faz a leitura do dicionario no arq 'relcg.py'
    f(arqgiro, girodic)
    
    #Procura a existência do arquivo benchmak
    if os.path.exists(arqgiro + '/' + pasta + '_cg.dat' ) and qtd==2:
      #Cria uma classe para a leitura do benchmark e transformação em dicionário
      datain = ('',arqgiro + '/' + pasta + '_cg.dat' , '')
      datain = es(datain)
      #cria dicionário com o benchmark
      girodatain[pasta] = datain.lerarqder()    
  
  arqzz = pasta + '/zigzag'
  if os.path.isdir(arqzz):
    #faz a leitura do dicionario no arq 'relzz.py'
    f(arqzz, zzdic)

    #Procura a existência do arquivo benchmak
    if os.path.exists(arqzz + '/' + pasta + '_zz.dat' ) and qtd == 2:
      #Cria uma classe para a leitura do benchmark e transformação em dicionário
      datain = ('',arqzz + '/' + pasta + '_zz.dat' , '')
      datain = es(datain)
      #cria dicionário com o benchmark
      zzdatain[pasta] = datain.lerarqder()

#Estas serão plotadas mais adiante quando forem adicionado os valores                
listnavio = girodic.keys()
comp = len(listnavio)

if comp != 0:
  listav = []
  listtrans = []
  listdiamt = []

compzz = len(zzdic.keys())
if compzz != 0:
  list1oversh = list(sp.zeros(comp))
  list2oversh = list(sp.zeros(comp))
  list3oversh = list(sp.zeros(comp))
  #listdit1ex  = sp.zeros(comp)
  #listdist1os = sp.zeros(comp)
  listtemp1os = list(sp.zeros(comp))
  listtempreach = list(sp.zeros(comp))


#Criando lista para os dados utilizados como benchmark
if len(girodatain.keys()) != 0:  
  lnav_per = girodatain.keys()
  comp_in = len(lnav_per) 
  lav_per = list(sp.zeros(comp_in))
  ltrans_per = list(sp.zeros(comp_in))
  ldiamt_per = list(sp.zeros(comp_in))

if len(zzdatain.keys()) != 0:
  zznav_per = zzdatain.keys()
  compzz_in = len(zznav_per)
  l1o_per = list(sp.zeros(compzz_in))
  l2o_per = list(sp.zeros(compzz_in))  
  l3o_per = list(sp.zeros(compzz_in))
  lt1o_per = list(sp.zeros(compzz_in))
  ltr_per = list(sp.zeros(compzz_in))
  #ldist1ex_per = sp.zeros(compzz_in)
  #ldist1os_per = sp.zeros(compzz_in)

  
#
#Plotando a curva de giro
if comp!=0:
  for n in listnavio:
    listav.append(girodic[n]['avanco'])
    listtrans.append(girodic[n]['trans'])    
    listdiamt.append(girodic[n]['dt'])
    
    if comp_in != 0: 
      if n in lnav_per:
        i = lnav_per.index(n)
        lav_per.insert(i, (girodatain[n]['avanco'] - 
        girodic[n]['avanco'])/girodic[n]['avanco'])
        
        ltrans_per.insert(i, ( girodatain[n]['trans'] - 
        girodic[n]['trans'])/girodic[n]['trans'])    
        
        ldiamt_per.insert(i, (girodatain[n]['dt'] - 
        girodic[n]['dt'])/girodic[n]['dt'])
      
if len(girodic.keys()) != 0:
  #Plotar os resultados simulados  
  listav = sp.array(listav)    
  listtrans = sp.array(listtrans)    
  listdiamt = sp.array(listdiamt)
  
  svplt(listav, 'avanco', listnavio)    
  svplt(listtrans, 'transferenia', listnavio)    
  svplt(listdiamt, 'diametro_tat', listnavio)  

#Plotar a diferença resultados simulados com o benchmark
if len(girodatain.keys()) != 0:
  lav_per = sp.array(lav_per)    
  ltrans_per = sp.array(ltrans_per)
  ldiamt_per = sp.array(ldiamt_per)
  
  svplt(lav_per, 'avanco_per', listnavio)    
  svplt(ltrans_per, 'transferenia_per', listnavio)    
  svplt(ldiamt_per, 'diametro_tat_per', listnavio)   

#
#Plotando a curva de zigzag
  
if compzz!=0:
  for n in listnavio:
    list1oversh.append(zzdic[n]['o1'])
    list2oversh.append(zzdic[n]['o2'])
    list3oversh.append(zzdic[n]['o3'])
    
    #Verificar se vou programar
    #listdist1ex[ind] = zzdic[listnavio[ind]]['dl1e']
    #listdist1os[ind] = zzdic[listnavio[ind]]['os1e']
    listtemp1os.append(zzdic[n]['t1ex'])
    listtempreach.append(zzdic[n]['reach'])

    if compzz_in != 0: 
      if n in zznav_per:
        y = zznav_per.index(n)
        l1o_per[y] = (zzdatain[n]['o1'] - 
        zzdic[n]['o1'])/zzdic[n]['o1']
        
        l2o_per[y] = (zzdatain[n]['o2'] - 
        zzdic[n]['o2'])/zzdic[n]['o2']    
        
        l3o_per[y] = (zzdatain[n]['o3'] - 
        zzdic[n]['o3'])/zzdic[n]['o3']

        lt1o_per[y] = (zzdatain[n]['t1ex'] - 
        zzdic[n]['t1ex'])/zzdic[n]['t1ex']                  

        ltr_per[y] = (zzdatain[n]['reach'] - 
        zzdic[n]['reach'])/zzdic[n]['reach'] 
        
if len(zzdic.keys()) != 0:                 
  #Plotar os resultados simulados  
  list1oversh = sp.array(list1oversh)
  list2oversh = sp.array(list2oversh)
  list3oversh = sp.array(list3oversh)
  listtemp1os = sp.array(listtemp1os)
  listtempreach = sp.array(listtempreach)  
  
  svplt(list1oversh, '1overshoot', listnavio)  
  svplt(list2oversh, '2overshoot', listnavio)    
  svplt(list3oversh, '3overshoot', listnavio)

  svplt(listtemp1os, 't1ex', listnavio)      
  svplt(listtempreach, 'reach', listnavio)  

if len(zzdatain.keys()) != 0:
  l1o_per = sp.array(l1o_per)
  l2o_per = sp.array(l2o_per)
  l3o_per = sp.array(l3o_per)
  lt1o_per = sp.array(lt1o_per)
  ltr_per = sp.array(ltr_per)  
  
  svplt(l1o_per, '1overshoot_per', zznav_per)    
  svplt(l2o_per, '2overshoot_per', zznav_per)    
  svplt(l3o_per, '3overshoot_per', zznav_per)
  
  svplt(lt1o_per, 't1ex_per', zznav_per)     
  svplt(ltr_per, 'reach_per', zznav_per)