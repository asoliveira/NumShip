# -*- coding: utf-8 -*-

import scipy as sp
import numpy  as np

from LemeGen import *

class lemeTris(leme):
    """
    Subclasse de leme seguindo o modelo do Paper de TrstanPerez

    """
    tipo = 'Modelo paper Tristan'
    data = '10-10-2010'
    autor = 'Alex'
  
    def __init__(self, DicionarioDerivadas):
        """"
        Construtor do leme
        __________________________
        Variáveis de entrada:
        
        DicionarioDerivadas (string)-- Dicionário com os coeficientes do casco e outros dados
        ___________________________
        Obs:
        para o DicionarioDerivadas deve se utilizar a classe entrada e a função lerarqder

        """
        
        leme.__init__(self)
        self.dic = DicionarioDerivadas
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        

    def MostraCoef(self,  Chave):
        """
        """
        return self.dic[Chave]
        
    
    
    def MudaVel(self,  Velocidade):
        """
        Muda a velocidade da embarcação
        __________________________
        Variáveis de entrada:
        
        Velocidade -- array de velocidades
        """
        
        vel =  Velocidade.copy()

        self.V = sp.sqrt(vel[0]**2+ vel[1]**2)

        vel[0] = vel[0] -  self.dic['unom']
        vel [:3]= vel[:3]/self.V
        vel[3:]= vel[3:]*self.dic['lpp']/self.V 
        self.vel = vel
        
    def MudaPos(self,  Posicao):
        """
        Muda a posição e orientação do casco
        __________________________
        Variáveis de entrada:
        Posicao -- Posição 
        """
        pos = Posicao.copy()
        pos[:3] = pos[:3]/self.dic['lpp']
        self.pos = pos
  
    def Fx (self):
        """
        Forcas em surge
        """
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        #ua = (u - self.dic['unom'])/u
    
        X = self.dic ['xd']*self.MostraLeme() + self.dic ['xdd']*self.MostraLeme()**2 + self.dic ['xdu']*self.MostraLeme()*ua + self.dic ['xddu']*ua*self.MostraLeme()**2 + self.dic ['xvd']*v*self.MostraLeme() + self.dic ['xvdd']*v*self.MostraLeme()**2
        
        return X*((self.dic['rho']*(self.V*self.dic['lpp'])**2)/2)
    
    def Fy (self):
        """
        Forcas de sway
        """
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        
        Y = self.dic ['yd']*self.MostraLeme() + self.dic ['ydd']*self.MostraLeme()**2 + self.dic ['yddd']*self.MostraLeme()**3 + self.dic ['ydv']*self.MostraLeme()*v + self.dic ['ydvv']*self.MostraLeme()*(v**2) + self.dic ['ydu']*self.MostraLeme()*ua + self.dic ['yddu']*ua*(self.MostraLeme()**2) + self.dic['ydddu']*ua*(self.MostraLeme()**3)
        
        return Y*((self.dic['rho']*(self.V*self.dic['lpp'])**2)/2)
      
    def K (self):
        """
        Momento de roll 
        """
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        P = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]  
    
        #ua = (u - self.dic['unom'])/u
    
        K = self.dic ['kd']*self.MostraLeme() + self.dic ['kdd']*self.MostraLeme()**2 + self.dic ['kddd']*self.MostraLeme()**3 + self.dic ['kdv']*self.MostraLeme()*v + self.dic ['kdvv']*self.MostraLeme()*v**2 + self.dic ['kdu']*self.MostraLeme()*ua + self.dic ['kddu']*ua*self.MostraLeme()**2 + self.dic['kdddu']*ua*self.MostraLeme()**3
    
        return K*(self.dic['rho']*(self.V**2)*(self.dic['lpp']**3)/2)
    
    def N (self):
        """
        Momento de yaw 
        """
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]  
    
     
        #ua = (u - self.dic['unom'])/u
    
        N = self.dic ['nd']*self.MostraLeme() + self.dic ['ndd']*self.MostraLeme()**2 + self.dic ['nddd']*self.MostraLeme()**3 + self.dic ['ndv']*self.MostraLeme()*v + self.dic ['ndvv']*self.MostraLeme()*v**2 + self.dic ['ndu']*self.MostraLeme()*ua + self.dic ['nddu']*ua*self.MostraLeme()**2 + self.dic['ndddu']*ua*self.MostraLeme()**3
        
        return N*(self.dic['rho']*(self.V**2)*(self.dic['lpp']**3)/2)
    
