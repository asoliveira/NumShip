# -*- coding: utf-8 -*-

#
#This file is part of a program called NumShip

#Copyright (C) 2011,2012  Alex Sandro Oliveira

#NumShip is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Algumas palavras teste 
"""

#imports
import os
import scipy as sp
from scipy import linalg
from scipy import stats

#Módulos criados
from Casco import  *
from Leme import  *
from Prop import *


class inte(object):
  """
  Classe que realiza a integração no tempo
  
  :version:0.0
  :author: Alex
  
  """
  
  
  def __init__(self):
    """
    """
    pass
    
  def rk4(self, function, x, t0, dt, par = None):
    """
    Integrador runge-kutta
    """
    k1 = function(x, t0, par)
    k2 = function(x + 1./2*dt*k1, t0 + 1./2*dt, par)
    k3 = function(x + 1./2*dt*k2, t0 + 1./2*dt, par)
    k4 = function(x + dt*k3, t0 + dt, par)
  
    xt = x + 1./6*(k1+ 2.*k2+ 2.*k3+ k4)*dt
  
    return xt
  
  def euler(self, f, x, t0, dt, par= None ):
    """
    """      
    return x + f(x, t0, par)*dt

  
  
class navio:
  """
  Classe de navios
  """
  
  tipo = 'Escolhido de acordo com self.Tipo'
  data = '10-11-2010'
  autor = 'Alex'
  
  def __init__(self, DicionarioDerivadas, Nome = 'Teste', Tipo = 'TP'):
    """"
    Construtor do navio
    __________________________
    Variáveis de entrada:
    
    Nome (string)-- Nome do Navio. Não possui relevância;
    Tipo ('TP')-- Tipo de modelo numérico adotado para a construção do
Leme

    """
    self.nome = Nome
    self.vel = sp.zeros((6, 1))
    self.acel = sp.zeros((6, 1))
    self.pos = sp.zeros((6, 1))
    self.dic = DicionarioDerivadas
    self.tipo = Tipo
    self.integrador = inte()
    self.uc = sp.array(self.dic['unom'])
    
    if Tipo == 'TP':
      self.leme = lemeTris(DicionarioDerivadas)
      self.casco = cascoTris(DicionarioDerivadas)
      self.prop = prop()
    elif Tipo == 'MARAD':
      self.leme = lemeMarAd(DicionarioDerivadas)
      self.casco = cascoMarAd(DicionarioDerivadas)
      self.prop = propMarAd(DicionarioDerivadas)




  def MostraVel(self):
    """
    Retorna a Velocidade da embarcação
    """
    return self.vel
    
  def MostraAcel(self):
    """
    Retorna a aceleração da embarcação
    """
    return self.acel
  
  def MostraLeme(self):
    """
    Retorna o leme em rad da embarcação
    """
    return self.leme.MostraLeme()

  def MostraLemeCom(self):
    """
    Retorna o leme em rad da embarcação
    """
    return self.leme.MostraLemeCom()
  
  def MostraPos(self):
    """
    Retorna a posição da embarcação
    """
    return self.pos

  def MostraRotCom(self):
    """
    Retorna a rotação comandada
    """
    return self.prop.MostraRotCom()

  def MostraRot(self):
    """
    Retorna a rotação
    """
    return self.prop.MostraRot()

  def MostraVelCom(self):
    """
    Retorna a velocidade comandada
    """
    return self.uc
    
  def MudaVelCom(self, uc):
    """
    Muda a velocidade comandada
    """
    self.uc  = uc.copy()
    self.prop.MudaVelCom(uc)
    
  def MudaLemeCom(self, AngLeme):
    """
    Muda o leme comandado da embarcação
    __________________________
    Variáveis de entrada:
    """
    temp = AngLeme.copy()
    self.leme.MudaLemeCom(temp)        

    
  def MudaVel(self, Velocidade):
    """
    Muda a velocidade da embarcação
    __________________________
    Variáveis de entrada:
    Velocidade -- velocidade (m/s)
    """
    temp = Velocidade.copy()
    
    self.vel = temp        
    self.casco.MudaVel(temp)
    self.leme.MudaVel(temp)
    self.prop.MudaVel(temp)

  def MudaPos(self, Posicao):
    """
    Muda a posição da embarcação 
    __________________________
    Variáveis de entrada:
    Posição -- posição (m)
    """
    temp = Posicao.copy()
    self.pos = temp
    self.casco.MudaPos(temp)
    self.leme.MudaPos(temp)
    self.prop.MudaPos(temp)


  def MudaRotCom(self, Rot):
    """
    Muda a rotação Comandada da embarcação
    """
    self.prop.MudaRotCom(Rot)
    
  def CalcFx(self):
    """
    Calcula a força em Surge   
    """
    m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    u = self.MostraVel()[0] 
    v = self.MostraVel()[1]
    p = self.MostraVel()[3]
    r = self.MostraVel()[5]
    xg = self.dic['xg']
    zg = self.dic['zg']
    
    cori = m*(v*r + xg*(r**2) -  zg*p*r) 
    
    if self.tipo == 'MARAD':
      saida = (self.casco.Fx() + self.prop.Fx() +
          self.leme.Fx(self.MostraRot(),
          self.MostraVelCom()/self.MostraVel()[0]) + cori) 
    elif self.tipo == 'TP':
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx() + cori
  
    return    saida

  def CalcFy(self):
    """
    Calcula a força em Sway
    """
    m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    u = self.MostraVel()[0] 
    v = self.MostraVel()[1]
    p = self.MostraVel()[3]
    r = self.MostraVel()[5]
    xg = self.dic['xg']
    zg = self.dic['zg']
    
    cori = -m*u*r
  
    if self.tipo == 'MARAD':
      saida = (self.casco.Fy() + self.leme.Fy(self.MostraRot()) +
          self.prop.Fy() + cori)
    elif self.tipo == 'TP':
      saida = self.casco.Fy() + self.leme.Fy() + self.prop.Fy() + cori
  
    return saida

  def CalcK(self):
    """
    Calcula o momento de Roll
    """
    m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    u = self.MostraVel()[0] 
    v = self.MostraVel()[1]
    p = self.MostraVel()[3]
    r = self.MostraVel()[5]
    xg = self.dic['xg']
    zg = self.dic['zg']
    
    cori = m*zg*u*r
  
    if self.tipo == 'MARAD':
      saida = (self.casco.K() + self.leme.K(self.MostraRot()) +
          self.prop.K() + cori)
    elif self.tipo == 'TP':
      saida = self.casco.K() + self.leme.K() + self.prop.K() + cori
  
    return    saida

  
  def CalcN(self):
    """
    Calcula o momento de  Yaw
    
    """
    m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    u = self.MostraVel()[0]
    v = self.MostraVel()[1]
    p = self.MostraVel()[3]
    r = self.MostraVel()[5]
    xg = self.dic['xg']
    zg = self.dic['zg']
    
    cori = -m*xg*u*r

    if self.tipo == 'MARAD':
      saida = (self.casco.N() + self.leme.N(self.MostraRot()) +
          self.prop.N() + cori)
    elif self.tipo == 'TP':
      saida = self.casco.N() + self.leme.N() + self.prop.N() + cori
  
    return saida
    
  def VetF(self, p=None):
    """
    Vetor de forças
    _________________________
    Variáveis de entrada:
    p --  tupla
    p[0] (integer)-- Graus de liberdade 
    p[1] (tupla)-- Com pesos
    """
    if p == None:
      GrausDeLib =4
      peso = None
    elif len(p)==1:
      GrausDeLib =p[0]
      peso = None
    elif len(p)==2:
      GrausDeLib =p[0]
      peso = p[1]
      
    if peso == None:
      if GrausDeLib == 4:
        saida = sp.array([self.CalcFx(), self.CalcFy(),
                self.CalcK(), self.CalcN()])  
      elif GrausDeLib == 3:
        saida = sp.array([self.CalcFx(), self.CalcFy(),
self.CalcN()])
    else:
      lemearq = self.MostraLeme()
      velarq = self.MostraVel()
      uc = self.MostraVelCom()
      
      ####################
      
      self.leme.MudaLemeDir(sp.array(0.))
      self.MudaVelCom(velarq[0]) #condição eta=1
      
##            ####################
##            Aquilo que depende somente de u
##
##            ####################
      
      veltemp = sp.zeros((6, 1))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)
      
      fu = self.VetF((GrausDeLib, ))

      ####################
      veltemp = sp.zeros((6, 1))
      veltemp[0] = velarq[0]
      veltemp[1] = velarq[1]
      self.MudaVel(veltemp)
      
      # leme = 0 e eta = 1

      fbeta = self.VetF((GrausDeLib, )) - fu
      it = 0
      fbeta1 = fbeta.copy()

      for arg in peso[0]:

        fbeta[it] = arg* fbeta[it]

        it +=1 
      ####################

      
      
      veltemp = sp.zeros((6, 1))
      veltemp[5] = velarq[5]
      veltemp[0] = velarq[0]            
      self.MudaVel(veltemp)
      
      fr = self.VetF((GrausDeLib, )) - fu
      fr1 = fr.copy()

      it = 0
      for arg in peso[1]:
        fr[it] = arg* fr[it]
        it +=1                

      ####################
      
      
      
      self.leme.MudaLemeDir(lemearq)
      veltemp = sp.zeros((6, 1))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)
      
      fleme = self.VetF((GrausDeLib, ))  - fu
      
      fleme1 = fleme.copy()

      it = 0            
      for arg in peso[2]:
        fleme[it] = arg* fleme[it]
        it +=1     
      

      ####################
      
      self.MudaVel(velarq)
      self.MudaVelCom(uc)
      
      fbetarl = self.VetF((GrausDeLib, )) - (fbeta1 + fr1 + fleme1)
      it = 0
    
      for arg in peso[3]:
        fbetarl[it] = arg* fbetarl[it]
        it +=1                            
      del it 
      
      
      
      saida = fbeta + fr + fleme + fbetarl
    
    return saida

  def H (self, GrausDeLib=4):
    """
    Matriz de massa menos matriz de massa adicional
    _________________________
    Variáveis de entrada:
    
    GrausDeLib (integer)-- Graus de liberdade 
    """
    H = None
    H = self.casco.M(GrausDeLib) - self.casco.Ma(GrausDeLib)
    
    return  sp.mat(H)

  def MatRot(self, p=None):
    """
    Retorna a matrix de rotação de do referêncial solidárial para o 
    inercial
    """
    if p== None:
      roll= self.MostraPos()[3]
      pitch = self.MostraPos()[4]
      yaw = self.MostraPos()[5]
    else:
      roll= p[0]
      pitch = p[1]
      yaw = p[2]
      
    Rot = sp.array([[sp.cos(yaw)*sp.cos(pitch), 
    -sp.sin(yaw)*sp.cos(roll) +
sp.cos(yaw)*sp.sin(pitch)*sp.sin(roll), 
    sp.sin(yaw)*sp.sin(roll) + sp.cos(yaw)*sp.cos(roll)*sp.sin(pitch)
], 
    [sp.sin(yaw)*sp.cos(pitch), 
    sp.cos(yaw)*sp.cos(roll) + sp.sin(roll)*sp.sin(pitch)*sp.sin(yaw), 
    -sp.cos(yaw)*sp.sin(roll) + sp.sin(yaw)*sp.cos(roll)*sp.sin(pitch)
], 
    [-sp.sin(pitch), sp.cos(pitch)*sp.sin(roll), 
    sp.cos(pitch)*sp.cos(roll)] ])
    
    Rot.shape  = (3, 3)
    Rot= sp.matrix(Rot)
    return Rot

  def f2 (self, VetF, H):
    """
    Calcula o valor de f(x) na equação
    x' = f(x)
    onde x são é  o vetor de velocidades no sistema solidário
    _________________________
    Variáveis de entrada:
    
    GrausDeLib (integer)-- Graus de liberdade 
    """
    
    GrausDeLib = len(VetF)
      
    if GrausDeLib == 4:
      a=  sp.zeros((6, 6))
      a[5, 5] = 1.
      a[4, 4] = 1.
      a[:4, :4]= H

      b=  sp.zeros((6, 1))
      b [4, 0] = self.vel[3]
      b [5, 0] = self.vel[5]*sp.cos(self.MostraPos()[3])
      b[:4, :]= VetF
    elif GrausDeLib == 3:
      a=  sp.zeros((4, 4))
      a[3, 3] = 1.
      a[:3, :3]= H

      b=  sp.zeros((4, 1))
      b[:3, :]= VetF
      b[3, 0] = self.MostraVel()[5]
    
    saida = linalg.solve(a, b ) 

    return saida
    
  def f(self, velocidade=None, t=None, p=(4, )):
    """
    O p é uma tupla com o valor dos graus de liberdade
    """
    GrausDeLib = p[0]
    if velocidade !=None:
      velarq = self.MostraVel()
      posarq = self.MostraPos()
      veltemp = sp.zeros((6, 1))
      postemp =  sp.zeros((6, 1))
      if GrausDeLib==3:
        veltemp[:2] = velocidade[:2]
        veltemp[5] = velocidade[2]
        postemp[5] = velocidade[3]
      elif GrausDeLib==4:
        veltemp[:2] = velocidade[:2]
        veltemp[3] = velocidade[2]
        veltemp[5] = velocidade[3]
        postemp[3] = velocidade[4]
        postemp[5] = velocidade[5]
      self.MudaVel(veltemp)
      self.MudaPos(postemp)
    
    if GrausDeLib == 4:
      a=  sp.zeros((6, 6))
      a[5, 5] = 1.
      a[4, 4] = 1.
      a[:4, :4]= self.H(GrausDeLib)

      b=  sp.zeros((6, 1))
      b [4, 0] = self.vel[3]
      b [5, 0] = self.vel[5]*sp.cos(self.MostraPos()[3])
      b[:4, :]= self.VetF(p)
    elif GrausDeLib == 3:
      a=  sp.zeros((4, 4))
      a[3, 3] = 1.
      a[:3, :3]= self.H(GrausDeLib)

      b=  sp.zeros((4, 1))
      b[:3, :]= self.VetF(p) 
      b[3, 0] = self.MostraVel()[5]
    
    saida = linalg.solve(a, b) 
    
    if velocidade !=None:
      self.MudaVel(velarq)
      self.MudaPos(posarq)
    return saida    
  def fvein(self, x, t, p):
    """
    x = sp.array(u, v , w)
    p = (  roll, pitch, yaw)
    """
  
    return sp.array(self.MatRot(p[0])*p[1])
    
  def simula(self, met='euler', t0=0., dt=0.5, t=100., GrausDeLib=4,
        velocidade=None, tipo='ZigZag', leme=sp.array(20.),
        proa=sp.array(20.), RotCom =sp.array(1),osa=sp.array(0.05),
        ospath=sp.array(150), erro=sp.array(0.05),
        errotf=sp.array(0.05), errotd=sp.array(0.05), arqs='saida'):
    """
    Simulador de manobras padrão
    _________________________
    Variáveis de entrada:
    
    GrausDeLib (integer)-- Graus de liberdade;        
    met -- Método de integração. Default- Euler;
    t0 -- Tempo inicial;
    dt -- Passo no tempo;
    t -- Tempo final 
    tipo - tipo de manobra simulada. Zig-Zag10/10 e Curva_de_Giro_port
ou 
    Curva_de_Giro_starboard . Default -Zig-Zag
    
    __________________________
    Saída:
    
    Tupla de sp.array
    
    (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis)
    
    Em cada elemento da tupla:
    A primeira coluna é o passo de tempo e as demais são as variáveis
    
    veloHis -- histórico de velocidades;
    posHis -- histórico de posições
    acelHis --- histórico de acelerações
    fHis -- histórico de forças 
    veloInerHis -- histórico de velocidades no sistema inercial
    lemeHis -- histórico do comando de leme
    """

#
#        Tipo de Simulação a ser realizada:
#
    self.MudaPos( sp.array([  [0.], [0.], [0.], [0.], [0.], [0.] ]))
    self.MudaVel(sp.array([  [self.dic['unom']], [0.], [0.], [0.], [0.],
    [0.] ]))
    self.MudaRotCom(RotCom)
    self.MudaVelCom(self.dic['unom'])
#Log é o parâmetro que indica quando a simulação armazenou os dados do
#relatório
    if tipo == 'Curva_de_Giro_port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      log = False
    elif tipo == 'Curva_de_Giro_starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      log = False
    elif tipo == 'ZigZag':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      exe = 0
    
    

###############################
##
##   Dados relacionados a curva de zizag
##
###############################
      if (tipo == 'ZigZag' and (((exe%2 == 0) and self.MostraPos()[5]
<=
        -(proa*sp.pi/180) ) or (exe%2 != 0 and self.MostraPos()[5]
>=
        (proa*sp.pi/180) ))):
        self.MudaLemeCom(self.MostraLeme()*(-1))
        if exe!=0:
          dic['reach'] = erro
          dic['ospath'] = ospath
          dic['osangle'] = abs(osa - dic['proa'])
          dados.append(dic.copy())

        exe += 1
        dic['exeNummber'] = exe
        dic['time'] = tp - sp.array(dt)
        dic['path'] = self.MostraPos()[1]
        dic['proa'] = self.MostraPos()[5]
    
      if tipo=='ZigZag' and exe!=0:
        if abs(self.MostraPos()[1]- dic['path'])>ospath:
          ospath = abs(self.MostraPos()[1]- dic['path'])  
        if abs(self.MostraPos()[5])>abs(osa):
          osa = self.MostraPos()[5]
        if abs(self.MostraPos()[5] - PosIni[5]) < erro:
          erro = abs(self.MostraPos()[5] - PosIni[5])            

        
      
      

###############################
##
##   Dados relacionados a curva de Giro
##
###############################            
      if ((tipo == 'Curva_de_Giro_port' or
        tipo == 'Curva_de_Giro_starboard') and not log):
        
        if (abs(abs(self.MostraPos()[5] - PosIni[5]) -
          (sp.array(90)*sp.pi/180)) <= errotf):
          errotf = (abs(abs(self.MostraPos()[5] - PosIni[5]) -
              (sp.array(90)*sp.pi/180)))
          dic['transfer'] = abs(self.MostraPos()[1] - PosIni[1])
          dic['advance'] = abs(self.MostraPos()[0] - PosIni[0])
        if abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi) <= errotd:
          errotd = abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi)
          dic['taticalDiameter'] = abs(self.MostraPos()[1] - \
PosIni[1])
        
        if abs(self.MostraPos()[5] - PosIni[5]) > sp.pi :
          log = True
          dados.append(dic)


      Rot = self.MatRot()
      
#
#                inc = Velocidades Lineares no Sistema Inecial
#
      VelIn = Rot*sp.matrix(self.vel[0:3])

      PosIne = self.MostraPos()[0:3]
      
##################################
#                
#                       Guardando os parâmetros
#                
##################################                
#          Velocidade Inercial      
      d= sp.hstack(VelIn)
      veloInerHis[cont, 1:] = d #
      veloInerHis[cont, 0] = tp #
#           Histórico Leme
      lemeHis[cont, 0] = tp
      lemeHis[cont, 1] = self.MostraLeme()
#           Histórico da posição
      temp = sp.hstack(self.MostraPos())
      posHis[cont, :] = sp.hstack((tp, temp))

#           Histórico da Velocidade
      temp = sp.hstack(self.MostraVel())
      veloHis[cont, :] = sp.hstack((tp, temp))

#           Histórico das Forças 
      temp =sp.hstack(sp.array(self.VetF(GrausDeLib)))
      if GrausDeLib == 4:
        fHis[cont, :]  = sp.hstack((tp, temp))
      elif GrausDeLib == 3:
        fHis[cont, :3]  = sp.hstack((tp, temp[:2]))
        fHis[cont, 4]  = temp[2]

#           Histórico Propulsor
      propHis[cont, :] = sp.hstack((tp, self.MostraRot()))

#           Histórico das Acelerações 
      Acel = self.f(GrausDeLib)
      
      if GrausDeLib == 4:
        vetor = sp.zeros((6, 1))
        vetor[:2] = Acel[:2]
        vetor[3] = Acel[2]
        vetor [5] = Acel[3]
      elif GrausDeLib == 3:
        vetor = sp.zeros((6, 1))
        vetor[:2] = Acel[:2]
        vetor [5] = Acel[2]
      acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))           



      del temp 
##############################
#
#    Criação de vetor de graus de liberdade
#
##############################
      if GrausDeLib == 4:
        xIn = sp.zeros([6, 1])
        
        xIn [0] = self.MostraVel()[0]
        xIn [1] = self.MostraVel()[1]
        xIn [2] = self.MostraVel()[3]
        xIn [3] = self.MostraVel()[5]
        xIn [4] = self.MostraPos()[3]
        xIn [5] = self.MostraPos()[5]
      elif  GrausDeLib == 3:
        xIn = sp.zeros([4, 1])
        xIn [0] = self.MostraVel()[0]
        xIn [1] = self.MostraVel()[1]
        xIn [2] = self.MostraVel()[5]
        xIn [3] = self.MostraPos()[5]         
##################################
#                
#                      Integração da Aceleração solidária
#                
##################################
      if met == 'euler':
        xIn =  self.integrador.euler(Acel, xIn, dt )
      elif met =='rk4':
        xIn = self.integrador.rk4(self.facel, dt, tp, xIn)
      
##################################
      if GrausDeLib == 4:
        x = sp.zeros((6, 1))
        x[0] = xIn[0] 
        x[1] = xIn[1] 
        x[3] = xIn[2]
        x[5] = xIn[3]
      elif GrausDeLib==3:
        x = sp.zeros((6, 1))
        x[0] = xIn[0] 
        x[1] = xIn[1] 
        x[5] = xIn[2]                
      self.MudaVel(x)               

      del x
##################################
##                
##                       Integração da velocidade inercial
##                
###################################
      posfutura = sp.zeros((6, 1))
      posfutura[:3] = self.integrador.euler(VelIn, PosIne, dt)
      
##################################
      if GrausDeLib== 4:
        posfutura[3] = xIn[4]
        posfutura[5] = xIn[5]
      elif GrausDeLib== 3:
        posfutura[5] = xIn[3]
        
      self.MudaPos(posfutura)
      cont += 1
      del posfutura
      
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)

    return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
propHis, 
        dados)
    
    
  def getCurvaGiro(self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
          GrausDeLib=3, tipo='port', leme=sp.array(20.),
          RotCom=None, VelCom= None, Vel=None, Eta='vel',
          PosIne=sp.array([[0.], [0.], [0.], [0.], [0.], [0.] ]),
          errotf=sp.array(0.05), errotd=sp.array(0.05),
          errosr=sp.array(0.001), saida='txt', arqs='saida'):
    """
    """

    if RotCom == None:
      RotCom = self.dic['rotnom']
    if VelCom == None:
      VelCom = self.dic['unom']
    if Vel ==  None:
      Vel = sp.array([  [self.dic['unom']], [0.], [0.], [0.], [0.],
[0.]
])
    
    self.MudaPos( PosIne)
    self.MudaVel(Vel)
    self.MudaRotCom(RotCom)
    self.MudaVelCom(VelCom)

#Log é o parâmetro que indica quando a simulação armazenou os dados do
#relatório
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      log = False
      log1 = False
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      log = False
      log1 = False
#
#   Criando espaço na memória para armazenar os parâmetros da curva
#
    nlin = len(sp.arange(t0, t, dt)) #Número de linhas das colunas a serem
#criadas
    if saida == 'mem':
      lemeHis = sp.zeros((nlin, 2)) #historico do leme
      veloHis = sp.zeros((nlin, 7)) #histórico da velocidade
      veloInerHis = sp.zeros((nlin, 4))#histórico da velocidade no
#sistema inercial Verificar depois a necessidade
      posHis =  sp.zeros([nlin, 7]) #histórico da posição no sistema
#inercial
      fHis     = sp.zeros((nlin, 5)) #histórico de forças
      acelHis = sp.zeros((nlin, 7)) #histórico de acelerações
      propHis = sp.zeros((nlin, 2)) #histórico Máquina
      EtaHis = sp.zeros((nlin, 2)) #histórico Eta
      betaHis =  sp.zeros((nlin, 2)) #histórico beta
    elif saida == 'txt':
      if os.path.exists(arqs):
        os.rename(arqs, arqs + '2')
      os.makedirs(arqs)
      os.chdir(arqs)
      lemeHis = open('leme.dat', 'w')#historico do leme
      lemeHis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n') 
      lemeHis.write('#Valor do leme em rad\n')
      lemeHis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' +
            '\n')
      
      veloHis = open('velo.dat', 'w') #histórico da velocidade
      veloHis.write('#Navio ' + self.nome + '\n' + 
            '#Manobra de Curva de Giro\n#\n')
      veloHis.write('#Velocidade Sistema Solidário \n#\n')
      veloHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 
            'dot roll'.rjust(11) + ' ' + 'dot pitch'.rjust(11)
+ 
            ' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      veloInerHis = open('veloiner.dat', 'w')#histórico da velocidade no
#sistema inercial Verificar depois a necessidade
      veloInerHis.write('#Navio ' + self.nome + '\n' +  
              '#Manobra de Curva de Giro\n#\n')
      veloInerHis.write('#Velocidade Inercial\n#\n')
      veloInerHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              'v'.rjust(11) + ' ' + 'r'.rjust(11) + '\n') 

      posHis =  open('pos.dat', 'w')#histórico da posição no sistema
#inercial
      posHis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n')
      posHis.write('#Posição e Orientação\n#\n')
      posHis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
            'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
            'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
            'yaw'.rjust(11)  + ' ' + '\n') 

      fHis     = open('forcas.dat', 'w') #histórico de forças
      fHis.write('#Navio ' + self.nome + '\n' + 
          '#Manobra de Curva de Giro\n#\n')
      fHis.write('#Forças e Momentos\n#\n')
      fHis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
          'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
          'N'.rjust(11) + ' ' + '\n') 
      
      acelHis = open('acel.dat', 'w') #histórico de acelerações
      acelHis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n')
      acelHis.write('#Aceleração\n#\n')
      acelHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
            'ddotroll'.rjust(11) + ' ' + 'ddotpitch'.rjust(11)
+							' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      propHis = open('propulsor.dat', 'w') #histórico Máquina
      propHis.write('#Navio ' + self.nome + '\n' + 
            '#Manobra de Curva de Giro\n#\n')
      propHis.write('#Rotações do propulsor\n#\n')
      propHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      EtaHis = open('Eta.dat', 'w') #histórico Eta
      EtaHis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n')
      EtaHis.write('#Eta \n#\n')
      EtaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' +
'\n')


      betaHis = open('beta.dat', 'w') #histórico Eta
      betaHis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n')
      betaHis.write('#Beta \n#\n')
      betaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' +
            '\n')
      
      os.chdir('..')
      os.chdir('..')
    
    dados = []
    dic = {}
    PosIni = self.MostraPos().copy()           

    del nlin #não preciso mais
    cont =0 #Contador
    
    if peso == None:   
      par =   (GrausDeLib, )
    else:
      par = (GrausDeLib, peso)
#
#   Iteração
#

    for tp in sp.arange(t0, t, dt):
      if not log1:
        if cont == 0:
          V1 = sp.sqrt(self.MostraVel()[0]**2 +
                self.MostraVel()[1]**2)
        elif cont == 1:
          V2 = sp.sqrt(self.MostraVel()[0]**2 +
                self.MostraVel()[1]**2)
        elif cont == 2:
          V3 = sp.sqrt(self.MostraVel()[0]**2 +
                self.MostraVel()[1]**2)
        elif cont == 3:
          V4 = sp.sqrt(self.MostraVel()[0]**2 +
                self.MostraVel()[1]**2)
        else:
          V1 = V2
          V2 = V3
          V3 = V4
          V4 = sp.sqrt(self.MostraVel()[0]**2 +
                self.MostraVel()[1]**2)                
        if log:
          if stats.tstd((V1, V2, V3, V4))<errosr:
            dic['steadytr'] = (sp.sqrt(self.MostraVel()[0]**2 +
                        self.MostraVel()[1]**2) /
                    self.MostraVel()[5])
            dados.append(dic.copy())
            log1= True
          
        if  not log:
          if (abs(abs(self.MostraPos()[5] - PosIni[5]) - 
              (sp.pi/2)) <= errotf):
            errotf = (abs(abs(self.MostraPos()[5] - PosIni[5]) -
                  (sp.pi/2)))
            dic['transfer'] = abs(self.MostraPos()[1] - PosIni[1])
            dic['advance'] = abs(self.MostraPos()[0] - PosIni[0])
          if (abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi) <=
            errotd):
            errotd = abs(abs(self.MostraPos()[5] - PosIni[5]) -
                  sp.pi)
            dic['taticalDiameter'] = abs(self.MostraPos()[1] -
                          PosIni[1])
          if abs(self.MostraPos()[5] - PosIni[5]) > sp.pi:
            log = True


###################################
      ft = self.VetF(par) 
###################################
##
##                inc = Velocidades Lineares no Sistema Inecial
##
###################################
      MatRot = self.MatRot()
      
      VelIn = sp.array(MatRot*self.MostraVel()[0:3])

      PosIne = self.MostraPos()[0:3]


##################################
##                
##                       Guardando os parâmetros
##                
##################################                
#          Velocidade Inercial
      if saida == 'txt':
        veloInerHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in VelIn:
          veloInerHis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloInerHis.write('\n')
      elif saida == 'mem':
        d = sp.hstack(VelIn)
        veloInerHis[cont, 1:] = d #
        veloInerHis[cont, 0] = tp #
#           Histórico Leme
      if saida == 'txt':
        lemeHis.write('%.2f'.rjust(5)%(tp) + ' ')
        lemeHis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      elif saida == 'mem':
        lemeHis[cont, 0] = tp
        lemeHis[cont, 1] = self.MostraLeme()
#           Histórico da posição
      if saida == 'txt':
        posHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraPos():
          posHis.write('%.5e'.rjust(11)%(arg) + ' ')
        posHis.write('\n')
      elif saida == 'mem':            
        temp = sp.hstack(self.MostraPos())
        posHis[cont, :] = sp.hstack((tp, temp))
        del temp
#           Histórico da Velocidade
      if saida == 'txt':
        veloHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraVel():
          veloHis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloHis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(self.MostraVel())
        veloHis[cont, :] = sp.hstack((tp, temp))
        del temp
#           Histórico das Forças 
      if saida == 'txt':
        temp = sp.zeros((4, 1))
        if GrausDeLib == 4:
          temp= ft
        elif GrausDeLib == 3:
          temp[:2]  = ft[:2]
          temp[3]  = ft[2]
        fHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in temp:
          fHis.write('%.5e'.rjust(11)%(arg) + ' ')
        fHis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(sp.array(ft))
        if GrausDeLib == 4:
          fHis[cont, :] = sp.hstack((tp, temp))
        elif GrausDeLib == 3:
          fHis[cont, :3] = sp.hstack((tp, temp[:2]))
          fHis[cont, 4] = temp[2]

#           Histórico Propulsor
      if saida == 'txt':
        propHis.write('%.2f'.rjust(5)%(tp) + ' ')
        propHis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      elif saida == 'mem':
        propHis[cont, :] = sp.hstack((tp, self.MostraRot()))
#           Histórico Eta
      if saida == 'txt':
        EtaHis.write('%.2f'.rjust(5)%(tp) + ' ')
        if Eta == 'rot':
          EtaHis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                self.MostraRot()) + '\n')
        elif Eta == 'vel':
          EtaHis.write('%.2f'.rjust(5) %
                (self.MostraVelCom() / self.MostraVel()[0])
+
                '\n')
      elif saida == 'mem':
        if Eta== 'rot':
          EtaHis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
          self.MostraRot()))
        elif Eta == 'vel':
          EtaHis[cont, :] = sp.hstack((tp, 
                        self.MostraVelCom() /
                        self.MostraVel()[0]))

#           Histórico Beta
      if saida == 'txt':
        betaHis.write('%.2f'.rjust(5) % (tp) + ' ')
        betaHis.write(('%.2f'.rjust(5) % 
              sp.arctan(-self.MostraVel()[1] /
              self.MostraVel()[0])) + '\n')
        
      elif saida == 'mem':
        betaHis[cont, :] = sp.hstack((tp,
                      sp.arctan(-self.MostraVel()[1]
/
                      self.MostraVel()[0])))

#           Histórico das Acelerações 
      Acel = self.f2(ft, self.H(GrausDeLib))
      vetor = sp.zeros((6, 1))
      if GrausDeLib == 4:
        vetor[:2] = Acel[:2]
        vetor[3] = Acel[2]
        vetor [5] = Acel[3]
      elif GrausDeLib == 3:
        vetor[:2] = Acel[:2]
        vetor [5] = Acel[2]
      if saida == 'txt':
        acelHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vetor:
          acelHis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        acelHis.write('\n')
      elif saida == 'mem':  
        acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       

  
  
        del temp 
##############################
#
#    Criação de vetor de graus de liberdade
#
##############################
      if GrausDeLib == 4:
        vt = sp.zeros([6, 1])
        
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[3]
        vt [3] = self.MostraVel()[5]
        vt [4] = self.MostraPos()[3]
        vt [5] = self.MostraPos()[5]
      elif  GrausDeLib == 3:
        vt = sp.zeros([4, 1])
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[5]
        vt [3] = self.MostraPos()[5]         
##################################
##                
##                      Integração da Aceleração solidária
##                
##################################
      if met == 'euler':
        vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      elif met =='rk4':
        vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
##################################
      if GrausDeLib == 4:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1] 
        v[3] = vt[2]
        v[5] = vt[3]
      elif GrausDeLib == 3:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1] 
        v[5] = vt[2]                
      self.MudaVel(v)               

      del v
##################################
##                
##                       Integração da velocidade inercial
##                
###################################
      x = sp.zeros((6, 1))
      if met == 'euler':
        x[:3] = self.integrador.euler(self.fvein ,
                      self.MostraPos()[:3], tp, dt ,
                      (self.MostraPos()[3:] ,
                      self.MostraVel()[:3]))	
      elif met == 'rk4':
        x[:3] = self.integrador.rk4(self.fvein, self.MostraPos()[:3],
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()[:3]))
##################################
      if GrausDeLib == 4:
        x[3] = vt[4]
        x[5] = vt[5]
      elif GrausDeLib == 3:
        x[5] = vt[3]
        
      self.MudaPos(x)
      
      del x
      cont += 1
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)
    if saida == 'txt':
      arq = [veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
        propHis, EtaHis]
      for arg in arq:
        arg.close()
      return dados
    elif saida == 'mem':
      return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
          propHis, EtaHis, dados, betaHis)

  def getCurvaZigZag(self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
                      GrausDeLib=3, tipo='port', leme=sp.array(20.),
                      RotCom=None, VelCom=None, Vel=None,
                      proa=sp.array([20.]), Eta='vel', 
                      PosIne=sp.array([[0.],[0.],[0.], [0.], [0.], [0.]]),
                      osa=sp.array(0.0), ospath=sp.array(0.0),
                      erro=sp.array(0.005),saida='txt'):
    """
    Simulador de manobras padrão
    _________________________
    Variáveis de entrada:
    
    GrausDeLib (integer)-- Graus de liberdade;        
    met -- Método de integração. Default- Euler;
    t0 -- Tempo inicial;
    dt -- Passo no tempo;
    t -- Tempo final 
    tipo - tipo de manobra simulada. Zig-Zag10/10 e Curva_de_Giro_port
ou
Curva_de_Giro_starboard . Default -Zig-Zag
    
    __________________________
    Saída:
    
    Tupla de sp.array
    
    (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis)
    
    Em cada elemento da tupla:
    A primeira coluna é o passo de tempo e as demais são as variáveis
    
    veloHis -- histórico de velocidades;
    posHis -- histórico de posições
    acelHis --- histórico de acelerações
    fHis -- histórico de forças 
    veloInerHis -- histórico de velocidades no sistema inercial
    lemeHis -- histórico do comando de leme
    """

    if RotCom == None:
      RotCom = self.dic['rotnom']
    if VelCom == None:
      VelCom = self.dic['unom']
    if Vel ==  None:
      Vel = sp.array([[self.dic['unom']], [0.], [0.], [0.], [0.], [0.]
              ])
    
    self.MudaPos( PosIne)
    self.MudaVel(Vel)
    self.MudaRotCom(RotCom)
    self.MudaVelCom(VelCom)


    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      exe=0
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      exe=1

    
#
#   Criando espaço na memória para armazenar os parâmetros da curva
#
#Número de linhas das colunas a seremcriadas
    nlin = len(sp.arange(t0, t, dt)) 

    if saida == 'mem':
      lemeHis = sp.zeros((nlin, 2)) #historico do leme
      veloHis = sp.zeros((nlin, 7)) #histórico da velocidade
      veloInerHis = sp.zeros((nlin, 4))#histórico da velocidade no
#sistema inercial Verificar depois a necessidade
      posHis =  sp.zeros([nlin, 7]) #histórico da posição no sistema
#inercial
      fHis     = sp.zeros((nlin, 5)) #histórico de forças
      acelHis = sp.zeros((nlin, 7)) #histórico de acelerações
      propHis = sp.zeros((nlin, 2)) #histórico Máquina
      EtaHis = sp.zeros((nlin, 2)) #histórico Eta
    elif saida == 'txt':
      os.makedirs('./saida/ZigZag')
      os.chdir('./saida/ZigZag')
      lemeHis = open('leme.dat', 'w')#historico do leme
      lemeHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            de Zig-Zag\n#\n')
      lemeHis.write('#Valor do leme em rad\n')
      lemeHis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' +
            '\n')
      
      veloHis = open('velo.dat', 'w') #histórico da velocidade
      veloHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            de Zig-Zag\n#\n')
      veloHis.write('#Velocidade Sistema Solidário \n#\n')
      veloHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 'dot \
              roll'.rjust(11) + ' ' + ' dot pitch'.rjust(11)  + 
              ' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      veloInerHis = open('veloiner.dat', 'w')#histórico da velocidade no
#sistema inercial Verificar depois a necessidade
      veloInerHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de \
              Curva de Zig-Zag\n#\n')
      veloInerHis.write('#Velocidade Inercial\n#\n')
      veloInerHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              'v'.rjust(11)  + ' '  + 'r'.rjust(11) + '\n') 

      posHis =  open('pos.dat', 'w')#histórico da posição no sistema
#inercial
      posHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            de Zig-Zag\n#\n')
      posHis.write('#Posição e Orientação\n#\n')
      posHis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
            'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
            'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
            'yaw'.rjust(11) + ' ' + '\n') 

      fHis = open('forcas.dat', 'w') #histórico de forças
      fHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva de \
            Zig-Zag\n#\n')
      fHis.write('#Forças e Momentos\n#\n')
      fHis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
          'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
          'N'.rjust(11) + ' ' + '\n') 
      
      acelHis = open('acel.dat', 'w') #histórico de acelerações
      acelHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
            de Zig-Zag\n#\n')
      acelHis.write('#Aceleração\n#\n')
      acelHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
            'ddotroll'.rjust(11) + ' ' + ' ddotpitch'.rjust(11)
            + ' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      propHis = open('propulsor.dat', 'w') #histórico Máquina
      propHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
            de Zig-Zag\n#\n')
      propHis.write('#Rotações do propulsor\n#\n')
      propHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      EtaHis = open('Eta.dat', 'w') #histórico Eta
      EtaHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            de Zig-Zag\n#\n')
      EtaHis.write('#Eta \n#\n')
      EtaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' + 
            '\n')
      
      os.chdir('..')
      os.chdir('..')
      
    dados = []
    dic = {}
    PosIni = self.MostraPos().copy()           

    del nlin #não preciso mais
    cont =0 #Contador
    
    if peso == None:   
      par =   (GrausDeLib, )
    else:
      par = (GrausDeLib, peso)
    

#
#   Iteração
#

    for tp in sp.arange(t0, t, dt):

###############################
##
##   Verificando o momento em que será realizada a mudança do leme
##
###############################
      if (((exe%2 == 0) and self.MostraPos()[5] <= 
        -(proa * sp.pi / 180)) or (exe%2 != 0 and 
        self.MostraPos()[5] >= (proa * sp.pi / 180))):
          self.MudaLemeCom(self.MostraLeme() * (-1))
          if ((exe != 0 and tipo == 'port') or (exe != 1
            and tipo == 'starboard')):
              dic['reach'] = erro
              dic['ospath'] = ospath
              dic['osangle'] = osa
              dados.append(dic.copy())
        
          osa = sp.array(0.0)
          ospath = sp.array(0)
          erro = sp.array(0.05)
          logospath = False
          logosa = False
          exe += 1
          if tipo =='port':
            dic['exeNummber'] = exe
          elif tipo=='starboard':
            dic['exeNummber'] = exe - 1
          dic['time'] = tp - sp.array(dt)
          dic['path'] = self.MostraPos()[1]
          dic['proa'] = self.MostraPos()[5]

###############################
##
##   Atualizando os parâmetros
##
###############################
      
      if ((exe!=0 and tipo == 'port') or (exe!=1 and tipo ==
        'starboard')):
        if ((logospath == False) and
          (abs(self.MostraPos()[1] - dic['path']) >= ospath)):
#(sp.sign(self.MostraPos()[1])== sp.sign(dic['path'])) and
          ospath = abs(self.MostraPos()[1] - dic['path'])
        else:
          logospath = True
        
        if ((logosa == False) and (abs(self.MostraPos()[5] - 
          dic['proa']) >= osa)): #(sp.sign(self.MostraPos()[5])==
#sp.sign(dic['proa'])) and 
          osa = abs(self.MostraPos()[5] - dic['proa'])
        else:
          logosa = True
          
        if abs(abs(self.MostraPos()[5]) - abs(PosIni[5])) < erro:
          erro = abs(self.MostraPos()[5] - PosIni[5])            

      
  
      
      
#
#                inc = Velocidades Lineares no Sistema Inecial
#
      MatRot = self.MatRot()
      VelIn = MatRot * sp.matrix(self.vel[0:3])

      PosIne = self.MostraPos()[0:3]

###################################

#################################
##
##  Cálculo das forças de Maneira Modular
##
###################################
      ft = self.VetF(par)

##################################
##################################
##                
##                       Guardando os parâmetros
##                
##################################                
#          Velocidade Inercial
      if saida == 'txt':
        veloInerHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in VelIn:
          veloInerHis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloInerHis.write('\n')
      elif saida == 'mem':
        d = sp.hstack(VelIn)
        veloInerHis[cont, 1:] = d #
        veloInerHis[cont, 0] = tp #
#           Histórico Leme
      if saida == 'txt':
        lemeHis.write('%.2f'.rjust(5)%(tp) + ' ')
        lemeHis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      elif saida == 'mem':
        lemeHis[cont, 0] = tp
        lemeHis[cont, 1] = self.MostraLeme()
#           Histórico da posição
      if saida == 'txt':
        posHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraPos():
          posHis.write('%.5e'.rjust(11)%(arg) + ' ')
        posHis.write('\n')
      elif saida == 'mem':            
        temp = sp.hstack(self.MostraPos())
        posHis[cont, :] = sp.hstack((tp, temp))
        del temp
#           Histórico da Velocidade
      if saida == 'txt':
        veloHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraVel():
          veloHis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloHis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(self.MostraVel())
        veloHis[cont, :] = sp.hstack((tp, temp))
        del temp
#           Histórico das Forças 
      if saida == 'txt':
        temp = sp.zeros((4, 1))
        if GrausDeLib == 4:
          temp = ft
        elif GrausDeLib == 3:
          temp[:2] = ft[:2]
          temp[3] = ft[2]
        fHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in temp:
          fHis.write('%.5e'.rjust(11)%(arg) + ' ')
        fHis.write('\n')  #def __init__(self):
    #"""
    #"""
    #pass
    
  #def rk4(self, function, x, t0, dt, par = None):
    #"""
    #Integrador runge-kutta
    #"""
    #k1 = function(x, t0, par)
    #k2 = function(x + 1./2*dt*k1, t0 + 1./2*dt, par)
    #k3 = function(x + 1./2*dt*k2, t0 + 1./2*dt, par)
    #k4 = function(x + dt*k3, t0 + dt, par)
  
    #xt = x + 1./6*(k1+ 2.*k2+ 2.*k3+ k4)*dt
  
    #return xt
  
  #def euler(self, f, x, t0, dt, par= None ):
    #"""
    #"""      
    #return x + f(x, t0, par)*dt

  
  
#class navio:
  #"""
  #Classe de navios
  #"""
  
  #tipo = 'Escolhido de acordo com self.Tipo'
  #data = '10-11-2010'
  #autor = 'Alex'
  
  #def __init__(self, DicionarioDerivadas, Nome = 'Teste', Tipo = 'TP'):
    #""""
    #Construtor do navio
    #__________________________
    #Variáveis de entrada:
    
    #Nome (string)-- Nome do Navio. Não possui relevância;
    #Tipo ('TP')-- Tipo de modelo numérico adotado para a construção do
#Leme

    #"""
    #self.nome = Nome
    #self.vel = sp.zeros((6, 1))
    #self.acel = sp.zeros((6, 1))
    #self.pos = sp.zeros((6, 1))
    #self.dic = DicionarioDerivadas
    #self.tipo = Tipo
    #self.integrador = inte()
    #self.uc = sp.array(self.dic['unom'])
    
    #if Tipo == 'TP':
      #self.leme = lemeTris(DicionarioDerivadas)
      #self.casco = cascoTris(DicionarioDerivadas)
      #self.prop = prop()
    #elif Tipo == 'MARAD':
      #self.leme = lemeMarAd(DicionarioDerivadas)
      #self.casco = cascoMarAd(DicionarioDerivadas)
      #self.prop = propMarAd(DicionarioDerivadas)




  #def MostraVel(self):
    #"""
    #Retorna a Velocidade da embarcação
    #"""
    #return self.vel
    
  #def MostraAcel(self):
    #"""
    #Retorna a aceleração da embarcação
    #"""
    #return self.acel
  
  #def MostraLeme(self):
    #"""
    #Retorna o leme em rad da embarcação
    #"""
    #return self.leme.MostraLeme()

  #def MostraLemeCom(self):
    #"""
    #Retorna o leme em rad da embarcação
    #"""
    #return self.leme.MostraLemeCom()
  
  #def MostraPos(self):
    #"""
    #Retorna a posição da embarcação
    #"""
    #return self.pos

  #def MostraRotCom(self):
    #"""
    #Retorna a rotação comandada
    #"""
    #return self.prop.MostraRotCom()

  #def MostraRot(self):
    #"""
    #Retorna a rotação
    #"""
    #return self.prop.MostraRot()

  #def MostraVelCom(self):
    #"""
    #Retorna a velocidade comandada
    #"""
    #return self.uc
    
  #def MudaVelCom(self, uc):
    #"""
    #Muda a velocidade comandada
    #"""
    #self.uc  = uc.copy()
    #self.prop.MudaVelCom(uc)
    
  #def MudaLemeCom(self, AngLeme):
    #"""
    #Muda o leme comandado da embarcação
    #__________________________
    #Variáveis de entrada:
    #"""
    #temp = AngLeme.copy()
    #self.leme.MudaLemeCom(temp)        

    
  #def MudaVel(self, Velocidade):
    #"""
    #Muda a velocidade da embarcação
    #__________________________
    #Variáveis de entrada:
    #Velocidade -- velocidade (m/s)
    #"""
    #temp = Velocidade.copy()
    
    #self.vel = temp        
    #self.casco.MudaVel(temp)
    #self.leme.MudaVel(temp)
    #self.prop.MudaVel(temp)

  #def MudaPos(self, Posicao):
    #"""
    #Muda a posição da embarcação 
    #__________________________
    #Variáveis de entrada:
    #Posição -- posição (m)
    #"""
    #temp = Posicao.copy()
    #self.pos = temp
    #self.casco.MudaPos(temp)
    #self.leme.MudaPos(temp)
    #self.prop.MudaPos(temp)


  #def MudaRotCom(self, Rot):
    #"""
    #Muda a rotação Comandada da embarcação
    #"""
    #self.prop.MudaRotCom(Rot)
    
  #def CalcFx(self):
    #"""
    #Calcula a força em Surge   
    #"""
    #m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    #u = self.MostraVel()[0] 
    #v = self.MostraVel()[1]
    #p = self.MostraVel()[3]
    #r = self.MostraVel()[5]
    #xg = self.dic['xg']
    #zg = self.dic['zg']
    
    #cori = m*(v*r + xg*(r**2) -  zg*p*r) 
    
    #if self.tipo == 'MARAD':
      #saida = (self.casco.Fx() + self.prop.Fx() +
          #self.leme.Fx(self.MostraRot(),
          #self.MostraVelCom()/self.MostraVel()[0]) + cori) 
    #elif self.tipo == 'TP':
      #saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx() + cori
  
    #return    saida

  #def CalcFy(self):
    #"""
    #Calcula a força em Sway
    #"""
    #m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    #u = self.MostraVel()[0] 
    #v = self.MostraVel()[1]
    #p = self.MostraVel()[3]
    #r = self.MostraVel()[5]
    #xg = self.dic['xg']
    #zg = self.dic['zg']
    
    #cori = -m*u*r
  
    #if self.tipo == 'MARAD':
      #saida = (self.casco.Fy() + self.leme.Fy(self.MostraRot()) +
          #self.prop.Fy() + cori)
    #elif self.tipo == 'TP':
      #saida = self.casco.Fy() + self.leme.Fy() + self.prop.Fy() + cori
  
    #return saida

  #def CalcK(self):
    #"""
    #Calcula o momento de Roll
    #"""
    #m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    #u = self.MostraVel()[0] 
    #v = self.MostraVel()[1]
    #p = self.MostraVel()[3]
    #r = self.MostraVel()[5]
    #xg = self.dic['xg']
    #zg = self.dic['zg']
    
    #cori = m*zg*u*r
  
    #if self.tipo == 'MARAD':
      #saida = (self.casco.K() + self.leme.K(self.MostraRot()) +
          #self.prop.K() + cori)
    #elif self.tipo == 'TP':
      #saida = self.casco.K() + self.leme.K() + self.prop.K() + cori
  
    #return    saida

  
  #def CalcN(self):
    #"""
    #Calcula o momento de  Yaw
    
    #"""
    #m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    #u = self.MostraVel()[0]
    #v = self.MostraVel()[1]
    #p = self.MostraVel()[3]
    #r = self.MostraVel()[5]
    #xg = self.dic['xg']
    #zg = self.dic['zg']
    
    #cori = -m*xg*u*r

    #if self.tipo == 'MARAD':
      #saida = (self.casco.N() + self.leme.N(self.MostraRot()) +
          #self.prop.N() + cori)
    #elif self.tipo == 'TP':
      #saida = self.casco.N() + self.leme.N() + self.prop.N() + cori
  
    #return saida
    
  #def VetF(self, p=None):
    #"""
    #Vetor de forças
    #_________________________
    #Variáveis de entrada:
    #p --  tupla
    #p[0] (integer)-- Graus de liberdade 
    #p[1] (tupla)-- Com pesos
    #"""
    #if p == None:
      #GrausDeLib =4
      #peso = None
    #elif len(p)==1:
      #GrausDeLib =p[0]
      #peso = None
    #elif len(p)==2:
      #GrausDeLib =p[0]
      #peso = p[1]
      
    #if peso == None:
      #if GrausDeLib == 4:
        #saida = sp.array([self.CalcFx(), self.CalcFy(),
                #self.CalcK(), self.CalcN()])  
      #elif GrausDeLib == 3:
        #saida = sp.array([self.CalcFx(), self.CalcFy(),
#self.CalcN()])
    #else:
      #lemearq = self.MostraLeme()
      #velarq = self.MostraVel()
      #uc = self.MostraVelCom()
      
      #####################
      
      #self.leme.MudaLemeDir(sp.array(0.))
      #self.MudaVelCom(velarq[0]) #condição eta=1
      
###            ####################
###            Aquilo que depende somente de u
###
###            ####################
      
      #veltemp = sp.zeros((6, 1))
      #veltemp[0] = velarq[0]
      #self.MudaVel(veltemp)
      
      #fu = self.VetF((GrausDeLib, ))

      #####################
      #veltemp = sp.zeros((6, 1))
      #veltemp[0] = velarq[0]
      #veltemp[1] = velarq[1]
      #self.MudaVel(veltemp)
      
      ## leme = 0 e eta = 1

      #fbeta = self.VetF((GrausDeLib, )) - fu
      #it = 0
      #fbeta1 = fbeta.copy()

      #for arg in peso[0]:

        #fbeta[it] = arg* fbeta[it]

        #it +=1 
      #####################

      
      
      #veltemp = sp.zeros((6, 1))
      #veltemp[5] = velarq[5]
      #veltemp[0] = velarq[0]            
      #self.MudaVel(veltemp)
      
      #fr = self.VetF((GrausDeLib, )) - fu
      #fr1 = fr.copy()

      #it = 0
      #for arg in peso[1]:
        #fr[it] = arg* fr[it]
        #it +=1                

      #####################
      
      
      
      #self.leme.MudaLemeDir(lemearq)
      #veltemp = sp.zeros((6, 1))
      #veltemp[0] = velarq[0]
      #self.MudaVel(veltemp)
      
      #fleme = self.VetF((GrausDeLib, ))  - fu
      
      #fleme1 = fleme.copy()

      #it = 0            
      #for arg in peso[2]:
        #fleme[it] = arg* fleme[it]
        #it +=1     
      

      #####################
      
      #self.MudaVel(velarq)
      #self.MudaVelCom(uc)
      
      #fbetarl = self.VetF((GrausDeLib, )) - (fbeta1 + fr1 + fleme1)
      #it = 0
    
      #for arg in peso[3]:
        #fbetarl[it] = arg* fbetarl[it]
        #it +=1                            
      #del it 
      
      
      
      #saida = fbeta + fr + fleme + fbetarl
    
    #return saida

  #def H (self, GrausDeLib=4):
    #"""
    #Matriz de massa menos matriz de massa adicional
    #_________________________
    #Variáveis de entrada:
    
    #GrausDeLib (integer)-- Graus de liberdade 
    #"""
    #H = None
    #H = self.casco.M(GrausDeLib) - self.casco.Ma(GrausDeLib)
    
    #return  sp.mat(H)

  #def MatRot(self, p=None):
    #"""
    #Retorna a matrix de rotação de do referêncial solidárial para o 
    #inercial
    #"""
    #if p== None:
      #roll= self.MostraPos()[3]
      #pitch = self.MostraPos()[4]
      #yaw = self.MostraPos()[5]
    #else:
      #roll= p[0]
      #pitch = p[1]
      #yaw = p[2]
      
    #Rot = sp.array([[sp.cos(yaw)*sp.cos(pitch), 
    #-sp.sin(yaw)*sp.cos(roll) +
#sp.cos(yaw)*sp.sin(pitch)*sp.sin(roll), 
    #sp.sin(yaw)*sp.sin(roll) + sp.cos(yaw)*sp.cos(roll)*sp.sin(pitch)
#], 
    #[sp.sin(yaw)*sp.cos(pitch), 
    #sp.cos(yaw)*sp.cos(roll) + sp.sin(roll)*sp.sin(pitch)*sp.sin(yaw), 
    #-sp.cos(yaw)*sp.sin(roll) + sp.sin(yaw)*sp.cos(roll)*sp.sin(pitch)
#], 
    #[-sp.sin(pitch), sp.cos(pitch)*sp.sin(roll), 
    #sp.cos(pitch)*sp.cos(roll)] ])
    
    #Rot.shape  = (3, 3)
    #Rot= sp.matrix(Rot)
    #return Rot

  #def f2 (self, VetF, H):
    #"""
    #Calcula o valor de f(x) na equação
    #x' = f(x)
    #onde x são é  o vetor de velocidades no sistema solidário
    #_________________________
    #Variáveis de entrada:
    
    #GrausDeLib (integer)-- Graus de liberdade 
    #"""
    
    #GrausDeLib = len(VetF)
      
    #if GrausDeLib == 4:
      #a=  sp.zeros((6, 6))
      #a[5, 5] = 1.
      #a[4, 4] = 1.
      #a[:4, :4]= H

      #b=  sp.zeros((6, 1))
      #b [4, 0] = self.vel[3]
      #b [5, 0] = self.vel[5]*sp.cos(self.MostraPos()[3])
      #b[:4, :]= VetF
    #elif GrausDeLib == 3:
      #a=  sp.zeros((4, 4))
      #a[3, 3] = 1.
      #a[:3, :3]= H

      #b=  sp.zeros((4, 1))
      #b[:3, :]= VetF
      #b[3, 0] = self.MostraVel()[5]
    
    #saida = linalg.solve(a, b ) 

    #return saida
    
  #def f(self, velocidade=None, t=None, p=(4, )):
    #"""
    #O p é uma tupla com o valor dos graus de liberdade
    #"""
    #GrausDeLib = p[0]
    #if velocidade !=None:
      #velarq = self.MostraVel()
      #posarq = self.MostraPos()
      #veltemp = sp.zeros((6, 1))
      #postemp =  sp.zeros((6, 1))
      #if GrausDeLib==3:
        #veltemp[:2] = velocidade[:2]
        #veltemp[5] = velocidade[2]
        #postemp[5] = velocidade[3]
      #elif GrausDeLib==4:
        #veltemp[:2] = velocidade[:2]
        #veltemp[3] = velocidade[2]
        #veltemp[5] = velocidade[3]
        #postemp[3] = velocidade[4]
        #postemp[5] = velocidade[5]
      #self.MudaVel(veltemp)
      #self.MudaPos(postemp)
    
    #if GrausDeLib == 4:
      #a=  sp.zeros((6, 6))
      #a[5, 5] = 1.
      #a[4, 4] = 1.
      #a[:4, :4]= self.H(GrausDeLib)

      #b=  sp.zeros((6, 1))
      #b [4, 0] = self.vel[3]
      #b [5, 0] = self.vel[5]*sp.cos(self.MostraPos()[3])
      #b[:4, :]= self.VetF(p)
    #elif GrausDeLib == 3:
      #a=  sp.zeros((4, 4))
      #a[3, 3] = 1.
      #a[:3, :3]= self.H(GrausDeLib)

      #b=  sp.zeros((4, 1))
      #b[:3, :]= self.VetF(p) 
      #b[3, 0] = self.MostraVel()[5]
    
    #saida = linalg.solve(a, b) 
    
    #if velocidade !=None:
      #self.MudaVel(velarq)
      #self.MudaPos(posarq)
    #return saida    
  #def fvein(self, x, t, p):
    #"""
    #x = sp.array(u, v , w)
    #p = (  roll, pitch, yaw)
    #"""
  
    #return sp.array(self.MatRot(p[0])*p[1])
    
  #def simula(self, met='euler', t0=0., dt=0.5, t=100., GrausDeLib=4,
        #velocidade=None, tipo='ZigZag', leme=sp.array(20.),
        #proa=sp.array(20.), RotCom =sp.array(1),osa=sp.array(0.05),
        #ospath=sp.array(150), erro=sp.array(0.05),
        #errotf=sp.array(0.05), errotd=sp.array(0.05)):
    #"""
    #Simulador de manobras padrão
    #_________________________
    #Variáveis de entrada:
    
    #GrausDeLib (integer)-- Graus de liberdade;        
    #met -- Método de integração. Default- Euler;
    #t0 -- Tempo inicial;
    #dt -- Passo no tempo;
    #t -- Tempo final 
    #tipo - tipo de manobra simulada. Zig-Zag10/10 e Curva_de_Giro_port
#ou 
    #Curva_de_Giro_starboard . Default -Zig-Zag
    
    #__________________________
    #Saída:
    
    #Tupla de sp.array
    
    #(veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis)
    
    #Em cada elemento da tupla:
    #A primeira coluna é o passo de tempo e as demais são as variáveis
    
    #veloHis -- histórico de velocidades;
    #posHis -- histórico de posições
    #acelHis --- histórico de acelerações
    #fHis -- histórico de forças 
    #veloInerHis -- histórico de velocidades no sistema inercial
    #lemeHis -- histórico do comando de leme
    #"""

##
##        Tipo de Simulação a ser realizada:
##
    #self.MudaPos( sp.array([  [0.], [0.], [0.], [0.], [0.], [0.] ]))
    #self.MudaVel(sp.array([  [self.dic['unom']], [0.], [0.], [0.], [0.],
    #[0.] ]))
    #self.MudaRotCom(RotCom)
    #self.MudaVelCom(self.dic['unom'])
##Log é o parâmetro que indica quando a simulação armazenou os dados do
##relatório
    #if tipo == 'Curva_de_Giro_port':
      #self.MudaLemeCom(sp.array(leme*sp.pi/180))
      #log = False
    #elif tipo == 'Curva_de_Giro_starboard':
      #self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      #log = False
    #elif tipo == 'ZigZag':
      #self.MudaLemeCom(sp.array(leme*sp.pi/180))
      #exe = 0
    
    

################################
###
###   Dados relacionados a curva de zizag
###
################################
      #if (tipo == 'ZigZag' and (((exe%2 == 0) and self.MostraPos()[5]
#<=
        #-(proa*sp.pi/180) ) or (exe%2 != 0 and self.MostraPos()[5]
#>=
        #(proa*sp.pi/180) ))):
        #self.MudaLemeCom(self.MostraLeme()*(-1))
        #if exe!=0:
          #dic['reach'] = erro
          #dic['ospath'] = ospath
          #dic['osangle'] = abs(osa - dic['proa'])
          #dados.append(dic.copy())

        #exe += 1
        #dic['exeNummber'] = exe
        #dic['time'] = tp - sp.array(dt)
        #dic['path'] = self.MostraPos()[1]
        #dic['proa'] = self.MostraPos()[5]
    
      #if tipo=='ZigZag' and exe!=0:
        #if abs(self.MostraPos()[1]- dic['path'])>ospath:
          #ospath = abs(self.MostraPos()[1]- dic['path'])  
        #if abs(self.MostraPos()[5])>abs(osa):
          #osa = self.MostraPos()[5]
        #if abs(self.MostraPos()[5] - PosIni[5]) < erro:
          #erro = abs(self.MostraPos()[5] - PosIni[5])            

        
      
      

################################
###
###   Dados relacionados a curva de Giro
###
################################            
      #if ((tipo == 'Curva_de_Giro_port' or
        #tipo == 'Curva_de_Giro_starboard') and not log):
        
        #if (abs(abs(self.MostraPos()[5] - PosIni[5]) -
          #(sp.array(90)*sp.pi/180)) <= errotf):
          #errotf = (abs(abs(self.MostraPos()[5] - PosIni[5]) -
              #(sp.array(90)*sp.pi/180)))
          #dic['transfer'] = abs(self.MostraPos()[1] - PosIni[1])
          #dic['advance'] = abs(self.MostraPos()[0] - PosIni[0])
        #if abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi) <= errotd:
          #errotd = abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi)
          #dic['taticalDiameter'] = abs(self.MostraPos()[1] - \
#PosIni[1])
        
        #if abs(self.MostraPos()[5] - PosIni[5]) > sp.pi :
          #log = True
          #dados.append(dic)


      #Rot = self.MatRot()
      
##
##                inc = Velocidades Lineares no Sistema Inecial
##
      #VelIn = Rot*sp.matrix(self.vel[0:3])

      #PosIne = self.MostraPos()[0:3]
      
###################################
##                
##                       Guardando os parâmetros
##                
###################################                
##          Velocidade Inercial      
      #d= sp.hstack(VelIn)
      #veloInerHis[cont, 1:] = d #
      #veloInerHis[cont, 0] = tp #
##           Histórico Leme
      #lemeHis[cont, 0] = tp
      #lemeHis[cont, 1] = self.MostraLeme()
##           Histórico da posição
      #temp = sp.hstack(self.MostraPos())
      #posHis[cont, :] = sp.hstack((tp, temp))

##           Histórico da Velocidade
      #temp = sp.hstack(self.MostraVel())
      #veloHis[cont, :] = sp.hstack((tp, temp))

##           Histórico das Forças 
      #temp =sp.hstack(sp.array(self.VetF(GrausDeLib)))
      #if GrausDeLib == 4:
        #fHis[cont, :]  = sp.hstack((tp, temp))
      #elif GrausDeLib == 3:
        #fHis[cont, :3]  = sp.hstack((tp, temp[:2]))
        #fHis[cont, 4]  = temp[2]

##           Histórico Propulsor
      #propHis[cont, :] = sp.hstack((tp, self.MostraRot()))

##           Histórico das Acelerações 
      #Acel = self.f(GrausDeLib)
      
      #if GrausDeLib == 4:
        #vetor = sp.zeros((6, 1))
        #vetor[:2] = Acel[:2]
        #vetor[3] = Acel[2]
        #vetor [5] = Acel[3]
      #elif GrausDeLib == 3:
        #vetor = sp.zeros((6, 1))
        #vetor[:2] = Acel[:2]
        #vetor [5] = Acel[2]
      #acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))           



      #del temp 
###############################
##
##    Criação de vetor de graus de liberdade
##
###############################
      #if GrausDeLib == 4:
        #xIn = sp.zeros([6, 1])
        
        #xIn [0] = self.MostraVel()[0]
        #xIn [1] = self.MostraVel()[1]
        #xIn [2] = self.MostraVel()[3]
        #xIn [3] = self.MostraVel()[5]
        #xIn [4] = self.MostraPos()[3]
        #xIn [5] = self.MostraPos()[5]
      #elif  GrausDeLib == 3:
        #xIn = sp.zeros([4, 1])
        #xIn [0] = self.MostraVel()[0]
        #xIn [1] = self.MostraVel()[1]
        #xIn [2] = self.MostraVel()[5]
        #xIn [3] = self.MostraPos()[5]         
###################################
##                
##                      Integração da Aceleração solidária
##                
###################################
      #if met == 'euler':
        #xIn =  self.integrador.euler(Acel, xIn, dt )
      #elif met =='rk4':
        #xIn = self.integrador.rk4(self.facel, dt, tp, xIn)
      
###################################
      #if GrausDeLib == 4:
        #x = sp.zeros((6, 1))
        #x[0] = xIn[0] 
        #x[1] = xIn[1] 
        #x[3] = xIn[2]
        #x[5] = xIn[3]
      #elif GrausDeLib==3:
        #x = sp.zeros((6, 1))
        #x[0] = xIn[0] 
        #x[1] = xIn[1] 
        #x[5] = xIn[2]                
      #self.MudaVel(x)               

      #del x
###################################
###                
###                       Integração da velocidade inercial
###                
####################################
      #posfutura = sp.zeros((6, 1))
      #posfutura[:3] = self.integrador.euler(VelIn, PosIne, dt)
      
###################################
      #if GrausDeLib== 4:
        #posfutura[3] = xIn[4]
        #posfutura[5] = xIn[5]
      #elif GrausDeLib== 3:
        #posfutura[5] = xIn[3]
        
      #self.MudaPos(posfutura)
      #cont += 1
      #del posfutura
      
      #self.prop.MudaRot(tp)
      #self.leme.MudaLeme(tp)

    #return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
#propHis, 
        #dados)
    
    
  #def getCurvaGiro(self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
          #GrausDeLib=3, tipo='port', leme=sp.array(20.),
          #RotCom=None, VelCom= None, Vel=None, Eta='vel',
          #PosIne=sp.array([[0.], [0.], [0.], [0.], [0.], [0.] ]),
          #errotf=sp.array(0.05), errotd=sp.array(0.05),
          #errosr=sp.array(0.001), saida='txt'):
    #"""
    #"""

    #if RotCom == None:
      #RotCom = self.dic['rotnom']
    #if VelCom == None:
      #VelCom = self.dic['unom']
    #if Vel ==  None:
      #Vel = sp.array([  [self.dic['unom']], [0.], [0.], [0.], [0.],
#[0.]
#])
    
    #self.MudaPos( PosIne)
    #self.MudaVel(Vel)
    #self.MudaRotCom(RotCom)
    #self.MudaVelCom(VelCom)

##Log é o parâmetro que indica quando a simulação armazenou os dados do
##relatório
    #if tipo == 'port':
      #self.MudaLemeCom(sp.array(leme*sp.pi/180))
      #log = False
      #log1 = False
    #elif tipo == 'starboard':
      #self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      #log = False
      #log1 = False
##
##   Criando espaço na memória para armazenar os parâmetros da curva
##
    #nlin = len(sp.arange(t0, t, dt)) #Número de linhas das colunas a serem
##criadas
    #if saida == 'mem':
      #lemeHis = sp.zeros((nlin, 2)) #historico do leme
      #veloHis = sp.zeros((nlin, 7)) #histórico da velocidade
      #veloInerHis = sp.zeros((nlin, 4))#histórico da velocidade no
##sistema inercial Verificar depois a necessidade
      #posHis =  sp.zeros([nlin, 7]) #histórico da posição no sistema
##inercial
      #fHis     = sp.zeros((nlin, 5)) #histórico de forças
      #acelHis = sp.zeros((nlin, 7)) #histórico de acelerações
      #propHis = sp.zeros((nlin, 2)) #histórico Máquina
      #EtaHis = sp.zeros((nlin, 2)) #histórico Eta
      #betaHis =  sp.zeros((nlin, 2)) #histórico beta
    #elif saida == 'txt':
      #os.makedirs('./saida/CurvaGiro')
      #os.chdir('./saida/CurvaGiro')
      #lemeHis = open('leme.dat', 'w')#historico do leme
      #lemeHis.write('#Navio ' + self.nome + '\n' +  
            #'#Manobra de Curva de Giro\n#\n') 
      #lemeHis.write('#Valor do leme em rad\n')
      #lemeHis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' +
            #'\n')
      
      #veloHis = open('velo.dat', 'w') #histórico da velocidade
      #veloHis.write('#Navio ' + self.nome + '\n' + 
            #'#Manobra de Curva de Giro\n#\n')
      #veloHis.write('#Velocidade Sistema Solidário \n#\n')
      #veloHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            #'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 
            #'dot roll'.rjust(11) + ' ' + 'dot pitch'.rjust(11)
#+ 
            #' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      #veloInerHis = open('veloiner.dat', 'w')#histórico da velocidade no
##sistema inercial Verificar depois a necessidade
      #veloInerHis.write('#Navio ' + self.nome + '\n' +  
              #'#Manobra de Curva de Giro\n#\n')
      #veloInerHis.write('#Velocidade Inercial\n#\n')
      #veloInerHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              #'v'.rjust(11) + ' ' + 'r'.rjust(11) + '\n') 

      #posHis =  open('pos.dat', 'w')#histórico da posição no sistema
##inercial
      #posHis.write('#Navio ' + self.nome + '\n' +  
            #'#Manobra de Curva de Giro\n#\n')
      #posHis.write('#Posição e Orientação\n#\n')
      #posHis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
            #'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
            #'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
            #'yaw'.rjust(11)  + ' ' + '\n') 

      #fHis     = open('forcas.dat', 'w') #histórico de forças
      #fHis.write('#Navio ' + self.nome + '\n' + 
          #'#Manobra de Curva de Giro\n#\n')
      #fHis.write('#Forças e Momentos\n#\n')
      #fHis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
          #'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
          #'N'.rjust(11) + ' ' + '\n') 
      
      #acelHis = open('acel.dat', 'w') #histórico de acelerações
      #acelHis.write('#Navio ' + self.nome + '\n' +  
            #'#Manobra de Curva de Giro\n#\n')
      #acelHis.write('#Aceleração\n#\n')
      #acelHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            #'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
            #'ddotroll'.rjust(11) + ' ' + 'ddotpitch'.rjust(11)
#+              ' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      #propHis = open('propulsor.dat', 'w') #histórico Máquina
      #propHis.write('#Navio ' + self.nome + '\n' + 
            #'#Manobra de Curva de Giro\n#\n')
      #propHis.write('#Rotações do propulsor\n#\n')
      #propHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      #EtaHis = open('Eta.dat', 'w') #histórico Eta
      #EtaHis.write('#Navio ' + self.nome + '\n' +  
            #'#Manobra de Curva de Giro\n#\n')
      #EtaHis.write('#Eta \n#\n')
      #EtaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' +
#'\n')


      #betaHis = open('beta.dat', 'w') #histórico Eta
      #betaHis.write('#Navio ' + self.nome + '\n' +  
            #'#Manobra de Curva de Giro\n#\n')
      #betaHis.write('#Beta \n#\n')
      #betaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' +
            #'\n')
      
      #os.chdir('..')
      #os.chdir('..')
    
    #dados = []
    #dic = {}
    #PosIni = self.MostraPos().copy()           

    #del nlin #não preciso mais
    #cont =0 #Contador
    
    #if peso == None:   
      #par =   (GrausDeLib, )
    #else:
      #par = (GrausDeLib, peso)
##
##   Iteração
##

    #for tp in sp.arange(t0, t, dt):
      #if not log1:
        #if cont == 0:
          #V1 = sp.sqrt(self.MostraVel()[0]**2 +
                #self.MostraVel()[1]**2)
        #elif cont == 1:
          #V2 = sp.sqrt(self.MostraVel()[0]**2 +
                #self.MostraVel()[1]**2)
        #elif cont == 2:
          #V3 = sp.sqrt(self.MostraVel()[0]**2 +
                #self.MostraVel()[1]**2)
        #elif cont == 3:
          #V4 = sp.sqrt(self.MostraVel()[0]**2 +
                #self.MostraVel()[1]**2)
        #else:
          #V1 = V2
          #V2 = V3
          #V3 = V4
          #V4 = sp.sqrt(self.MostraVel()[0]**2 +
                #self.MostraVel()[1]**2)                
        #if log:
          #if stats.tstd((V1, V2, V3, V4))<errosr:
            #dic['steadytr'] = (sp.sqrt(self.MostraVel()[0]**2 +
                        #self.MostraVel()[1]**2) /
                    #self.MostraVel()[5])
            #dados.append(dic.copy())
            #log1= True
          
        #if  not log:
          #if (abs(abs(self.MostraPos()[5] - PosIni[5]) - 
              #(sp.pi/2)) <= errotf):
            #errotf = (abs(abs(self.MostraPos()[5] - PosIni[5]) -
                  #(sp.pi/2)))
            #dic['transfer'] = abs(self.MostraPos()[1] - PosIni[1])
            #dic['advance'] = abs(self.MostraPos()[0] - PosIni[0])
          #if (abs(abs(self.MostraPos()[5] - PosIni[5]) - sp.pi) <=
            #errotd):
            #errotd = abs(abs(self.MostraPos()[5] - PosIni[5]) -
                  #sp.pi)
            #dic['taticalDiameter'] = abs(self.MostraPos()[1] -
                          #PosIni[1])
          #if abs(self.MostraPos()[5] - PosIni[5]) > sp.pi:
            #log = True


####################################
      #ft = self.VetF(par) 
####################################
###
###                inc = Velocidades Lineares no Sistema Inecial
###
####################################
      #MatRot = self.MatRot()
      
      #VelIn = sp.array(MatRot*self.MostraVel()[0:3])

      #PosIne = self.MostraPos()[0:3]


###################################
###                
###                       Guardando os parâmetros
###                
###################################                
##          Velocidade Inercial
      #if saida == 'txt':
        #veloInerHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in VelIn:
          #veloInerHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #veloInerHis.write('\n')
      #elif saida == 'mem':
        #d = sp.hstack(VelIn)
        #veloInerHis[cont, 1:] = d #
        #veloInerHis[cont, 0] = tp #
##           Histórico Leme
      #if saida == 'txt':
        #lemeHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #lemeHis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      #elif saida == 'mem':
        #lemeHis[cont, 0] = tp
        #lemeHis[cont, 1] = self.MostraLeme()
##           Histórico da posição
      #if saida == 'txt':
        #posHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in self.MostraPos():
          #posHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #posHis.write('\n')
      #elif saida == 'mem':            
        #temp = sp.hstack(self.MostraPos())
        #posHis[cont, :] = sp.hstack((tp, temp))
        #del temp
##           Histórico da Velocidade
      #if saida == 'txt':
        #veloHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in self.MostraVel():
          #veloHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #veloHis.write('\n')
      #elif saida == 'mem': 
        #temp = sp.hstack(self.MostraVel())
        #veloHis[cont, :] = sp.hstack((tp, temp))
        #del temp
##           Histórico das Forças 
      #if saida == 'txt':
        #temp = sp.zeros((4, 1))
        #if GrausDeLib == 4:
          #temp= ft
        #elif GrausDeLib == 3:
          #temp[:2]  = ft[:2]
          #temp[3]  = ft[2]
        #fHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in temp:
          #fHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #fHis.write('\n')
      #elif saida == 'mem': 
        #temp = sp.hstack(sp.array(ft))
        #if GrausDeLib == 4:
          #fHis[cont, :] = sp.hstack((tp, temp))
        #elif GrausDeLib == 3:
          #fHis[cont, :3] = sp.hstack((tp, temp[:2]))
          #fHis[cont, 4] = temp[2]

##           Histórico Propulsor
      #if saida == 'txt':
        #propHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #propHis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      #elif saida == 'mem':
        #propHis[cont, :] = sp.hstack((tp, self.MostraRot()))
##           Histórico Eta
      #if saida == 'txt':
        #EtaHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #if Eta == 'rot':
          #EtaHis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                #self.MostraRot()) + '\n')
        #elif Eta == 'vel':
          #EtaHis.write('%.2f'.rjust(5) %
                #(self.MostraVelCom() / self.MostraVel()[0])
#+
                #'\n')
      #elif saida == 'mem':
        #if Eta== 'rot':
          #EtaHis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
          #self.MostraRot()))
        #elif Eta == 'vel':
          #EtaHis[cont, :] = sp.hstack((tp, 
                        #self.MostraVelCom() /
                        #self.MostraVel()[0]))

##           Histórico Beta
      #if saida == 'txt':
        #betaHis.write('%.2f'.rjust(5) % (tp) + ' ')
        #betaHis.write(('%.2f'.rjust(5) % 
              #sp.arctan(-self.MostraVel()[1] /
              #self.MostraVel()[0])) + '\n')
        
      #elif saida == 'mem':
        #betaHis[cont, :] = sp.hstack((tp,
                      #sp.arctan(-self.MostraVel()[1]
#/
                      #self.MostraVel()[0])))

##           Histórico das Acelerações 
      #Acel = self.f2(ft, self.H(GrausDeLib))
      #vetor = sp.zeros((6, 1))
      #if GrausDeLib == 4:
        #vetor[:2] = Acel[:2]
        #vetor[3] = Acel[2]
        #vetor [5] = Acel[3]
      #elif GrausDeLib == 3:
        #vetor[:2] = Acel[:2]
        #vetor [5] = Acel[2]
      #if saida == 'txt':
        #acelHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in vetor:
          #acelHis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        #acelHis.write('\n')
      #elif saida == 'mem':  
        #acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       

  
  
        #del temp 
###############################
##
##    Criação de vetor de graus de liberdade
##
###############################
      #if GrausDeLib == 4:
        #vt = sp.zeros([6, 1])
        
        #vt [0] = self.MostraVel()[0]
        #vt [1] = self.MostraVel()[1]
        #vt [2] = self.MostraVel()[3]
        #vt [3] = self.MostraVel()[5]
        #vt [4] = self.MostraPos()[3]
        #vt [5] = self.MostraPos()[5]
      #elif  GrausDeLib == 3:
        #vt = sp.zeros([4, 1])
        #vt [0] = self.MostraVel()[0]
        #vt [1] = self.MostraVel()[1]
        #vt [2] = self.MostraVel()[5]
        #vt [3] = self.MostraPos()[5]         
###################################
###                
###                      Integração da Aceleração solidária
###                
###################################
      #if met == 'euler':
        #vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      #elif met =='rk4':
        #vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
###################################
      #if GrausDeLib == 4:
        #v = sp.zeros((6, 1))
        #v[0] = vt[0] 
        #v[1] = vt[1] 
        #v[3] = vt[2]
        #v[5] = vt[3]
      #elif GrausDeLib == 3:
        #v = sp.zeros((6, 1))
        #v[0] = vt[0] 
        #v[1] = vt[1] 
        #v[5] = vt[2]                
      #self.MudaVel(v)               

      #del v
###################################
###                
###                       Integração da velocidade inercial
###                
####################################
      #x = sp.zeros((6, 1))
      #if met == 'euler':
        #x[:3] = self.integrador.euler(self.fvein ,
                      #self.MostraPos()[:3], tp, dt ,
                      #(self.MostraPos()[3:] ,
                      #self.MostraVel()[:3])) 
      #elif met == 'rk4':
        #x[:3] = self.integrador.rk4(self.fvein, self.MostraPos()[:3],
                      #tp, dt, (self.MostraPos()[3:],
                      #self.MostraVel()[:3]))
###################################
      #if GrausDeLib == 4:
        #x[3] = vt[4]
        #x[5] = vt[5]
      #elif GrausDeLib == 3:
        #x[5] = vt[3]
        
      #self.MudaPos(x)
      
      #del x
      #cont += 1
      #self.prop.MudaRot(tp)
      #self.leme.MudaLeme(tp)
    #if saida == 'txt':
      #arq = [veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
        #propHis, EtaHis]
      #for arg in arq:
        #arg.close()
      #return dados
    #elif saida == 'mem':
      #return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
          #propHis, EtaHis, dados, betaHis)

  #def getCurvaZigZag(self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
                      #GrausDeLib=3, tipo='port', leme=sp.array(20.),
                      #RotCom=None, VelCom=None, Vel=None,
                      #proa=sp.array([20.]), Eta='vel', 
                      #PosIne=sp.array([[0.],[0.],[0.], [0.], [0.], [0.]]),
                      #osa=sp.array(0.0), ospath=sp.array(0.0),
                      #erro=sp.array(0.005),saida='txt'):
    #"""
    #Simulador de manobras padrão
    #_________________________
    #Variáveis de entrada:
    
    #GrausDeLib (integer)-- Graus de liberdade;        
    #met -- Método de integração. Default- Euler;
    #t0 -- Tempo inicial;
    #dt -- Passo no tempo;
    #t -- Tempo final 
    #tipo - tipo de manobra simulada. Zig-Zag10/10 e Curva_de_Giro_port
#ou
#Curva_de_Giro_starboard . Default -Zig-Zag
    
    #__________________________
    #Saída:
    
    #Tupla de sp.array
    
    #(veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis)
    
    #Em cada elemento da tupla:
    #A primeira coluna é o passo de tempo e as demais são as variáveis
    
    #veloHis -- histórico de velocidades;
    #posHis -- histórico de posições
    #acelHis --- histórico de acelerações
    #fHis -- histórico de forças 
    #veloInerHis -- histórico de velocidades no sistema inercial
    #lemeHis -- histórico do comando de leme
    #"""

    #if RotCom == None:
      #RotCom = self.dic['rotnom']
    #if VelCom == None:
      #VelCom = self.dic['unom']
    #if Vel ==  None:
      #Vel = sp.array([[self.dic['unom']], [0.], [0.], [0.], [0.], [0.]
              #])
    
    #self.MudaPos( PosIne)
    #self.MudaVel(Vel)
    #self.MudaRotCom(RotCom)
    #self.MudaVelCom(VelCom)


    #if tipo == 'port':
      #self.MudaLemeCom(sp.array(leme*sp.pi/180))
      #exe=0
    #elif tipo == 'starboard':
      #self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      #exe=1

    
##
##   Criando espaço na memória para armazenar os parâmetros da curva
##
##Número de linhas das colunas a seremcriadas
    #nlin = len(sp.arange(t0, t, dt)) 

    #if saida == 'mem':
      #lemeHis = sp.zeros((nlin, 2)) #historico do leme
      #veloHis = sp.zeros((nlin, 7)) #histórico da velocidade
      #veloInerHis = sp.zeros((nlin, 4))#histórico da velocidade no
##sistema inercial Verificar depois a necessidade
      #posHis =  sp.zeros([nlin, 7]) #histórico da posição no sistema
##inercial
      #fHis     = sp.zeros((nlin, 5)) #histórico de forças
      #acelHis = sp.zeros((nlin, 7)) #histórico de acelerações
      #propHis = sp.zeros((nlin, 2)) #histórico Máquina
      #EtaHis = sp.zeros((nlin, 2)) #histórico Eta
    #elif saida == 'txt':
      #os.makedirs('./saida/ZigZag')
      #os.chdir('./saida/ZigZag')
      #lemeHis = open('leme.dat', 'w')#historico do leme
      #lemeHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #lemeHis.write('#Valor do leme em rad\n')
      #lemeHis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' +
            #'\n')
      
      #veloHis = open('velo.dat', 'w') #histórico da velocidade
      #veloHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #veloHis.write('#Velocidade Sistema Solidário \n#\n')
      #veloHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              #'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 'dot \
              #roll'.rjust(11) + ' ' + ' dot pitch'.rjust(11)  + 
              #' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      #veloInerHis = open('veloiner.dat', 'w')#histórico da velocidade no
##sistema inercial Verificar depois a necessidade
      #veloInerHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de \
              #Curva de Zig-Zag\n#\n')
      #veloInerHis.write('#Velocidade Inercial\n#\n')
      #veloInerHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              #'v'.rjust(11)  + ' '  + 'r'.rjust(11) + '\n') 

      #posHis =  open('pos.dat', 'w')#histórico da posição no sistema
##inercial
      #posHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #posHis.write('#Posição e Orientação\n#\n')
      #posHis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
            #'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
            #'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
            #'yaw'.rjust(11) + ' ' + '\n') 

      #fHis = open('forcas.dat', 'w') #histórico de forças
      #fHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva de \
            #Zig-Zag\n#\n')
      #fHis.write('#Forças e Momentos\n#\n')
      #fHis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
          #'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
          #'N'.rjust(11) + ' ' + '\n') 
      
      #acelHis = open('acel.dat', 'w') #histórico de acelerações
      #acelHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #acelHis.write('#Aceleração\n#\n')
      #acelHis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
            #'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
            #'ddotroll'.rjust(11) + ' ' + ' ddotpitch'.rjust(11)
            #+ ' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      #propHis = open('propulsor.dat', 'w') #histórico Máquina
      #propHis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #propHis.write('#Rotações do propulsor\n#\n')
      #propHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      #EtaHis = open('Eta.dat', 'w') #histórico Eta
      #EtaHis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            #de Zig-Zag\n#\n')
      #EtaHis.write('#Eta \n#\n')
      #EtaHis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' + 
            #'\n')
      
      #os.chdir('..')
      #os.chdir('..')
      
    #dados = []
    #dic = {}
    #PosIni = self.MostraPos().copy()           

    #del nlin #não preciso mais
    #cont =0 #Contador
    
    #if peso == None:   
      #par =   (GrausDeLib, )
    #else:
      #par = (GrausDeLib, peso)
    

##
##   Iteração
##

    #for tp in sp.arange(t0, t, dt):

################################
###
###   Verificando o momento em que será realizada a mudança do leme
###
################################
      #if (((exe%2 == 0) and self.MostraPos()[5] <= 
        #-(proa * sp.pi / 180)) or (exe%2 != 0 and 
        #self.MostraPos()[5] >= (proa * sp.pi / 180))):
          #self.MudaLemeCom(self.MostraLeme() * (-1))
          #if ((exe != 0 and tipo == 'port') or (exe != 1
            #and tipo == 'starboard')):
              #dic['reach'] = erro
              #dic['ospath'] = ospath
              #dic['osangle'] = osa
              #dados.append(dic.copy())
        
          #osa = sp.array(0.0)
          #ospath = sp.array(0)
          #erro = sp.array(0.05)
          #logospath = False
          #logosa = False
          #exe += 1
          #if tipo =='port':
            #dic['exeNummber'] = exe
          #elif tipo=='starboard':
            #dic['exeNummber'] = exe - 1
          #dic['time'] = tp - sp.array(dt)
          #dic['path'] = self.MostraPos()[1]
          #dic['proa'] = self.MostraPos()[5]

################################
###
###   Atualizando os parâmetros
###
################################
      
      #if ((exe!=0 and tipo == 'port') or (exe!=1 and tipo ==
        #'starboard')):
        #if ((logospath == False) and
          #(abs(self.MostraPos()[1] - dic['path']) >= ospath)):
##(sp.sign(self.MostraPos()[1])== sp.sign(dic['path'])) and
          #ospath = abs(self.MostraPos()[1] - dic['path'])
        #else:
          #logospath = True
        
        #if ((logosa == False) and (abs(self.MostraPos()[5] - 
          #dic['proa']) >= osa)): #(sp.sign(self.MostraPos()[5])==
##sp.sign(dic['proa'])) and 
          #osa = abs(self.MostraPos()[5] - dic['proa'])
        #else:
          #logosa = True
          
        #if abs(abs(self.MostraPos()[5]) - abs(PosIni[5])) < erro:
          #erro = abs(self.MostraPos()[5] - PosIni[5])            

      
  
      
      
##
##                inc = Velocidades Lineares no Sistema Inecial
##
      #MatRot = self.MatRot()
      #VelIn = MatRot * sp.matrix(self.vel[0:3])

      #PosIne = self.MostraPos()[0:3]

####################################

##################################
###
###  Cálculo das forças de Maneira Modular
###
####################################
      #ft = self.VetF(par)

###################################
###################################
###                
###                       Guardando os parâmetros
###                
###################################                
##          Velocidade Inercial
      #if saida == 'txt':
        #veloInerHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in VelIn:
          #veloInerHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #veloInerHis.write('\n')
      #elif saida == 'mem':
        #d = sp.hstack(VelIn)
        #veloInerHis[cont, 1:] = d #
        #veloInerHis[cont, 0] = tp #
##           Histórico Leme
      #if saida == 'txt':
        #lemeHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #lemeHis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      #elif saida == 'mem':
        #lemeHis[cont, 0] = tp
        #lemeHis[cont, 1] = self.MostraLeme()
##           Histórico da posição
      #if saida == 'txt':
        #posHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in self.MostraPos():
          #posHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #posHis.write('\n')
      #elif saida == 'mem':            
        #temp = sp.hstack(self.MostraPos())
        #posHis[cont, :] = sp.hstack((tp, temp))
        #del temp
##           Histórico da Velocidade
      #if saida == 'txt':
        #veloHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in self.MostraVel():
          #veloHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #veloHis.write('\n')
      #elif saida == 'mem': 
        #temp = sp.hstack(self.MostraVel())
        #veloHis[cont, :] = sp.hstack((tp, temp))
        #del temp
##           Histórico das Forças 
      #if saida == 'txt':
        #temp = sp.zeros((4, 1))
        #if GrausDeLib == 4:
          #temp = ft
        #elif GrausDeLib == 3:
          #temp[:2] = ft[:2]
          #temp[3] = ft[2]
        #fHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in temp:
          #fHis.write('%.5e'.rjust(11)%(arg) + ' ')
        #fHis.write('\n')
      #elif saida == 'mem': 
        #temp = sp.hstack(sp.array(ft))
        #if GrausDeLib == 4:
          #fHis[cont, :] = sp.hstack((tp, temp))
        #elif GrausDeLib == 3:
          #fHis[cont, :3] = sp.hstack((tp, temp[:2]))
          #fHis[cont, 4] = temp[2]

##           Histórico Propulsor
      #if saida == 'txt':
        #propHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #propHis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      #elif saida == 'mem':
        #propHis[cont, :] = sp.hstack((tp, self.MostraRot()))
##           Histórico Eta
      #if saida == 'txt':
        #EtaHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #if Eta == 'rot':
          #EtaHis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                #self.MostraRot()) + '\n')
        #elif Eta == 'vel':   
          #EtaHis.write('%.2f'.rjust(5) % (self.MostraVelCom() /
                #self.MostraVel()[0]) + '\n')
      #elif saida == 'mem':
        #if Eta== 'rot':
          #EtaHis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
                        #self.MostraRot()))
        #elif Eta == 'vel':
          #EtaHis[cont, :] = sp.hstack((tp, self.MostraVelCom() /
                        #self.MostraVel()[0]))

##           Histórico das Acelerações 
      #Acel = self.f2(ft, self.H(GrausDeLib))
      #vetor = sp.zeros((6, 1))
      #if GrausDeLib == 4:
        #vetor[:2] = Acel[:2]
        #vetor[3] = Acel[2]
        #vetor [5] = Acel[3]
      #elif GrausDeLib == 3:
        #vetor[:2] = Acel[:2]
        #vetor [5] = Acel[2]
      #if saida == 'txt':
        #acelHis.write('%.2f'.rjust(5)%(tp) + ' ')
        #for arg in vetor:
          #acelHis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        #acelHis.write('\n')
      #elif saida == 'mem':  
        #acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       

  
      #del vetor 

###############################
###
###    Criação de vetor de graus de liberdade
###
###############################
      #if GrausDeLib == 4:
        #vt = sp.zeros([6, 1])
        
        #vt [0] = self.MostraVel()[0]
        #vt [1] = self.MostraVel()[1]
        #vt [2] = self.MostraVel()[3]
        #vt [3] = self.MostraVel()[5]
        #vt [4] = self.MostraPos()[3]
        #vt [5] = self.MostraPos()[5]
      #elif  GrausDeLib == 3:
        #vt = sp.zeros([4, 1])
        #vt [0] = self.MostraVel()[0]
        #vt [1] = self.MostraVel()[1]
        #vt [2] = self.MostraVel()[5]
        #vt [3] = self.MostraPos()[5]         
###################################
###                
###                      Integração da Aceleração solidária
###                
###################################
      #if met == 'euler':
        #vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      #elif met =='rk4':
        #vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
###################################
      #if GrausDeLib == 4:
        #v = sp.zeros((6, 1))
        #v[0] = vt[0] 
        #v[1] = vt[1] 
        #v[3] = vt[2]
        #v[5] = vt[3]
      #elif GrausDeLib ==3:
        #v = sp.zeros((6, 1))
        #v[0] = vt[0] 
        #v[1] = vt[1] 
        #v[5] = vt[2]                
      #self.MudaVel(v)               

      #del v
###################################
###                
###                       Integração da velocidade inercial
###                
####################################
      #x = sp.zeros((6, 1))
      #if met == 'euler':
        #x[:3] = self.integrador.euler(self.fvein,
#self.MostraPos()[:3],
                      #tp, dt, (self.MostraPos()[3:],
                      #self.MostraVel()[:3]))
      #elif met == 'rk4':
        #x[:3] = self.integrador.rk4(self.fvein,
#self.MostraPos()[:3],
                      #tp, dt, (self.MostraPos()[3:],
                      #self.MostraVel()[:3]))
###################################
      #if GrausDeLib == 4:
        #x[3] = vt[4]
        #x[5] = vt[5]
      #elif GrausDeLib == 3:
        #x[5] = vt[3]
        
      #self.MudaPos(x)
      #cont += 1
      #del x
      
      #self.prop.MudaRot(tp)
      #self.leme.MudaLeme(tp)

    #if saida == 'txt':
      #arq = [veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
        #propHis, EtaHis]
      #for arg in arq:
        #arg.close()
      #return dados
    #elif saida == 'mem':
      #return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
          #propHis, EtaHis, dados)

  #def simulaTestb(self, p, intervalo=sp.array(5.), V= None ):
    #"""
    #Retorna uma matrix com o valor das forças variando de acordo com
#que
#varia a velocidade 
    #u= Vcos(beta) v = Vsen(beta) com beta variando de 0 a 180 graus em
#um
#intervalo = intervalo        
    #"""
    
    #if V == None:
      #V = self.dic['unom']
      
    #Velocidade = sp.zeros((6, 1))
    #saida = sp.zeros([len( sp.arange(0., sp.pi, intervalo * sp.pi /
#180)),
            #5])
    #contlinha = 0
    
    #for beta in sp.arange(0., sp.pi, intervalo * sp.pi / 180):
      #Velocidade[0] = sp.array(V) * sp.cos(beta)
      #Velocidade[1] = -sp.array(V) * sp.sin(beta)
      #self.MudaVelCom(Velocidade[0]) #condição que força \eta=1
      #self.MudaVel(Velocidade)
      #v = sp.sqrt(Velocidade[0] ** 2 + Velocidade[1] ** 2)
      #rho = self.dic['rho']
      #lpp = self.dic['lpp']
      #vetF = self.VetF((4, p))
##            vetF = sp.hstack(vetF)
      #saida[contlinha, :] = sp.hstack([beta, vetF[0] * (2 / (rho *
#(lpp *
                      #(v ** 2)))), vetF[1] * (2 /
#(rho *
                      #(lpp* (v ** 2)))), vetF[2] *
                      #(2 / (rho * ((lpp * v) ** 2))),
                      #vetF[3] * (2 / (rho * ((lpp * v) **
                      #2)))])
      #contlinha += 1
    
    #return saida

#if __name__ == '__main__':
  #main()

      elif saida == 'mem': 
        temp = sp.hstack(sp.array(ft))
        if GrausDeLib == 4:
          fHis[cont, :] = sp.hstack((tp, temp))
        elif GrausDeLib == 3:
          fHis[cont, :3] = sp.hstack((tp, temp[:2]))
          fHis[cont, 4] = temp[2]

#           Histórico Propulsor
      if saida == 'txt':
        propHis.write('%.2f'.rjust(5)%(tp) + ' ')
        propHis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      elif saida == 'mem':
        propHis[cont, :] = sp.hstack((tp, self.MostraRot()))
#           Histórico Eta
      if saida == 'txt':
        EtaHis.write('%.2f'.rjust(5)%(tp) + ' ')
        if Eta == 'rot':
          EtaHis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                self.MostraRot()) + '\n')
        elif Eta == 'vel':   
          EtaHis.write('%.2f'.rjust(5) % (self.MostraVelCom() /
                self.MostraVel()[0]) + '\n')
      elif saida == 'mem':
        if Eta== 'rot':
          EtaHis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
                        self.MostraRot()))
        elif Eta == 'vel':
          EtaHis[cont, :] = sp.hstack((tp, self.MostraVelCom() /
                        self.MostraVel()[0]))

#           Histórico das Acelerações 
      Acel = self.f2(ft, self.H(GrausDeLib))
      vetor = sp.zeros((6, 1))
      if GrausDeLib == 4:
        vetor[:2] = Acel[:2]
        vetor[3] = Acel[2]
        vetor [5] = Acel[3]
      elif GrausDeLib == 3:
        vetor[:2] = Acel[:2]
        vetor [5] = Acel[2]
      if saida == 'txt':
        acelHis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vetor:
          acelHis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        acelHis.write('\n')
      elif saida == 'mem':  
        acelHis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       

  
      del vetor 

##############################
##
##    Criação de vetor de graus de liberdade
##
##############################
      if GrausDeLib == 4:
        vt = sp.zeros([6, 1])
        
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[3]
        vt [3] = self.MostraVel()[5]
        vt [4] = self.MostraPos()[3]
        vt [5] = self.MostraPos()[5]
      elif  GrausDeLib == 3:
        vt = sp.zeros([4, 1])
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[5]
        vt [3] = self.MostraPos()[5]         
##################################
##                
##                      Integração da Aceleração solidária
##                
##################################
      if met == 'euler':
        vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      elif met =='rk4':
        vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
##################################
      if GrausDeLib == 4:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1] 
        v[3] = vt[2]
        v[5] = vt[3]
      elif GrausDeLib ==3:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1] 
        v[5] = vt[2]                
      self.MudaVel(v)               

      del v
##################################
##                
##                       Integração da velocidade inercial
##                
###################################
      x = sp.zeros((6, 1))
      if met == 'euler':
        x[:3] = self.integrador.euler(self.fvein,
self.MostraPos()[:3],
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()[:3]))
      elif met == 'rk4':
        x[:3] = self.integrador.rk4(self.fvein,
self.MostraPos()[:3],
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()[:3]))
##################################
      if GrausDeLib == 4:
        x[3] = vt[4]
        x[5] = vt[5]
      elif GrausDeLib == 3:
        x[5] = vt[3]
        
      self.MudaPos(x)
      cont += 1
      del x
      
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)

    if saida == 'txt':
      arq = [veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
        propHis, EtaHis]
      for arg in arq:
        arg.close()
      return dados
    elif saida == 'mem':
      return (veloHis, posHis, acelHis, fHis, veloInerHis, lemeHis,
          propHis, EtaHis, dados)

  def simulaTestb(self, p, intervalo=sp.array(5.), V= None ):
    """
    Retorna uma matrix com o valor das forças variando de acordo com
que
varia a velocidade 
    u= Vcos(beta) v = Vsen(beta) com beta variando de 0 a 180 graus em
um
intervalo = intervalo        
    """
    
    if V == None:
      V = self.dic['unom']
      
    Velocidade = sp.zeros((6, 1))
    saida = sp.zeros([len( sp.arange(0., sp.pi, intervalo * sp.pi /
180)),
            5])
    contlinha = 0
    
    for beta in sp.arange(0., sp.pi, intervalo * sp.pi / 180):
      Velocidade[0] = sp.array(V) * sp.cos(beta)
      Velocidade[1] = -sp.array(V) * sp.sin(beta)
      self.MudaVelCom(Velocidade[0]) #condição que força \eta=1
      self.MudaVel(Velocidade)
      v = sp.sqrt(Velocidade[0] ** 2 + Velocidade[1] ** 2)
      rho = self.dic['rho']
      lpp = self.dic['lpp']
      vetF = self.VetF((4, p))
#            vetF = sp.hstack(vetF)
      saida[contlinha, :] = sp.hstack([beta, vetF[0] * (2 / (rho *
(lpp *
                      (v ** 2)))), vetF[1] * (2 /
(rho *
                      (lpp* (v ** 2)))), vetF[2] *
                      (2 / (rho * ((lpp * v) ** 2))),
                      vetF[3] * (2 / (rho * ((lpp * v) **
                      2)))])
      contlinha += 1
    
    return saida

if __name__ == '__main__':
  print ("Módulo chamado pelo mesmo módulo")
else:
  print ("Módulo chamado por outro módulo")
