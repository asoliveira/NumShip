# -*- coding: utf-8 -*-

import scipy as sp
import numpy  as np

from LemeGen import *

class lemeMarAd(leme):
    """
    """
    def __init__(self,  DicionarioDerivadas):
        """
        """
        leme.__init__(self)
        self.dic = DicionarioDerivadas
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))


    def MudaVel(self,  Velocidade):
        """
        Muda a velocidade do casco
        """
        self.vel = Velocidade.copy()
    
    def MudaLemeDir(self,  leme):
        """
        Utilizar em casos específicos
        """
        self.leme = leme.copy()

    def Fx (self,  Rot= None,  Eta =None):
        """
        Retorna  a força em surge
        """
        u = self.MostraVel()[0] 
        
        if Rot == None:
            Rot = self.dic['rotnom']
        if Eta == None:
            Eta = sp.array([1.])
        
        
        
        if Rot>= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif Rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d*(u**2) + e*u*Rot*self.dic['dp'] + f*(Rot*self.dic['dp'])**2)
        X = ((self.dic['rho']/2)*(self.dic['lpp']*ud)**2)*(self.dic['xdrdr']*(self.MostraLeme()**2) + self.dic['xdrdretaetaeta']*((self.MostraLeme()*Eta)**2))

        return X
    
    def Fy (self,  Rot=None):
        """
        Retorna  a força de sway
        """
        u = self.MostraVel()[0]
        if Rot == None:
            Rot = self.dic['rotnom']


        if Rot>= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif Rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d*(u**2) + e*u*Rot*self.dic['dp'] + f*(Rot*self.dic['dp'])**2)

        Y =  (self.dic['rho']/2)*(self.dic['lpp']**2)*(self.dic['ydr']*(ud**2)*self.MostraLeme())
        
        return Y
      
    def K (self, Rot= None):
        """
        Retorna o momento de roll 
        """
        
    
        return sp.array([0.])
    
    def N (self,  Rot= None):
        """
        Retorna o momento de yaw 
        """
        u = self.MostraVel()[0]
        if Rot == None:
            Rot = self.dic['rotnom']
        
        if Rot>= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif Rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d*(u**2) + e*u*Rot*self.dic['dp'] + f*(Rot*self.dic['dp'])**2)
        N =  (self.dic['rho']/2)*(self.dic['lpp']**3)*(self.dic['ndr']*(ud**2)*self.MostraLeme())
        
        return N

