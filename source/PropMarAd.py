# - * - coding: utf-8 - * -

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

from PropGen import  * 

class propMarAd(prop):
    
    def __init__(self,  DicionarioDerivadas):
        """Construtor do casco"""
        
        self.dic = DicionarioDerivadas
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        self.Rot =  sp.array(self.dic['rotnom'])
        self.RotCom =  sp.array(self.dic['rotnom'])
        self.uc = self.dic['unom']
       

    def MudaRotCom (self, Rot):
        """Muda a rotação comandada"""        
        
        self.RotCom = Rot.copy()
        
    def MudaVelCom (self, uc):
        """Muda a velocidade comandada""" 
        
        self.uc = uc.copy()
    
    def MudaRot (self, dt):
      """Muda a rotação do propulsor"""
      
      self.Rot = self.RotCom.copy()
        
    def MostraRot(self):
        """Retorna a rotação da máquina atual"""
        
        return self.Rot
        
    def MostraRotCom (self):
        """Retorna a rotação comandada"""
        
        return self.RotCom
        
    def MostraVelCom (self):
        """Retorna a velocidade comandada"""
        
        return self.uc         
        
    def Fx (self):
        """Retorna a força em surge"""
        
        Eta = self.MostraVelCom() / self.MostraVel()[0]
       
        if  Eta < sp.array(0.):
            a =  self.dic['a4']
            b =  self.dic['b4']
            c =  self.dic['c4']
        elif sp.array(0.) <= Eta and Eta < sp.array(1.):
            a =  self.dic['a3']
            b =  self.dic['b3']
            c =  self.dic['c3']
        elif sp.array(1) <= Eta and Eta < sp.array(2):
            a =  self.dic['a2']
            b =  self.dic['b2']
            c =  self.dic['c2']  
        elif sp.array(2) <= Eta :
            a =  self.dic['a1']
            b =  self.dic['b1']
            c =  self.dic['c1'] 
        
        u = self.MostraVel()[0] 
        v = self.MostraVel()[1]
        r  = self.MostraVel()[5]
        X = (self.dic['rho'] * (self.dic['lpp'] ** 2) / 2) * (u ** 2) * (a +
             b * Eta + c * (Eta ** 2)) + (self.dic['rho'] * \
             (self.dic['lpp'] ** 2) / 2) * self.dic['xvveta'] * (v ** 2) * \
             (Eta - 1)
        
        return X
        
    def Fy (self):
        """Retorna a força em sway"""

        Eta = self.MostraVelCom() / self.MostraVel()[0]
        
        if self.MostraRot()< sp.array(0.):
            d = self.dic['d*0']
            e = self.dic['e*0']
            f = self.dic['f*0']
        elif self.MostraRot() >= sp.array(0.):
            d = self.dic['d*1']
            e = self.dic['e*1']
            f = self.dic['f*1']
        
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r  = self.MostraVel()[5]
       
        uz = sp.sqrt(d * (u ** 2) + e * u * self.MostraRot() * 
            self.dic['dp'] + f * ((self.MostraRot() * self.dic['dp']) ** 2))

        
        Y = (self.dic['rho'] * (self.dic['lpp'] ** 3)/2) * \
            self.dic['yreta'] * u * r * (Eta-1) + (self.dic['rho'] * \
            (self.dic['lpp'] ** 2) / 2) * self.dic['yveta'] * u * v * \
            (Eta - 1) + (self.dic['rho'] * (self.dic['lpp'] ** 2) / 2) * \
            self.dic['y*'] * (uz ** 2)
            
        return Y

    def N (self):
        """Retorna o momento de yaw """

        Eta = self.MostraVelCom() / self.MostraVel()[0]
        
        if self.MostraRot()< sp.array(0.):
            d = self.dic['d*0']
            e = self.dic['e*0']
            f = self.dic['f*0']
        elif self.MostraRot() >= sp.array(0.):
            d = self.dic['d*1']
            e = self.dic['e*1']
            f = self.dic['f*1']
        
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r  = self.MostraVel()[5]
        
        uz = sp.sqrt(d * (u ** 2) + e * u * self.MostraRot() * 
             self.dic['dp'] + f * ((self.MostraRot() * self.dic['dp']) ** 2))

        N = (self.dic['rho'] * (self.dic['lpp'] ** 4)/2) * \
             self.dic['nreta'] * u * r * (Eta-1) + (self.dic['rho'] * \
             (self.dic['lpp'] ** 3)/2) * self.dic['nveta'] * u * v * \
             (Eta-1) + (self.dic['rho'] * (self.dic['lpp'] ** 3)/2) * \
             self.dic['n*'] * (uz ** 2)
             
        return N      

if __name__ == "__main__":
    import doctest
    doctest.testmod()         