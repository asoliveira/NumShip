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
Navio Module
============

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
  :author: Alex S. Oliveira
  
  """
  
  
  def __init__(self):
    """
    """
    
    pass
    
  def rk4(self, function, x, t0, dt, par=None):
    """
    Integrador runge-kutta
    
    :par: São os parâmetros de entrada da função.
    """
    k1 = function(x, t0, par)
    k2 = function(x + (1./2)*dt*k1, t0 + (1./2)*dt, par)
    k3 = function(x + (1./2)*dt*k2, t0 + (1./2)*dt, par)
    k4 = function(x + dt*k3, t0 + dt, par)
  
    xt = x + 1./6*(k1+ 2.*k2+ 2.*k3+ k4)*dt
  
    return xt
  
  def euler(self, f, x, t0, dt, par=None ):
    """
    """      
    return x + f(x, t0, par)*dt

  
  
class navio:
  """Classe de navios"""
  
  def __init__ (self, dicvar, nome = 'navioteste', tipo = 'MARAD'):
    """"Construtor do navio
    
    :param dicvar: Dicionário de derivadas hidrodinâmicas e parâmetros
                   necessários para a construção do navio;
    :param nome: Nome do navio. Não possui relevância(default = 'navioteste');
    :param tipo: Tipo de modelo matemático adotado para a construção do navio
                 (default = 'MARAD')
                 As opções são:
                 MARAD
                 MARAD-L1
                 MARAD-P
                 TP;
    :type dicvar: dict
    :type nome: str
    :type tipo: str 

    """
    
    self.nome = nome
    self.vel = sp.zeros((6, 1))
    self.acel = sp.zeros((6, 1))
    self.pos = sp.zeros((6, 1))
    self.dic = dicvar
    self.tipo = tipo
    self.integrador = inte()
    self.uc = sp.array(self.dic['unom'])
    
    if tipo == 'TP':
      self.leme = lemeTris(dicvar)
      self.casco = cascoTris(dicvar)
      self.prop = prop()
    elif tipo == 'MARAD':
      self.leme = lemeMarAd(dicvar)
      self.casco = cascoMarAd(dicvar)
      self.prop = propMarAd(dicvar)
    elif tipo == 'MARAD-L1':
      self.leme = leme1(dicvar)
      self.casco = cascoMarAd(dicvar)
      self.prop = propMarAd(dicvar)
    elif tipo == 'MARAD-P':
      self.leme = lemep(dicvar)
      self.casco = cascoMarAd(dicvar)
      self.prop = propMarAd(dicvar)
      
  def MostraVel (self):
    """Retorna a Velocidade da embarcação"""
    
    return self.vel.copy()
    
  def MostraAcel (self):
    """Retorna a aceleração da embarcação"""
    
    return self.acel.copy()
  
  def MostraLeme (self):
    """Retorna o leme em rad da embarcação"""
    
    return self.leme.MostraLeme().copy()

  def MostraLemeCom (self):
    """Retorna o leme em rad da embarcação"""
    
    return self.leme.MostraLemeCom().copy()
  
  def MostraPos (self):
    """Retorna a posição da embarcação"""
    
    return self.pos.copy()

  def MostraRotCom (self):
    """Retorna a rotação comandada"""
    
    return self.prop.MostraRotCom().copy()

  def MostraRot (self):
    """Retorna a rotação"""
    
    return self.prop.MostraRot().copy()

  def MostraVelCom (self):
    """Retorna a velocidade comandada"""
    
    return self.uc.copy()
    
  def MudaVelCom (self, uc):
    """Muda a velocidade comandada"""
    
    self.uc  = uc.copy()
    self.prop.MudaVelCom(uc)
    
    pass

  def MudaLemeCom (self, leme):
    """Muda o leme comandado da embarcação
    
    :param leme:
    
    """
    
    temp = leme.copy()
    self.leme.MudaLemeCom(temp)        
    
    pass
    
  def MudaVel (self, velocidade):
    """Muda a velocidade da embarcação
    
    :param velocidade: velocidade (m/s)
    
    """
    
    temp = velocidade.copy()
    
    self.vel = temp        
    self.casco.MudaVel(temp)
    self.leme.MudaVel(temp)
    self.prop.MudaVel(temp)
    
    pass

  def MudaAcel (self, aceleracao):
    """Muda a aceleração da embarcação
    
    Este não influência nos cálculos, é um resultado deles.
        
    :param velocidade: velocidade (m/s)
    
    """  
    self.acel = aceleracao 
         
  def MudaPos (self, posicao):
    """Muda a posição da embarcação 
    
    :param posição: -- posição (m)
    
    """
    temp = posicao.copy()
    self.pos = temp
    self.casco.MudaPos(temp)
    self.leme.MudaPos(temp)
    self.prop.MudaPos(temp)

    
    pass

  def MudaRotCom (self, Rot):
    """Muda a rotação Comandada da embarcação"""
    
    self.prop.MudaRotCom(Rot)
    
    pass

  def CalcFx (self):
    """Calcula a força em Surge"""
    
    if (self.tipo == 'MARAD') or ('MARAD' in self.tipo):
      if self.dic['eta'] == 1:
        saida = self.casco.Fx() + self.prop.Fx(self.MostraVelCom() / self.MostraVel()[0]) +\
                self.leme.Fx(self.MostraRot(),self.MostraVelCom() / self.MostraVel()[0])
      elif self.dic['eta'] == 2:
        saida = self.casco.Fx() + self.prop.Fx(self.MostraVelCom() / self.MostraVel()[0]) +\
                self.leme.Fx(self.MostraRot(),self.MostraRotCom() / self.MostraRot()[0])
                
    elif self.tipo == 'TP':
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx()
    elif self.tipo == '' or self.tipo == None:
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx()
            
    return saida

  def CalcFy (self):
    """Calcula a força em Sway"""

    if (self.tipo == 'MARAD') or ('MARAD' in self.tipo):
      if self.dic['eta'] == 1:
        saida = self.casco.Fy() + self.leme.Fy(self.MostraRot()) +\
          self.prop.Fy(self.MostraVelCom()/self.MostraVel()[0])
      if self.dic['eta'] == 2:
        saida = self.casco.Fy() + self.leme.Fy(self.MostraRot()) +\
          self.prop.Fy(self.MostraRotCom()/self.MostraRot())
    elif self.tipo == 'TP':
      saida = self.casco.Fy() + self.leme.Fy() + self.prop.Fy()
    elif self.tipo == '' or self.tipo == None:
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx()
  
    return saida
  
  def CalcFz (self):
    """Calcula a força no eixo z"""
    
    saida = self.casco.Fz() + self.leme.Fz() + self.prop.Fz()
    
    return saida
    
  def CalcK (self):
    """ Calcula o momento de Roll"""
    
    if (self.tipo == 'MARAD') or ('MARAD' in self.tipo):
      saida = self.casco.K() + self.leme.K(self.MostraRot()) + \
          self.prop.K()
    elif self.tipo == 'TP':
      saida = self.casco.K() + self.leme.K() + self.prop.K()
    elif self.tipo == '' or self.tipo == None:
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx()
  
    return saida
    
  def CalcM (self):
    """Calcula o momento Pitch"""
    
    saida =  self.casco.M() + self.leme.M() + self.prop.M()
    
    return saida
  
  def CalcN (self):
    """Calcula o momento de  Yaw"""

    if (self.tipo == 'MARAD') or ('MARAD' in self.tipo):
      if self.dic['eta'] == 1:
        saida = self.casco.N() + self.leme.N(self.MostraRot()) + self.prop.N(self.MostraVelCom()/self.MostraVel()[0])
      elif self.dic['eta'] == 2:
        saida = self.casco.N() + self.leme.N(self.MostraRot()) + self.prop.N(self.MostraRotCom()/self.MosRotVel())
    elif self.tipo == 'TP':
      saida = self.casco.N() + self.leme.N() + self.prop.N()
    elif self.tipo == '' or self.tipo == None:
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx()
  
    return saida
    
  def VetF (self, p=None):
    r"""Vetor de forças.
    
    Retorna o vetor de forças atuantes na embarcação:
    
    .. math:: 
       
       f (\beta, r, \delta_r) = \left[\begin{array}{c c c c}
       \beta_{x} X(\beta) &r_{x}X(r) &\delta_{R x}X(\delta_R)
       &X_{res} \\
       \beta_{y} Y(\beta) &r_{y}Y(r) &\delta_{R y}Y(\delta_R)
       &Y_{res} \\
       \beta_{n} N(\beta) &r_{n}N(r) &\delta_{R n}N(\delta_R)
       &N_{res}
       \end{array}\right]
       
    :param p: Tupla, onde:
    
              * p[0] (int) -- Termo que determina quantos graus de liberdade
                              possui o modelo matemático;
              * p[1] (tupla) -- Pesos Com os fatores multiplicadores das
                                forças. Tomando :math:`p\left[1\right] = 
                                \left[p_a \ p_b \ p_c \ p_d\right]`,então,
                     
                     .. math::
                     
                        &p_a &= \left[ \beta_x \ \beta_y \ \beta_n \right],\\
                        &p_b &= \left[ r_x \ r_y \ r_n \right],\\
                        &p_c &= \left[ \delta_{Rx} \ \delta_{Ry} \ 
                                \delta_{Rn} \right]
                        &p_d &= \left[ res_{Rx} \ res_{Ry} \ 
                                res_{Rn} \right]
                     
                     Cada fator é um int ou float.
                     Este termo é opcional onde o valor default é uma
                     simulação com um modelo de quatro-4- graus de liberdade 
                     e as forças sem nenhum termo multiplicativo.
    :type p: tuple
    :return: Uma matriz com as forças que atuam na embarcação. 
    :rtype: numpy.ndarray
    
    :Example:
   
        >>> import scipy as sp
        >>> import matplotlib.pyplot as plt
        >>> import Es
        >>> import Navio
        >>> 
        >>> entrada = ('NavioTeste', '../dados/bemformatado.dat',
        ... 'inputtab.dat')
        >>> en = Es.es(entrada)
        >>> nav = Navio.navio(en.lerarqder())
        >>> nav.MudaVelCom(nav.uc)
        >>> nav.MudaVel(sp.array([nav.uc, 0, 0, 0, 0, 0]))
        >>> nav.VetF().reshape(4,1)
        array([[        0.        ],
               [    78315.9850437 ],
               [        0.        ],
               [-14403055.51605981]])
        >>> 
        >>> pa = (1, 1, 1)
        >>> pb = (1, 1, 1)
        >>> pc = (1, 1, 1)
        >>> pd = (1, 1, 1)
        >>> p = (pa, pb, pc, pd)
        >>> gl = 3
        >>> 
        >>> print nav.VetF((gl, p)).reshape(3,1)
        [[        0.        ]
         [    78315.9850437 ]
         [-14403055.51605981]]
    """
    
    if p == None:
      GrausDeLib = 4
      peso = None
    elif len(p) == 1:
      GrausDeLib = p[0]
      peso = None
    elif len(p) == 2:
      GrausDeLib = p[0]
      peso = p[1]
      
    if peso == None:
      if GrausDeLib == 4:
        saida = sp.array([self.CalcFx(), self.CalcFy(),
                self.CalcK(), self.CalcN()])  
      elif GrausDeLib == 3 or GrausDeLib == 6:
        saida = sp.array([self.CalcFx(), self.CalcFy(), self.CalcFz(), self.CalcK(), self.CalcM(), self.CalcN()])        
    else:
      #Arquivando as variáveis do navio, pois será feito modificações
      #posteriores para o cálculo das forças de uma maneira modular
      lemearq = self.MostraLeme()
      velarq = self.MostraVel()
      uc = self.MostraVelCom()
      
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está em equilíbrio somente com velocidade longitudinal u
      self.leme.MudaLemeDir(sp.array(0.))
      self.MudaVelCom(velarq[0]) #condição eta=1
      # setando a velocidade V = [u, 0, 0, 0, 0, 0]
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)
     
      fu = self.VetF((GrausDeLib, )) 
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, v, 0, 0, 0, 0]
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      veltemp[1] = velarq[1]
      self.MudaVel(veltemp)
      # leme = 0 e eta = 1
      fbeta = self.VetF((GrausDeLib, )) - fu
      fbeta2 = fbeta.copy()
      it = 0
      for arg in peso[0]:
        fbeta[it] = arg* fbeta[it]
        it +=1 
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, dotpsi]
      veltemp = sp.zeros((6,))
      veltemp[5] = velarq[5]
      veltemp[0] = velarq[0]            
      self.MudaVel(veltemp)
      # leme = 0 e eta = 1
      fr = self.VetF((GrausDeLib, )) - fu
      fr2 = fr.copy()
      
      it = 0
      for arg in peso[1]:
        fr[it] = arg* fr[it]
        it +=1                
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, 0]  e leme igual ao
      #leme inicial, e eta = 1.
      self.leme.MudaLemeDir(lemearq)
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)      
      fleme = self.VetF((GrausDeLib, ))  - fu
      fleme2 = fleme.copy()
      
      it = 0            
      for arg in peso[2]:
        fleme[it] = arg* fleme[it]
        it +=1     
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, 0],
      #leme = 0, e eta = 1. Agora será feito da força devido as interações e
      #ao resíduo
      self.MudaVel(velarq)
      self.MudaVelCom(uc)
      fbetarl = self.VetF((GrausDeLib, )) - (fbeta2 + fr2 + fleme2)
      it = 0
      for arg in peso[3]:
        fbetarl[it] = arg* fbetarl[it]
        it +=1                            
      del it
      
      saida = fbeta + fr + fleme + fbetarl

    return saida
  
  def coriolis (self, p):
    """Retorna um vetor de 6 graus liberdade com os valores de 'coriolis'"""
    
    m = self.dic['m']*(self.dic['rho']*(self.dic['lpp']**3)/2)
    u = self.MostraVel()[0] 
    v = self.MostraVel()[1]
    p = self.MostraVel()[3]
    r = self.MostraVel()[5]
    xg = self.dic['xg']
    zg = self.dic['zg']
    
    corix = m*(v*r + xg*(r**2) -  zg*p*r)
    coriy = -m*u*r
    corimk = m*zg*u*r
    corimn = -m*xg*u*r 

    if p == None:
      GrausDeLib = 4
      peso = None
    elif len(p) == 1:
      GrausDeLib = p[0]
      peso = None
    elif len(p) == 2:
      GrausDeLib = p[0]
      peso = p[1]
    
    if peso == None:
      saida = sp.array([corix, coriy, [0.], corimk, [0.], corimn])
    else:
      #Arquivando as variáveis do navio, pois será feito modificações
      #posteriores para o cálculo das forças de uma maneira modular
      lemearq = self.MostraLeme()
      velarq = self.MostraVel()
      uc = self.MostraVelCom()
      
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está em equilíbrio somente com velocidade longitudinal u
      self.leme.MudaLemeDir(sp.array(0.))
      self.MudaVelCom(velarq[0]) #condição eta=1
      # setando a velocidade V = [u, 0, 0, 0, 0, 0]
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)
     
      vcori_u = self.coriolis((GrausDeLib, )) 
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, v, 0, 0, 0, 0]
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      veltemp[1] = velarq[1]
      self.MudaVel(veltemp)
      # leme = 0 e eta = 1
      vcori_beta = self.coriolis((GrausDeLib, )) - vcori_u
      vcori_beta2 = vcori_beta.copy()
      it = 0
      for arg in peso[0]:
        vcori_beta[it] = arg * vcori_beta[it]
        it +=1 
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, dotpsi]
      veltemp = sp.zeros((6,))
      veltemp[5] = velarq[5]
      veltemp[0] = velarq[0]            
      self.MudaVel(veltemp)
      # leme = 0 e eta = 1
      vcori_r = self.coriolis((GrausDeLib, )) - vcori_u
      vcori_r2 = vcori_r.copy()
      
      it = 0
      for arg in peso[1]:
        vcori_r2[it] = arg* vcori_r[it]
        it +=1                
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, 0]  e leme igual ao
      #leme inicial, e eta = 1.
      self.leme.MudaLemeDir(lemearq)
      veltemp = sp.zeros((6,))
      veltemp[0] = velarq[0]
      self.MudaVel(veltemp)      
      vcori_l = self.coriolis((GrausDeLib, )) - vcori_u
      vcori_l2 = vcori_l.copy()
      
      it = 0            
      for arg in peso[2]:
        fleme[it] = arg* fleme[it]
        it +=1     
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, 0],
      #leme = 0, e eta = 1. Agora será feito da força devido as interações e
      #ao resíduo
      self.MudaVel(velarq)
      self.MudaVelCom(uc)
      vcori_betarl = self.coriolis((GrausDeLib, )) - (fbeta2 + fr2 + fleme2)
      it = 0
      for arg in peso[3]:
        vcori_betarl[it] = arg * vcori_betarl[it]
        it +=1                            
      del it
      
      saida = vcori_beta + vcori_r + vcori_l + vcori_betarl
          
    return saida

  def H (self, GrausDeLib=4):
    """Matriz de massa menos matriz de massa adicional.
    
    :param GrausDeLib: Graus de liberdade.
    :type GrausDeLib: int
    
    """
    
    H = None
    H = self.casco.Massa(GrausDeLib) - self.casco.Ma(GrausDeLib)
    
    return sp.mat(H)

  def MatRot (self, p=None):
    """Retorna a matriz de rotação de do referencial solidário para o
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
    
    #Matriz de rotação da velocidade linear expressa no eixo solidário para velocidade expressa no eixo inercial.
    Rot = sp.array([[sp.cos(yaw) * sp.cos(pitch),
    # elemento linha 1 coluna 2
    -sp.sin(yaw) * sp.cos(roll) + sp.cos(yaw) * sp.sin(pitch) * sp.sin(roll),
    # elemento linha 1 coluna 3
    sp.sin(yaw) * sp.sin(roll) + sp.cos(yaw) * sp.cos(roll) * sp.sin(pitch)],
    #LINHA 2
    # elemento linha 2 coluna 1
    [sp.sin(yaw) * sp.cos(pitch),
    # elemento linha 2 coluna 2
    sp.cos(yaw) * sp.cos(roll) + sp.sin(roll) * sp.sin(pitch) * sp.sin(yaw),
    # elemento linha 2 coluna 3
    -sp.cos(yaw) * sp.sin(roll) + sp.sin(yaw) * sp.cos(roll) * sp.sin(pitch)],
    #LINHA 3
    # elemento linha 3 coluna 1
    [-sp.sin(pitch),
    # elemento linha 3 coluna 2
    sp.cos(pitch) * sp.sin(roll),
    # elemento linha 3 coluna 3
    sp.cos(pitch) * sp.cos(roll)]])
    
    #Matriz de rotação da velocidade angular expressa no eixo solidário para a derivada dos ângulos de euler expressa no eixo inercial.
    T = sp.array([[sp.array((1.)),
    # elemento linha 1 coluna 2
    sp.sin(roll) * sp.tan(pitch),
    # elemento linha 1 coluna 3
    sp.cos(roll) * sp.tan(pitch)],
    #LINHA 2
    # elemento linha 2 coluna 1
    [sp.array((0.)),
    # elemento linha 2 coluna 2
    sp.cos(roll),
    # elemento linha 2 coluna 3
    -sp.sin(pitch)],
    #LINHA 3
    # elemento linha 3 coluna 1
    [sp.array((0.)),
    # elemento linha 3 coluna 2
    sp.sin(roll) / sp.cos(pitch),
    # elemento linha 3 coluna 3
    sp.cos(roll) / sp.cos(pitch)]])
    
    trans6g = sp.zeros((6,6))
    for argl in sp.arange(3):
      for argc in sp.arange(3):
        trans6g[argl, argc] = Rot[argl, argc]
 
    for argl in sp.arange(3,6):
      for argc in sp.arange(3,6):       
        trans6g[argl, argc] = T[argl - 3, argc - 3]
        
    trans6g= sp.matrix(trans6g)
    
    return trans6g
    
  def f2 (self, VetF, H):
    r"""Calcula o valor de f(x) na equação :math:`\dot x = f(x)` onde x  é 
    o vetor de velocidades no sistema solidário.
    
    :param VetF:
    :param H:
    
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
    
    saida = linalg.solve(a, b) 

    return saida
    
  def f (self, velocidade=None, t=None, p=(4,)):
    """Retorna a aceleração
    
    O p é uma tupla com o valor dos graus de liberdade"""
    
    GrausDeLib = p[0]
    
    if GrausDeLib == 4:
      a = self.H(GrausDeLib)
      b = self.VetF(p) + self.coriolis(p)
      a = sp.array([[a[0,0], a[0,1], a[0,3], a[0,5]], 
      [a[1,0],a[1,1], a[1,3], a[1,5]],
      [a[3,0],a[3,1], a[3,3], a[3,5]],    
      [a[5,0], a[5,1], a[5,3], a[5,5]]])
      b = sp.array((b[0,0],b[1,0], b[3,5], b[5,0]))
      s = linalg.solve(a, b)
      saida = sp.array([[s[0]], [s[1]], [0.], s[2], [0.], [s[3]]])
    elif GrausDeLib == 3:
      a = self.H(GrausDeLib)
      b = self.VetF(p) + self.coriolis(p)
      a = sp.array([[a[0,0], a[0,1], a[0,5]],
      [a[1,0],a[1,1],a[1,5]],
      [a[5,0], a[5,1], a[5,5]]])
      b = sp.array((b[0,0],b[1,0],b[5,0]))
      s = linalg.solve(a, b)
      saida = sp.array([[s[0]], [s[1]], [0.], [0.], [0.], [s[2]]])
        
    return saida
    
  def fvein (self, x, t, p):
    """ Retorna a velocidade do navio no eixo inercial
        
    :param x: sp.array(u, v , w)
    :param t:
    :param p: ((roll, pitch, yaw), (u, v,, w, p, q, r))
    
    """

    vetor = sp.array(p[1])
    saida = sp.array(self.MatRot(p[0]) * vetor)
    return saida
        
    
  def openlogfile(self):
    """Abre arquivos de log
    
    return: Retorma uma tupla com 9 elementos.
    """
    lemehis = open('leme.dat', 'w')#histórico do leme
    lemehis.write('#Navio {nome}\n'.format(nome=self.nome))
    lemehis.write('#Valor do leme em rad\n')
    lemehis.write('#{0:<8}{1:<7}\n'.format('tempo', 'leme'))

    velohis = open('velo.dat', 'w') #histórico da velocidade
    velohis.write('#Navio {nome}\n'.format(nome=self.nome))
    velohis.write('#Velocidade Sistema Solidário  \n#\n')
    velohis.write('#{0:<8}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
    'tempo', 'u', 'v', 'w', 'p', 'q', 'r')) 

    veloinerhis = open('veloiner.dat','w')#histórico da velocidade no
    #sistema inercial. Verificar depois a necessidade
    veloinerhis.write('#Navio {nome}\n'.format(nome=self.nome))
    veloinerhis.write('#Velocidade Inercial\n#\n')
    veloinerhis.write('#{0:<8}{1:<11}{2:<11}{3:<11}\n'.format('tempo','u',
    'v', 'r')) 

    poshis = open('pos.dat', 'w')#histórico da posição
    poshis.write('#Navio {nome}\n'.format(nome=self.nome))
    poshis.write('#Posição e Orientação\n#\n')
    poshis.write('#{0:<8}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
'tempo', 'x', 'y', 'z', 'pitch', 'roll', 'yaw')) 

    fhis = open('forcas.dat', 'w') #histórico de forças
    fhis.write('#Navio {nome}\n'.format(nome=self.nome)) 
    fhis.write('#Forças e Momentos\n#\n')
    fhis.write('#{0:<8}{1:<11}{2:<11}{3:<11}{4:<11}\n'.format('tempo', 'X',
'Y', 'K', 'N')) 

    acelhis = open('acel.dat', 'w') #histórico de acelerações
    acelhis.write('#Navio {nome}\n'.format(nome=self.nome))
    acelhis.write('#Aceleração\n#\n')
    acelhis.write('#{0:<8}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
    'tempo', 'dot u', 'dot v', 'dot w', 'dot pitch', 'dot roll', 'dot yaw')) 

    prophis = open('propulsor.dat', 'w')#histórico Máquina
    prophis.write('#Navio {nome}\n'.format(nome=self.nome))
    prophis.write('#Rotações do propulsor\n#\n')
    prophis.write('#{0:<8}{1:<8}\n'.format('tempo', 'rotações'))

    etahis = open('eta.dat', 'w') #histórico eta
    etahis.write('#Navio {nome}\n'.format(nome=self.nome))
    etahis.write('#eta \n#\n')
    etahis.write('#{0:<8}{1:<8}\n'.format('tempo', 'eta'))

    betahis = open('beta.dat', 'w') #histórico eta
    betahis.write('#Navio {nome}\n'.format(nome=self.nome))
    betahis.write('#Beta \n#\n')
    betahis.write('#{0:<8}{1:<8}\n'.format('tempo', 'beta'))
    
    return (lemehis, velohis, veloinerhis, poshis, fhis, acelhis, prophis,
etahis, betahis)
    
  def getCurvaGiro (self, peso=None, met='rk4', t0=0., dt=0.5, t=100., GrausDeLib=3, tipo='port', leme=sp.array(20.), rotcom=None, vel=None, velcom= None, posin=None, arqs='saida'):
    r"""Simula manobras de Curva de Giro.
    
    :param GrausDeLib: Graus de liberdade de modelo matemático;
    :param met: Método de integração. (default = euler);
    :param t0: Tempo inicial;
    :param dt: Passo no tempo;
    :param t: Tempo final;
    :param leme: Ângulo do leme em graus;
    :param rotcom: Comando de rotação do propulsor[opcional];
    :param vel: Velocidade Inicial da embarcação [opcional];
    :param velcom: Comando de velocidade da embarcação[opcional];
    :param posin: Posição e orientação inicial da embarcação.[opcional];
    :param arqs: Nome do arquivo de saída;
    :return: Simplesmente cria arquivos `txt` no diretório indicado na
             entrada. No diretório terá os seguintes arquivos:
             
             * velohis -- histórico de velocidades;
             * poshis -- histórico de posições;
             * acelhis --- histórico de acelerações;
             * fhis -- histórico de forças;
             * veloinerhis -- histórico de velocidades no sistema inercial;
             * lemehis -- histórico do comando de leme.
    :type GrausDeLib: int
    :type met: str
    :type t0: float;
    :type dt: float;
    :type t: float;
    :type leme: numpy.ndarray;
    :type rotcom: numpy.ndarray
    :type velcom: numpy.ndarray
    :type vel: numpy.ndarray
    :type posin: numpy.ndarray
    :type arqs: str
    :rtype: tuple, file
    
    """
    
    if rotcom == None:
      rotcom = self.dic['rotnom']
    if velcom == None:
      velcom = self.dic['unom']
    if posin == None:
      posin = sp.zeros((6,1)) 
    if vel == None:
      vel = sp.zeros((6,1))
    if peso == None:
      par =   (GrausDeLib, )
    else:
      par = (GrausDeLib, peso)
      
    self.MudaPos(posin)
    self.MudaRotCom(rotcom)
    self.MudaVelCom(velcom)
    vel = self.MostraVel()
    if vel[0] == 0.:
      vel[0] = self.MostraVelCom()
    self.MudaVel(vel)    
    acel = self.f(self.MostraVel(), p=par)
    posini = self.MostraPos().copy()    
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
    velin = self.fvein(self.MostraPos(), 0., (self.MostraPos()[3:], self.MostraVel()))
    
    #Trantando dos arquivos que serão gerados
    if os.path.exists(arqs):
      os.rename(arqs, arqs + '2')
    os.makedirs(arqs)
    os.chdir(arqs)
    (lemehis, velohis, veloinerhis, poshis, fhis, acelhis, prophis, etahis, betahis) = self.openlogfile()
    os.chdir('../..')
    
    #Início da iteração  
    for tp in sp.arange(t0, t, dt): 
      ft = self.VetF(par)
      #Guardando os parâmetros

      #velocidade Inercial
      veloinerhis.write('{0: < 8}'.format(tp))
      for arg in velin:
        veloinerhis.write('{0: < 11.3e}'.format(float(arg)))
      veloinerhis.write('\n')
              
      #histórico Leme
      lemehis.write('{0: < 8}'.format(tp))
      lemehis.write('{0: < 11.3e}'.format(float(self.MostraLeme())))
      lemehis.write('\n')
              
      #histórico da posição
      poshis.write('{0: < 8}'.format(tp))
      for arg in self.MostraPos():
        poshis.write('{0: < 11.3e}'.format(arg[0]))
      poshis.write('\n')
      
      #histórico da Velocidade
      velohis.write('{0: < 8}'.format(tp))
      for arg in self.MostraVel():
        velohis.write('{0: < 11.3e}'.format(arg[0]))
      velohis.write('\n')

      #histórico das Forças 
      fhis.write('{0: < 8}'.format(tp)) 
      for arg in ft:
        fhis.write('{0: < 11.3e}'.format(arg[0]))
      fhis.write('\n')

      #histórico Propulsor
      prophis.write('{0: < 8}'.format(tp))
      prophis.write('{0: < 11.3e}\n'.format(float(self.MostraRot())))

      #histórico eta
      etahis.write('{0: < 8}'.format(tp))
      if self.dic['eta'] == 2:
        etahis.write('{0: < 11.3e}\n'.format(self.MostraRotCom() /
                                        self.MostraRot()))
      elif self.dic['eta'] == 1:
        etahis.write('{0: < 11.3e}\n'.format(float(self.MostraVelCom() /
                                        self.MostraVel()[0])))
                                          
      #histórico Beta
      betahis.write('{0: < 8}'.format(tp))
      betahis.write('{0: < 11.3e}\n'.format(float(sp.arctan(-self.MostraVel()[1] / self.MostraVel()[0]))))  

      #histórico das Acelerações 
      acelhis.write('{0: < 8}'.format(tp))
      for arg in acel:
        acelhis.write('{0: < 11.3e}'.format(arg[0]))
      acelhis.write('\n')
      
      #Passo no tempo para a velocidade no sistema solidário
      if met == 'euler':
        vel = self.integrador.euler(self.f, vel, tp, dt, par)
      elif met =='rk4':
        vel = self.integrador.rk4(self.f, vel, tp, dt, par)

      self.MudaVel(vel)             
      acel = self.f(self.MostraVel(), p=par)
      self.MudaAcel(acel)
      
      #Passo no tempo para a posição
      if met == 'euler':
        pos = self.integrador.euler(self.fvein ,
                      self.MostraPos(), tp, dt ,
                      (self.MostraPos()[3:] ,
                      self.MostraVel()))
      elif met == 'rk4':
        pos = self.integrador.rk4(self.fvein, self.MostraPos(),
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()))
      
      self.MudaPos(pos)
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)
      velin = self.fvein(self.MostraPos(), tp, (self.MostraPos()[3:], self.MostraVel())) 
  
    arq = (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
           etahis)
    for arg in arq:
      arg.close()
    pass

  def getCurvaZigZag (self, peso=None, met='rk4', t0=0., dt=0.5, t=100.,
                      GrausDeLib=3, tipo='port', leme=sp.array(20.),
                      rotcom=None, velcom=None, vel=None, proa=None,
                      posin=None,  arqs='./saida/zz'):
    r"""Simula manobras de Zig Zag.
    
    :param GrausDeLib: Graus de liberdade de modelo matemático;
    :param met: Método de integração. (default = euler);
    :param t0: Tempo inicial;
    :param dt: Passo no tempo;
    :param t: Tempo final;
    :param leme: Ângulo do leme em graus;
    :param proa: Ângulo de ataque em graus para iniciar a mudança de leme.
                 Utilizada na curva de Zig/Zag;
    :param arqs: Nome do arquivo de saída;
    :param rotcom: Comando de rotação do propulsor[opcional];
    :param velcom: Comando de velocidade da embarcação[opcional];
    :param vel: velocidade da embarcação[opcional];
    :return: (Simplesmente cria arquivos `txt` no diretório indicado na
             entrada. No diretório terá os seguintes arquivos:
             * velohis -- histórico de velocidades;
             * poshis -- histórico de posições;
             * acelhis --- histórico de acelerações;
             * fhis -- histórico de forças;
             * veloinerhis -- histórico de velocidades no sistema inercial;
             * lemehis -- histórico do comando de leme.
    :type GrausDeLib: int
    :type met: str
    :type t0: float;
    :type dt: float;
    :type t: float;
    :type leme: numpy.ndarray;
    :type proa: numpy.ndarray
    :type rotcom: numpy.ndarray
    :type velcom: numpy.ndarray
    :type vel: numpy.ndarray
    :type posin: numpy.ndarray
    :type arqs: str
    :rtype: tuple
    
    """

    if rotcom == None:
      rotcom = self.dic['rotnom']
    if velcom == None:
      velcom = self.dic['unom']
    if vel ==  None:
      vel = sp.zeros((6,1))
      vel[0] = self.dic['unom']
    if posin == None:
      posin = sp.zeros((6,1))
    if proa == None:
      proa = sp.array(20.)
    if peso == None:
      par =   (GrausDeLib, )
    else:
      par = (GrausDeLib, peso)
          
    self.MudaPos( posin)
    self.MudaVel(vel)
    self.MudaRotCom(rotcom)
    self.MudaVelCom(velcom)
    acel = self.f(self.MostraVel(), p=par)
    posini = self.MostraPos().copy()  
    #A variável exe é utilizada mais tarde como parâmetro para contar o 
    #número de execuções do leme. Este valor sinalizará o memento em que
    #devemos inverter o valor do leme comandado
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      exe = 0
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      exe = 1
    velin = self.fvein(self.MostraPos(), 0., (self.MostraPos()[3:], self.MostraVel()))
    
    #Trantando dos arquivos que serão gerados
    if os.path.exists(arqs):
      os.rename(arqs, arqs + '2')
    os.makedirs(arqs)
    os.chdir(arqs)
    (lemehis, velohis, veloinerhis, poshis, fhis, acelhis, prophis, etahis, betahis) = self.openlogfile()
    os.chdir('../..')
    
    #Início da iteração
    for tp in sp.arange(t0, t, dt):
    #Verificando o momento em que será realizada a mudança do leme.
    #Quando guinando para  bombordo o valor de exe%2 = True e para boreste o
    #contrario.
      if (((exe%2 == 0) and self.MostraPos()[5] <= -(proa * sp.pi / 180)) or
         (exe%2 != 0 and self.MostraPos()[5] >= (proa * sp.pi / 180))):
           self.MudaLemeCom(self.MostraLeme() * (-1))
           exe +=1

      #Cálculo de forças
      ft = self.VetF(par)
      #Guardando os parâmetros

      #velocidade Inercial
      veloinerhis.write('{0: < 8}'.format(tp))
      for arg in velin:
        veloinerhis.write('{0: < 11.3e}'.format(float(arg)))
      veloinerhis.write('\n')
              
      #histórico Leme
      lemehis.write('{0: < 8}'.format(tp))
      lemehis.write('{0: < 11.3e}'.format(float(self.MostraLeme())))
      lemehis.write('\n')
              
      #histórico da posição
      poshis.write('{0: < 8}'.format(tp))
      for arg in self.MostraPos():
        poshis.write('{0: < 11.3e}'.format(arg[0]))
      poshis.write('\n')
      
      #histórico da Velocidade
      velohis.write('{0: < 8}'.format(tp))
      for arg in self.MostraVel():
        velohis.write('{0: < 11.3e}'.format(arg[0]))
      velohis.write('\n')

      #histórico das Forças 
      fhis.write('{0: < 8}'.format(tp)) 
      for arg in ft:
        fhis.write('{0: < 11.3e}'.format(arg[0]))
      fhis.write('\n')

      #histórico Propulsor
      prophis.write('{0: < 8}'.format(tp))
      prophis.write('{0: < 11.3e}\n'.format(float(self.MostraRot())))

      #histórico eta
      etahis.write('{0: < 8}'.format(tp))
      if self.dic['eta'] == 2:
        etahis.write('{0: < 11.3e}\n'.format(self.MostraRotCom() /
                                        self.MostraRot()))
      elif self.dic['eta'] == 1:
        etahis.write('{0: < 11.3e}\n'.format(float(self.MostraVelCom() /
                                        self.MostraVel()[0])))
                                          
      #histórico Beta
      betahis.write('{0: < 8}'.format(tp))
      betahis.write('{0: < 11.3e}\n'.format(float(sp.arctan(-self.MostraVel()[1] / self.MostraVel()[0]))))  

      #histórico das Acelerações 
      acelhis.write('{0: < 8}'.format(tp))
      for arg in acel:
        acelhis.write('{0: < 11.3e}'.format(arg[0]))
      acelhis.write('\n')
      
      #Passo no tempo para a velocidade no sistema solidário
      if met == 'euler':
        vel = self.integrador.euler(self.f, vel, tp, dt, par)
      elif met =='rk4':
        vel = self.integrador.rk4(self.f, vel, tp, dt, par)

      self.MudaVel(vel)             
      acel = self.f(self.MostraVel(), p=par)
      self.MudaAcel(acel)
      
      #Passo no tempo para a posição
      if met == 'euler':
        pos = self.integrador.euler(self.fvein ,
                      self.MostraPos(), tp, dt ,
                      (self.MostraPos()[3:] ,
                      self.MostraVel()))
      elif met == 'rk4':
        pos = self.integrador.rk4(self.fvein, self.MostraPos(),
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()))
      
      self.MudaPos(pos)
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)
      velin = self.fvein(self.MostraPos(), tp, (self.MostraPos()[3:], self.MostraVel())) 
  
    arq = (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
           etahis)
    for arg in arq:
      arg.close()
    pass


      

  def simulaTestb(self, p, intervalo=sp.array(5.), V=None):
    r"""Gera uma tabela de forças variando com o ângulo :math:`\beta`
    
    :param p: Mesmo parâmetro utilizado para chamar a função :ref: `VetF`;
    :param intervalo: Intervalo de variação do ângulo :math:`\beta`;
    :param V: Velocidade da embarcação.
    :return: Retorna uma matriz com o valor das forças variando de acordo com a
             velocidade.
    :type intervalo: numpy.ndarray
         
    :Example:
        >>> import scipy as sp
        >>> import matplotlib.pyplot as plt
        >>> import Es
        >>> import Navio
        >>> entrada = ('NavioTeste', '../dados/bemformatado.dat',
        ... 'inputtab.dat')
        >>> en = Es.es(entrada)
        >>> nav = Navio.navio(en.lerarqder())
        >>> pa = (1, 1, 1)
        >>> pb = (1, 1, 1)
        >>> pc = (1, 1, 1)
        >>> pd = (1, 1, 1)
        >>> p = (pa, pb, pc, pd)
        >>> print nav.simulaTestb(p)[:2,]
        [[ 0.          0.          0.02576571  0.         -0.01349632]
         [ 0.08726646  0.00765429  0.46717178  0.          0.20968975]]

    """
    
    if V == None:
      V = self.dic['unom']
      
    Velocidade = sp.zeros((6, 1))
    saida = sp.zeros([len( sp.arange(0., sp.pi, intervalo * sp.pi / 180)),
                                     5])
    contlinha = 0   
    for beta in sp.arange(0., sp.pi/2, intervalo * sp.pi / 180):
      Velocidade[0] = sp.array(V) * sp.cos(beta)
      Velocidade[1] = -sp.array(V) * sp.sin(beta)
      self.MudaVelCom(Velocidade[0]) #condição que força \eta=1
      self.MudaVel(Velocidade)
      v = sp.sqrt(Velocidade[0] ** 2 + Velocidade[1] ** 2)
      rho = self.dic['rho']
      lpp = self.dic['lpp']
      vetF = self.VetF((4, p))
      saida[contlinha, :] = sp.hstack([beta, vetF[0] * (2 / 
                      (rho * (lpp * (v ** 2)))), vetF[1] * 
                      (2 / (rho * (lpp* (v ** 2)))), vetF[2] *
                      (2 / (rho * ((lpp * v) ** 2))),
                      vetF[3] * (2 / (rho * ((lpp * v) **
                                             2)))])
      contlinha += 1
    
    return saida

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
