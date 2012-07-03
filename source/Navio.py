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
  """Classe de navios"""
  
  def __init__ (self, dicvar, nome = 'navioteste', tipo = 'MARAD'):
    """"Construtor do navio
    
    :param dicvar: Dicionário de derivadas hidrodinâmicas e parâmetros
                   necessários para a construção do navio;
    :param nome: Nome do navio. Não possui relevância(default = 'navioteste');
    :param tipo: Tipo de modelo matemático adotado para a construção do navio
                 (default = 'MARAD');
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

  def MostraVel (self):
    """Retorna a Velocidade da embarcação"""
    
    return self.vel
    
  def MostraAcel (self):
    """Retorna a aceleração da embarcação"""
    
    return self.acel
  
  def MostraLeme (self):
    """Retorna o leme em rad da embarcação"""
    
    return self.leme.MostraLeme()

  def MostraLemeCom (self):
    """Retorna o leme em rad da embarcação"""
    
    return self.leme.MostraLemeCom()
  
  def MostraPos (self):
    """Retorna a posição da embarcação"""
    
    return self.pos

  def MostraRotCom (self):
    """Retorna a rotação comandada"""
    
    return self.prop.MostraRotCom()

  def MostraRot (self):
    """Retorna a rotação"""
    
    return self.prop.MostraRot()

  def MostraVelCom (self):
    """Retorna a velocidade comandada"""
    
    return self.uc
    
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
                self.MostraVelCom() / self.MostraVel()[0]) + cori) 
    elif self.tipo == 'TP':
      saida = self.casco.Fx() + self.leme.Fx() + self.prop.Fx() + cori
  
    return saida

  def CalcFy (self):
    """Calcula a força em Sway"""
    
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

  def CalcK (self):
    """ Calcula o momento de Roll"""
    
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
  
    return saida

  
  def CalcN (self):
    """Calcula o momento de  Yaw"""
    
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
      elif GrausDeLib == 3:
        saida = sp.array([self.CalcFx(), self.CalcFy(), self.CalcN()])
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
      
      it = 0
      for arg in peso[0]:
        fbeta[it] = arg* fbeta[it]
        it +=1 
      #Configurando o navio para o cálculo das forças na condição em que a
      #embarcação está com velocidade V = [u, 0, 0, 0, 0, psi]
      veltemp = sp.zeros((6,))
      veltemp[5] = velarq[5]
      veltemp[0] = velarq[0]            
      self.MudaVel(veltemp)
      # leme = 0 e eta = 1
      fr = self.VetF((GrausDeLib, )) - fu
      
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
      fbetarl = self.VetF((GrausDeLib, )) - (fbeta + fr + fleme)
      it = 0
      for arg in peso[3]:
        fbetarl[it] = arg* fbetarl[it]
        it +=1                            
      del it
      
      saida = fbeta + fr + fleme + fbetarl

    return saida

  def H (self, GrausDeLib=4):
    """Matriz de massa menos matriz de massa adicional.
    
    :param GrausDeLib: Graus de liberdade.
    :type GrausDeLib: int
    
    """
    
    H = None
    H = self.casco.M(GrausDeLib) - self.casco.Ma(GrausDeLib)
    
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
      
    Rot = sp.array([[sp.cos(yaw) * sp.cos(pitch), 
                    -sp.sin(yaw) * sp.cos(roll) +
                     sp.cos(yaw) * sp.sin(pitch) * sp.sin(roll), 
                     sp.sin(yaw) * sp.sin(roll) + sp.cos(yaw) * sp.cos(roll)
                    * sp.sin(pitch)], [sp.sin(yaw) * sp.cos(pitch), 
                    sp.cos(yaw) * sp.cos(roll) + sp.sin(roll) * 
                    sp.sin(pitch) * sp.sin(yaw), -sp.cos(yaw) * 
                    sp.sin(roll) + sp.sin(yaw) * sp.cos(roll) *
                    sp.sin(pitch)],                           
    
    
    [-sp.sin(pitch), sp.cos(pitch) * sp.sin(roll), 
    sp.cos(pitch) * sp.cos(roll)]])
    
    Rot.shape  = (3, 3)
    Rot= sp.matrix(Rot)
    
    return Rot

  def f2 (self, VetF, H):
    r"""Calcula o valor de f(x) na equação :math:`\dot x = f(x)` onde x são é 
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
    
    saida = linalg.solve(a, b ) 

    return saida
    
  def f (self, velocidade=None, t=None, p=(4, )):
    """O p é uma tupla com o valor dos graus de liberdade"""
    
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
    
  def fvein (self, x, t, p):
    """
    :param x: sp.array(u, v , w)
    :param t:
    :param p: (  roll, pitch, yaw)
    
    """
    
    return sp.array(self.MatRot(p[0])*p[1])
    
  def getCurvaGiro (self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
                    GrausDeLib=3, tipo='port', leme=sp.array(20.), 
                    rotcom=None, velcom= None, vel=None, eta='vel',
                    posine=None,
                    errotf=sp.array(0.05), errotd=sp.array(0.05),
                    errosr=sp.array(0.001), saida='txt', arqs='saida'):
    r"""Simula manobras de Curva de Giro.
    
    :param GrausDeLib: Graus de liberdade de modelo matemático;
    :param met: Método de integração. (default = euler);
    :param t0: Tempo inicial;
    :param dt: Passo no tempo;
    :param t: Tempo final;
    :param leme: Ângulo do leme em graus;
    :param proa: Ângulo de ataque em graus para iniciar a mudança de leme.
                 Utilizada na curva de Zig/Zag;
    :param osa: Ajuste do erro no ângulo de overshoot para iniciar a mudança
                de leme na curva de ZigZag;
    :param ospath:
    :param errosr:
    :param errotf: Valor mínima da diferença :math:`\pi / 2 - \psi` para
                   considerar o valor `transferência` e o do `avanço`;
    :param errotd: Valor mínima da diferença :math:`\pi - \psi` para 
                   considerar o valor do `diâmetro tático`;
    :param saida: Tipo de arquivo de saída;
    :param arqs: Nome do arquivo de saída;
    :param rotcom: Comando de rotação do propulsor[opcional];
    :param velcom: Comando de velocidade da embarcação[opcional];
    :param vel: Velocidade da embarcação[opcional];
    :return: Uma tupla (velohis, poshis, acelhis, fhis, veloinerhis, lemehis,
             prophis, etahis, dados, betahis)
             Em cada elemento da tupla a primeira coluna é o passo de tempo e
             as demais são as variáveis:
             * velohis -- histórico de velocidades;
             * poshis -- histórico de posições;
             * acelhis --- histórico de acelerações;
             * fhis -- histórico de forças;
             * veloinerhis -- histórico de velocidades no sistema inercial;
             * lemehis -- histórico do comando de leme.
             Ou simplesmente cria arquivos `txt` no diretório indicado na
             entrada com todos este valores
    :type GrausDeLib: int
    :type met: str
    :type t0: float;
    :type dt: float;
    :type t: float;
    :type leme: numpy.ndarray;
    :type proa: numpy.ndarray
    :type osa: numpy.ndarray
    :type ospath: numpy.ndarray
    :type erro: numpy.ndarray
    :type errotf: numpy.ndarray
    :type errotd: numpy.ndarray
    :type arqs: str
    :type rotcom: numpy.ndarray
    :type velcom: numpy.ndarray
    :type vel: numpy.ndarray
    :rtype: tuple, file
    
    """
    
    if rotcom == None:
      rotcom = self.dic['rotnom']
    if velcom == None:
      velcom = self.dic['unom']
    if vel == None:
      vel = sp.zeros((6,1))
      vel[0] = self.dic['unom']
    if posine == None:
      posine = sp.zeros((6,1)) 
    
    self.MudaPos(posine)
    self.MudaVel(vel)
    self.MudaRotCom(rotcom)
    self.MudaVelCom(velcom)

    #log é o parâmetro que indica quando a simulação armazenou os dados do
    #relatório.
    #o valor de r adimensional.
    log = False
    equi = False
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))

    if saida == 'mem':
       #Número de linhas das colunas a serem criadas
      nlin = len(sp.arange(t0, t, dt)) 
      lemehis = sp.zeros((nlin, 2)) #histórico do leme
      velohis = sp.zeros((nlin, 7)) #histórico da velocidade
      veloinerhis = sp.zeros((nlin, 4))#histórico da velocidade no
      poshis =  sp.zeros((nlin, 7)) #histórico da posição no sistema
      #inercial
      fhis     = sp.zeros((nlin, 5)) #histórico de forças
      acelhis = sp.zeros((nlin, 7)) #histórico de acelerações
      prophis = sp.zeros((nlin, 2)) #histórico Máquina
      etahis = sp.zeros((nlin, 2)) #histórico eta
      betahis =  sp.zeros((nlin, 2)) #histórico beta
      del nlin #não preciso mais
    elif saida == 'txt':
      if os.path.exists(arqs):
        os.rename(arqs, arqs + '2')
      os.makedirs(arqs)
      os.chdir(arqs)
      
      lemehis = open('leme.dat', 'w')#historico do leme
      lemehis.write('#Navio ' + self.nome + '\n' +  
            '#Manobra de Curva de Giro\n#\n') 
      lemehis.write('#Valor do leme em rad\n')
      lemehis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' +
            '\n')
      
      velohis = open('velo.dat', 'w') #histórico da velocidade
      velohis.write('#Navio ' + self.nome + '\n' + 
            '#Manobra de Curva de Giro\n#\n')
      velohis.write('#Velocidade Sistema Solidário \n#\n')
      velohis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
                    'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 
                    'dot roll'.rjust(11) + ' ' + 'dot pitch'.rjust(11) +
                    ' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      veloinerhis = open('veloiner.dat', 'w')#histórico da velocidade no
      #sistema inercial. Verificar depois a necessidade
      veloinerhis.write('#Navio ' + self.nome + '\n' +  
                        '#Manobra de Curva de Giro\n#\n')
      veloinerhis.write('#Velocidade Inercial\n#\n')
      veloinerhis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
              'v'.rjust(11) + ' ' + 'r'.rjust(11) + '\n') 

      poshis =  open('pos.dat', 'w')#histórico da posição no sistema
      #inercial
      poshis.write('#Navio ' + self.nome + '\n' +  
                   '#Manobra de Curva de Giro\n#\n')
      poshis.write('#Posição e Orientação\n#\n')
      poshis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
                   'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
                   'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
                   'yaw'.rjust(11)  + ' ' + '\n') 

      fhis     = open('forcas.dat', 'w') #histórico de forças
      fhis.write('#Navio ' + self.nome + '\n' + 
          '#Manobra de Curva de Giro\n#\n')
      fhis.write('#Forças e Momentos\n#\n')
      fhis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
                 'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
                 'N'.rjust(11) + ' ' + '\n') 
      
      acelhis = open('acel.dat', 'w') #histórico de acelerações
      acelhis.write('#Navio ' + self.nome + '\n' +  
                    '#Manobra de Curva de Giro\n#\n')
      acelhis.write('#Aceleração\n#\n')
      acelhis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
                    'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
                    'ddotroll'.rjust(11) + ' ' + 'ddotpitch'.rjust(11)
                    + ' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      prophis = open('propulsor.dat', 'w') #histórico Máquina
      prophis.write('#Navio ' + self.nome + '\n' + 
                    '#Manobra de Curva de Giro\n#\n')
      prophis.write('#Rotações do propulsor\n#\n')
      prophis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      etahis = open('eta.dat', 'w') #histórico eta
      etahis.write('#Navio ' + self.nome + '\n' +  
                   '#Manobra de Curva de Giro\n#\n')
      etahis.write('#eta \n#\n')
      etahis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' + '\n')


      betahis = open('beta.dat', 'w') #histórico eta
      betahis.write('#Navio ' + self.nome + '\n' +  
                    '#Manobra de Curva de Giro\n#\n')
      betahis.write('#Beta \n#\n')
      betahis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' + '\n')
      
      os.chdir('../..')
    
    dados = []
    dic = {}
    posini = self.MostraPos().copy()          
    cont =0 #Contador
    
    #iteração
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
            #Calcula o desvio padrão das últimas 4 velocidades se for abaixo 
            #de 'errosr' armazema o raio de equilíbrio da curva como v/r
          if stats.tstd((V1, V2, V3, V4)) < errosr:
            dic['steadytr'] = (sp.sqrt(self.MostraVel()[0] ** 2 +
                                             self.MostraVel()[1] ** 2) / 
                                     self.MostraVel()[5])
            dados.append(dic.copy())
            log1 = True
          
        if  not log:
          if (abs(abs(self.MostraPos()[5] - posini[5]) - 
              (sp.pi/2)) <= errotf):
            errotf = (abs(abs(self.MostraPos()[5] - posini[5]) - (sp.pi/2)))
            dic['transfer'] = abs(self.MostraPos()[1] - posini[1])
            dic['advance'] = abs(self.MostraPos()[0] - posini[0])
          if (abs(abs(self.MostraPos()[5] - posini[5]) - sp.pi) <= errotd):
            errotd = abs(abs(self.MostraPos()[5] - posini[5]) - sp.pi)
            dic['taticalDiameter'] = abs(self.MostraPos()[1] - posini[1])
          if abs(self.MostraPos()[5] - posini[5]) > sp.pi:
            log = True
      
      if peso == None:
        par =   (GrausDeLib, )
      else:
        par = (GrausDeLib, peso)
      ft = self.VetF(par) 

      MatRot = self.MatRot()
      VelIn = sp.array(MatRot*self.MostraVel()[0:3])
      posine = self.MostraPos()[0:3]
      vel = self.MostraVel()

      #Guardando os parâmetros
      
      #Velocidade Inercial
      if saida == 'txt':
        veloinerhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in VelIn:
          veloinerhis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloinerhis.write('\n')
      elif saida == 'mem':
        d = sp.hstack(VelIn)
        veloinerhis[cont, 1:] = d #
        veloinerhis[cont, 0] = tp #

      #histórico Leme
      if saida == 'txt':
        lemehis.write('%.2f'.rjust(5)%(tp) + ' ')
        lemehis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      elif saida == 'mem':
        lemehis[cont, 0] = tp
        lemehis[cont, 1] = self.MostraLeme()
      
      #histórico da posição
      if saida == 'txt':
        poshis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraPos():
          poshis.write('%.5e'.rjust(11)%(arg) + ' ')
        poshis.write('\n')
      elif saida == 'mem':            
        temp = sp.hstack(self.MostraPos())
        poshis[cont, :] = sp.hstack((tp, temp))
        del temp
      
      #histórico da Velocidade
      if saida == 'txt':
        velohis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vel:
          velohis.write('%.5e'.rjust(11)%(arg) + ' ')
        velohis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(self.MostraVel())
        velohis[cont, :] = sp.hstack((tp, temp))
        del temp
        
      #histórico das Forças 
      if saida == 'txt':
        temp = sp.zeros((4, 1))
        if GrausDeLib == 4:
          temp = ft
        elif GrausDeLib == 3:
          temp[:2]  = ft[:2]
          temp[3]  = ft[2]
        fhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in temp:
          fhis.write('%.5e'.rjust(11)%(arg) + ' ')
        fhis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(sp.array(ft))
        if GrausDeLib == 4:
          fhis[cont, :] = sp.hstack((tp, temp))
        elif GrausDeLib == 3:
          fhis[cont, :3] = sp.hstack((tp, temp[:2]))
          fhis[cont, 4] = temp[2]
      del temp

      #histórico Propulsor
      if saida == 'txt':
        prophis.write('%.2f'.rjust(5)%(tp) + ' ')
        prophis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      elif saida == 'mem':
        prophis[cont, :] = sp.hstack((tp, self.MostraRot()))
        
      #histórico eta
      if saida == 'txt':
        etahis.write('%.2f'.rjust(5)%(tp) + ' ')
        if eta == 'rot':
          etahis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                                          self.MostraRot()) + '\n')
        elif eta == 'vel':
          etahis.write('%.2f'.rjust(5) % (self.MostraVelCom() /
                                          self.MostraVel()[0]) + '\n')
      elif saida == 'mem':
        if eta == 'rot':
          etahis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
                                       self.MostraRot()))
        elif eta == 'vel':
          etahis[cont, :] = sp.hstack((tp, self.MostraVelCom() /
                                       self.MostraVel()[0]))

      #histórico Beta
      if saida == 'txt':
        betahis.write('%.2f'.rjust(5) % (tp) + ' ')
        betahis.write(('%.2f'.rjust(5) % sp.arctan(-self.MostraVel()[1] /
                       self.MostraVel()[0])) + '\n')  
      elif saida == 'mem':
        betahis[cont, :] = sp.hstack((tp, sp.arctan(-self.MostraVel()[1] / 
                                      self.MostraVel()[0])))

      #histórico das Acelerações 
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
        acelhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vetor:
          acelhis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        acelhis.write('\n')
      elif saida == 'mem':  
        acelhis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       
      #Criação do vetor de graus de liberdade
      if GrausDeLib == 4:
        vt = sp.zeros((6, 1))
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[3]
        vt [3] = self.MostraVel()[5]
        vt [4] = self.MostraPos()[3]
        vt [5] = self.MostraPos()[5]
      elif  GrausDeLib == 3:
        vt = sp.zeros((4, 1))
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[5]
        vt [3] = self.MostraPos()[5]         
      #integração da aceleração solidária
      if met == 'euler':
        vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      elif met =='rk4':
        vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
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
      #integração da velocidade inercial
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
      arq = (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
             etahis)
      for arg in arq:
        arg.close()
      return dados
    elif saida == 'mem':
      return (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
              etahis, betahis, dados)

  def getCurvaZigZag (self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
                      GrausDeLib=3, tipo='port', leme=sp.array(20.),
                      rotcom=None, velcom=None, vel=None, proa=None,
                      eta='vel', posine=None, osa=sp.array(0.0),
                      ospath=sp.array(0.0), erro=sp.array(0.005),
                      saida='txt', arqs='./saida/zz'):
    r"""Simula manobras de Zig Zag.
    
    :param GrausDeLib: Graus de liberdade de modelo matemático;
    :param met: Método de integração. (default = euler);
    :param t0: Tempo inicial;
    :param dt: Passo no tempo;
    :param t: Tempo final;
    :param leme: Ângulo do leme em graus;
    :param proa: Ângulo de ataque em graus para iniciar a mudança de leme.
                 Utilizada na curva de Zig/Zag;
    :param osa: Ajuste do erro no ângulo de overshoot para iniciar a mudança
                de leme na curva de ZigZag;
    :param ospath:
    :param errosr:
    :param errotf:
    :param errotd:
    :param saida: Tipo de arquivo de saída;
    :param arqs: Nome do arquivo de saída;
    :param rotcom: Comando de rotação do propulsor[opcional];
    :param velcom: Comando de velocidade da embarcação[opcional];
    :param vel: velocidade da embarcação[opcional];
    :return: (velohis, poshis, acelhis, fhis, veloinerhis, lemehis,
             prophis, etahis). Caso o valor do parâmetro *saida* seja 'txt' 
             retorna estes valores como arquivos de texto no diretório 
             indicado pelo parâmetro *arqs*. Mesmo nesse caso a função
             retorna uma lista que contém dicionários com parâmetros com
             overshoot da proa *'osa'* e overshoot lateral linear *'ospath'*.
             Em cada elemento da tupla a primeira coluna é o passo de tempo e
             as demais são as variáveis:
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
    :type osa: numpy.ndarray
    :type ospath: numpy.ndarray
    :type erro: numpy.ndarray
    :type errotf: numpy.ndarray
    :type errotd: numpy.ndarray
    :type arqs: str
    :type rotcom: numpy.ndarray
    :type velcom: numpy.ndarray
    :type vel: numpy.ndarray
    :rtype: tuple
    
    """

    if rotcom == None:
      rotcom = self.dic['rotnom']
    if velcom == None:
      velcom = self.dic['unom']
    if vel ==  None:
      vel = sp.zeros((6,1))
      vel[0] = self.dic['unom']
    if posine == None:
      posine = sp.zeros((6,1))
    if proa == None:
      proa = sp.array(20.)
    
    self.MudaPos( posine)
    self.MudaVel(vel)
    self.MudaRotCom(rotcom)
    self.MudaVelCom(velcom)

    #A variável exe é utilizada mais tarde como parâmetro para contar o 
    #número de execuções do leme. Este valo sinalizará o memento em que
    #devemos inverter o valor do leme comandado
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
      exe = 0
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))
      exe = 1

    #Criando espaço na memória para armazenar os parâmetros da curva

    if saida == 'mem':
      nlin = len(sp.arange(t0, t, dt)) 
      lemehis = sp.zeros((nlin, 2)) #histórico do leme
      velohis = sp.zeros((nlin, 7)) #histórico da velocidade
      veloinerhis = sp.zeros((nlin, 4))#histórico da velocidade no
      #sistema inercial Verificar depois a necessidade
      poshis =  sp.zeros([nlin, 7]) #histórico da posição no sistema inercial
      fhis     = sp.zeros((nlin, 5)) #histórico de forças
      acelhis = sp.zeros((nlin, 7)) #histórico de acelerações
      prophis = sp.zeros((nlin, 2)) #histórico Máquina
      etahis = sp.zeros((nlin, 2)) #histórico eta
      del nlin #não preciso mais
    elif saida == 'txt':
      if os.path.exists(arqs):
        os.rename(arqs, arqs + '2')        
      os.makedirs(arqs)
      os.chdir(arqs)
      
      lemehis = open('leme.dat', 'w')#histórico do leme
      lemehis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
                    de Zig-Zag\n#\n')
      lemehis.write('#Valor do leme em rad\n')
      lemehis.write('#temp'.center(5) + ' ' + 'leme'.rjust(8) + ' ' + '\n')
      
      velohis = open('velo.dat', 'w') #histórico da velocidade
      velohis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
                    de Zig-Zag\n#\n')
      velohis.write('#velocidade no Sistema Solidário \n#\n')
      velohis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
                    'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' + 'dot \
                    roll'.rjust(11) + ' ' + ' dot pitch'.rjust(11)  + 
                    ' ' + 'dot yaw'.rjust(11) + ' ' + '\n') 
      
      #histórico da velocidade no sistema inercial Verificar depois a
      #necessidade.
      veloinerhis = open('veloiner.dat', 'w')
      veloinerhis.write('#Navio ' + self.nome + '\n' +  '#Manobra de \
                        Curva de Zig-Zag\n#\n')
      veloinerhis.write('#velocidade Inercial\n#\n')
      veloinerhis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
                        'v'.rjust(11)  + ' '  + 'r'.rjust(11) + '\n') 

      #histórico da posição no sistema inercial
      poshis =  open('pos.dat', 'w')
      poshis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
                   de Zig-Zag\n#\n')
      poshis.write('#Posição e Orientação\n#\n')
      poshis.write('#temp'.center(5) + ' ' + 'x'.rjust(11)  + ' ' +
                   'y'.rjust(11)  + ' ' + 'z'.rjust(11)  + ' ' +
                   'roll'.rjust(11) + ' ' + 'pitch'.rjust(11)  + ' ' +
                   'yaw'.rjust(11) + ' ' + '\n') 

      #histórico de forças
      fhis = open('forcas.dat', 'w') 
      fhis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva de \
                  Zig-Zag\n#\n')
      fhis.write('#Forças e Momentos\n#\n')
      fhis.write('#temp'.center(5) + ' ' + 'X'.rjust(11)  + ' ' +
                 'Y'.rjust(11)  + ' ' + 'K'.rjust(11)  + ' ' +
                 'N'.rjust(11) + ' ' + '\n') 
      
      #histórico de acelerações
      acelhis = open('acel.dat', 'w') 
      acelhis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
                    de Zig-Zag\n#\n')
      acelhis.write('#Aceleração\n#\n')
      acelhis.write('#temp'.center(5) + ' ' + 'u'.rjust(11)  + ' ' +
                    'v'.rjust(11)  + ' ' + 'w'.rjust(11)  + ' ' +
                    'ddotroll'.rjust(11) + ' ' + ' ddotpitch'.rjust(11)
                    + ' ' + 'ddotyaw'.rjust(11)  + ' ' + '\n') 

      #histórico Máquina
      prophis = open('propulsor.dat', 'w') 
      prophis.write('#Navio ' + self.nome + '\n' + '#Manobra de Curva \
                    de Zig-Zag\n#\n')
      prophis.write('#Rotações do propulsor\n#\n')
      prophis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + '\n')
      
      #histórico eta
      etahis = open('eta.dat', 'w') 
      etahis.write('#Navio ' + self.nome + '\n' +  '#Manobra de Curva \
            de Zig-Zag\n#\n')
      etahis.write('#eta \n#\n')
      etahis.write('#temp'.center(5) + ' ' + 'rot'.rjust(8) + ' ' +  '\n')
      #Voltando ao diretório de trabalho
      os.chdir('../..')
    dados = []
    dic = {}
    posini = self.MostraPos().copy()          
    cont = 0 #Contador
   
    if peso == None:
      par =   (GrausDeLib, )
    else:
      par = (GrausDeLib, peso)
    
    #Início da iteração
    for tp in sp.arange(t0, t, dt):
    #Verificando o momento em que será realizada a mudança do leme.
    #Quando guinando para  bombordo o valor de exe%2 = True e para boreste o
    #contrario.
      if (((exe%2 == 0) and self.MostraPos()[5] <= -(proa * sp.pi / 180)) or
         (exe%2 != 0 and self.MostraPos()[5] >= (proa * sp.pi / 180))):
          self.MudaLemeCom(self.MostraLeme() * (-1))
          if ((exe != 0 and tipo == 'port') or 
              (exe != 1 and tipo == 'starboard')):
            dic['reach'] = erro
            dic['ospath'] = ospath
            dic['osangle'] = osa
            dados.append(dic.copy())
          osa = sp.array(0.0)
          ospath = sp.array(0)
          erro = sp.array(0.05)
          logospath = False
          logosa = False
          if tipo == 'port':
            dic['exeNumber'] = exe
          elif tipo =='starboard':
            dic['exeNumber'] = exe - 1
          dic['time'] = tp - sp.array(dt)
          dic['path'] = self.MostraPos()[1]
          dic['proa'] = self.MostraPos()[5]
          exe += 1
      #Atualizando os parâmetros.
      #Este if pergunta se está é a primeira execução
      if ((exe != 0 and tipo == 'port') or 
          (exe != 1 and tipo == 'starboard')):
        #Já atingi o maior valor de overshoot da distancia e armazenei este
        #valor?
        if ((logospath == False) and
            (abs(self.MostraPos()[1] - dic['path']) >= ospath)):
          ospath = abs(self.MostraPos()[1] - dic['path'])
        else:
          logospath = True
        #Já atingi o maior valor de overshoot do proamento e armazenei este
        #valor?
        if ((logosa == False) and (abs(self.MostraPos()[5] - 
          dic['proa']) >= osa)):
          osa = abs(self.MostraPos()[5] - dic['proa'])
        else:
          logosa = True
          
        if abs(abs(self.MostraPos()[5]) - abs(posini[5])) < erro:
          erro = abs(self.MostraPos()[5] - posini[5])
          
      MatRot = self.MatRot()
      velin = MatRot * sp.matrix(self.vel[0:3])
      posine = self.MostraPos()[0:3]
      #Cálculo de forças
      ft = self.VetF(par)            
      #Guardando os parâmetros.
      #velocidade Inercial
      if saida == 'txt':
        veloinerhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in velin:
          veloinerhis.write('%.5e'.rjust(11)%(arg) + ' ')
        veloinerhis.write('\n')
      elif saida == 'mem':
        d = sp.hstack(velin)
        veloinerhis[cont, 1:] = d 
        veloinerhis[cont, 0] = tp 
      #Guardando o histórico do Leme
      if saida == 'txt':
        lemehis.write('%.2f'.rjust(5)%(tp) + ' ')
        lemehis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      elif saida == 'mem':
        lemehis[cont, 0] = tp
        lemehis[cont, 1] = self.MostraLeme()
      #histórico da posição
      if saida == 'txt':
        poshis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraPos():
          poshis.write('%.5e'.rjust(11)%(arg) + ' ')
        poshis.write('\n')
      elif saida == 'mem':            
        temp = sp.hstack(self.MostraPos())
        poshis[cont, :] = sp.hstack((tp, temp))
        del temp
      #histórico da velocidade
      if saida == 'txt':
        velohis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraVel():
          velohis.write('%.5e'.rjust(11)%(arg) + ' ')
        velohis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(self.MostraVel())
        velohis[cont, :] = sp.hstack((tp, temp))
        del temp
      #histórico das Forças 
      if saida == 'txt':
        temp = sp.zeros((4, 1))
        if GrausDeLib == 4:
          temp = ft
        elif GrausDeLib == 3:
          temp[:2] = ft[:2]
          temp[3] = ft[2]
        fhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in temp:
          fhis.write('%.5e'.rjust(11)%(arg) + ' ')
        fhis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(sp.array(ft))
        if GrausDeLib == 4:
          fhis[cont, :] = sp.hstack((tp, temp))
        elif GrausDeLib == 3:
          fhis[cont, :3] = sp.hstack((tp, temp[:2]))
          fhis[cont, 4] = temp[2]

      #histórico Propulsor
      if saida == 'txt':
        prophis.write('%.2f'.rjust(5)%(tp) + ' ')
        prophis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      elif saida == 'mem':
        prophis[cont, :] = sp.hstack((tp, self.MostraRot()))
      
      #histórico eta
      if saida == 'txt':
        etahis.write('%.2f'.rjust(5)%(tp) + ' ')
        if eta == 'rot':
          etahis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                self.MostraRot()) + '\n')
        elif eta == 'vel':   
          etahis.write('%.2f'.rjust(5) % (self.MostraVelCom() /
                self.MostraVel()[0]) + '\n')
      elif saida == 'mem':
        if eta== 'rot':
          etahis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
                        self.MostraRot()))
        elif eta == 'vel':
          etahis[cont, :] = sp.hstack((tp, self.MostraVelCom() /
                        self.MostraVel()[0]))

      #histórico das Acelerações 
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
        acelhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vetor:
          acelhis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        acelhis.write('\n')
      elif saida == 'mem':  
        acelhis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       
      del vetor 

      #Criação de vetor de graus de liberdade
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
        
      #Integração da Aceleração solidária
      if met == 'euler':
        vt =  self.integrador.euler(self.f, vt, tp, dt ,par  )
      elif met =='rk4':
        vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      #Preparando a saída da integração
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

      #Integração da velocidade inercial
      x = sp.zeros((6, 1))
      if met == 'euler':
        x[:3] = self.integrador.euler(self.fvein, self.MostraPos()[:3],
                                      tp, dt, (self.MostraPos()[3:],
                                      self.MostraVel()[:3]))
      elif met == 'rk4':
        x[:3] = self.integrador.rk4(self.fvein, self.MostraPos()[:3],
                                    tp, dt, (self.MostraPos()[3:],
                                    self.MostraVel()[:3]))
      #Preparando a saída da integração
      if GrausDeLib == 4:
        x[3] = vt[4]
        x[5] = vt[5]
      elif GrausDeLib == 3:
        x[5] = vt[3]
      
      #Preparando os parâmetros para o próximo passo de integração
      self.MudaPos(x)
      cont += 1
      del x
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)

    if saida == 'txt':
      arq = (velohis, poshis, acelhis, fhis, veloinerhis, lemehis,
             prophis, etahis)
      for arg in arq:
        arg.close()
      return dados
    elif saida == 'mem':
      return (velohis, poshis, acelhis, fhis, veloinerhis, lemehis,
              prophis, etahis, dados)

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