# -*- coding: utf-8 -*-
import scipy as sp

from Casco import *


class cascoMarAd(casco):
    """
    """
    def __init__(self,  DicionarioDerivada ):
        """
        """
    
        casco.__init__(self)
        self.dic = DicionarioDerivada   
    def MudaVel(self,  Velocidade):
        """
        Muda a velocidade do casco
        """
        self.vel = Velocidade.copy()

    def Fx (self):
        """
        Retorna a força em surge
        """
        u = self.MostraVel()[0] 
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
        

        X = (self.dic['rho']/2)*(self.dic['lpp']**4)*(self.dic['xrr']*r**2) + (self.dic['rho']/2)*(self.dic['lpp']**3)*(self.dic['xvr']*v*r)  +  (self.dic['rho']/2)*(self.dic['lpp']**2)*((self.dic['xvv'])*v**2 )

        return X
    
    def Fy (self):
        """
        Retorna a força de sway
        """
        
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
        

        Y = (self.dic['rho']/2)*(self.dic['lpp']**4)*(self.dic['yr|r|']*r*abs(r)) + (self.dic['rho']/2)*(self.dic['lpp']**3)*(self.dic['yr']*u*r+ self.dic['yv|r|']*v*abs(r))  +  (self.dic['rho']/2)*(self.dic['lpp']**2)*(self.dic['yv']*v*u + self.dic['yv|v|']*v*abs(v) )
        
        
        return Y
      
    def K (self):
        """
        Retorna o momento de roll 
        """
        
    
        return sp.array([0.])
    
    def N (self):
        """
        Retorna o momento de yaw 
        """
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
        

        N = (self.dic['rho']/2)*(self.dic['lpp']**5)*(self.dic['nr|r|']*r*abs(r)) + (self.dic['rho']/2)*(self.dic['lpp']**4)*(self.dic['nr']*u*r+ self.dic['n|v|r']*r*abs(v))  +  (self.dic['rho']/2)*(self.dic['lpp']**3)*(self.dic['nv']*v*u + self.dic['nv|v|']*v*abs(v) )
        
        return N
