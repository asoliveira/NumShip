# -*- coding: utf-8 -*-


#Dados de entrada
formato = 'pdf'
dire = 'fig'
if 'qtd' not in dir():
  qtd = 4
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
  
  if mi == abs(mi):
    mi = 0.8 * mi
  else:
    mi = 1.2 * mi
  
  if ma == abs(ma):
    ma = 1.2 * ma
  else:
    ma = 0.8 * ma
    
  if mi == ma:
    ma = 1.3*mi
    if mi == 0:
      ma = 1
      mi = -1
    
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
    if ('bench' not in arqgiro):
      #faz a leitura do dicionario no arq 'relcg.py'
      f(arqgiro, girodic)
    
      #Procura a existência do arquivo benchmak
      if os.path.exists(arqgiro + '/' + pasta + '_cg.dat' ) and qtd==2:
        #Cria uma classe para a leitura do benchmark e transformação em dicionário
        datain = ('',arqgiro + '/' + pasta + '_cg.dat' , '')
        datain = es(datain)
        #cria dicionário com o benchmark
        girodatain[pasta] = datain.lerarqder()    
    elif qtd==3 or qtd == 4:
      f(arqgiro, girodatain)
    
  arqzz = pasta + '/zigzag'
  if os.path.isdir(arqzz):
    if ('bench' not in arqzz):
      #faz a leitura do dicionario no arq 'relzz.py'
      f(arqzz, zzdic)

      #Procura a existência do arquivo benchmak
      if os.path.exists(arqzz + '/' + pasta + '_zz.dat' ) and qtd == 2:
        #Cria uma classe para a leitura do benchmark e transformação em dicionário
        datain = ('',arqzz + '/' + pasta + '_zz.dat' , '')
        datain = es(datain)
        #cria dicionário com o benchmark
        zzdatain[pasta] = datain.lerarqder()
    elif qtd==3 or qtd == 4:
      f(arqzz, zzdatain)
 
if qtd==3 or qtd == 4:
  if girodatain:
    k =girodatain.keys()[-1]
    for i in girodic.keys():
      girodatain[i] = girodatain[k]
    girodatain.pop(k)

  if zzdatain:
    k =zzdatain.keys()[-1]
    for i in zzdic.keys():
      zzdatain[i] = zzdatain[k]
    zzdatain.pop(k)    
#Estas serão plotadas mais adiante quando forem adicionado os valores                
if girodic:
  listnavio = girodic.keys()
else:
  listnavio = zzdic.keys()
    
comp = len(listnavio)

if listnavio:
  listav = []
  listtrans = []
  listdiamt = []

compzz = len(zzdic.keys())
if compzz != 0:
  list1oversh = []
  list2oversh = []
  list3oversh = []
  #listdit1ex  = sp.zeros(comp)
  #listdist1os = sp.zeros(comp)
  listtemp1os = []
  listtempreach = []


#Criando lista para os dados utilizados como benchmark
lnav_per = girodatain.keys()
comp_in = len(lnav_per)
if comp_in != 0:   
  lav_per = list(sp.zeros(comp_in))
  ltrans_per = list(sp.zeros(comp_in))
  ldiamt_per = list(sp.zeros(comp_in))

zznav_per = zzdatain.keys()
compzz_in = len(zznav_per)  
if compzz_in != 0:
  l1o_per = list(sp.zeros(compzz_in))
  l2o_per = list(sp.zeros(compzz_in))  
  l3o_per = list(sp.zeros(compzz_in))
  lt1o_per = list(sp.zeros(compzz_in))
  ltr_per = list(sp.zeros(compzz_in))
  #ldist1ex_per = sp.zeros(compzz_in)
  #ldist1os_per = sp.zeros(compzz_in)
 
#
#Plotando a curva de giro
if girodic:
  for n in listnavio:
    listav.append(girodic[n]['avanco'])
    listtrans.append(girodic[n]['trans'])    
    listdiamt.append(girodic[n]['dt'])
    
    if girodatain: 
      if n in lnav_per:
        i = lnav_per.index(n)
        lav_per[i] = (girodatain[n]['avanco'] - 
        girodic[n]['avanco'])/girodic[n]['avanco']
        
        ltrans_per[i] = ( girodatain[n]['trans'] - 
        girodic[n]['trans'])/girodic[n]['trans']
        
        ldiamt_per[i] = (girodatain[n]['dt'] - 
        girodic[n]['dt'])/girodic[n]['dt']

  #Plotar os resultados simulados  
  listav = sp.array(listav)    
  listtrans = sp.array(listtrans)    
  listdiamt = sp.array(listdiamt)
  
  svplt(listav, 'avanco', listnavio)    
  svplt(listtrans, 'transferenia', listnavio)    
  svplt(listdiamt, 'diametro_tat', listnavio)  

  #Plotar a diferença resultados simulados com o benchmark
  lav_per = sp.array(lav_per)    
  ltrans_per = sp.array(ltrans_per)
  ldiamt_per = sp.array(ldiamt_per)
   
  svplt(lav_per, 'avanco_per', lnav_per)    
  svplt(ltrans_per, 'transferenia_per', lnav_per)    
  svplt(ldiamt_per, 'diametro_tat_per', lnav_per)   

#
#Plotando a curva de zigzag
  
if zzdic:
  for n in listnavio:
    list1oversh.append(zzdic[n]['o1'])
    list2oversh.append(zzdic[n]['o2'])
    list3oversh.append(zzdic[n]['o3'])
    
    #Verificar se vou programar
    #listdist1ex[ind] = zzdic[listnavio[ind]]['dl1e']
    #listdist1os[ind] = zzdic[listnavio[ind]]['os1e']
    listtemp1os.append(zzdic[n]['t1ex'])
    listtempreach.append(zzdic[n]['reach'])

    if zzdatain: 
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

if zzdatain:

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