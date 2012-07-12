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
        """Muda a velocidade do casco"""
        
        self.vel = Velocidade.copy()

    def Fx (self):
        r"""Retorna a força em surge
        
        Aqui estão contabilizadas algumas forças relacionadas ao resíduo
        tudo de dimensional.
        
        :return: :math:`X(\beta) + X(r) + X_{res}`
        
        """
        
        u = self.MostraVel()[0] 
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
       
        X = (self.dic['rho'] / 2) * (self.dic['lpp'] ** 4) * \
             (self.dic['xrr'] * r ** 2) + (self.dic['rho'] / 2) * \
             (self.dic['lpp'] ** 3) * (self.dic['xvr'] * v * r)  + \
             (self.dic['rho'] / 2) * (self.dic['lpp'] ** 2) * \
             ((self.dic['xvv']) * v ** 2 )

        return X
    
    def Fy (self):
        """Retorna a força de sway"""
        
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
        

        Y = (self.dic['rho'] / 2) * (self.dic['lpp'] ** 4) * \
            (self.dic['yr|r|'] * r * abs(r)) + (self.dic['rho'] / 2) * \
            (self.dic['lpp'] ** 3) * (self.dic['yr'] * u * r + \
                                      self.dic['yv|r|'] * v * abs(r)) + \
            (self.dic['rho'] / 2) * (self.dic['lpp'] ** 2) * \
            (self.dic['yv'] * v * u + self.dic['yv|v|'] * v * abs(v))
       
        return Y
      
    def K (self):
        """Retorna o momento de roll
        
        O modelo matemático é de 3 graus de liberdade, assim o momento de
        Roll não é calculado. Esta função retorna um array de valor *zero*
        apenas para suprir alguma compatibilidade do programa"""
       
        return sp.array([0.])
    
    def N (self):
        """Retorna o momento de yaw """
        
        u = self.MostraVel()[0]
        v = self.MostraVel()[1]
        r = self.MostraVel()[5]
        
        N = (self.dic['rho'] / 2) * (self.dic['lpp'] ** 5) * \
            (self.dic['nr|r|'] * r * abs(r)) + (self.dic['rho'] / 2) * \
            (self.dic['lpp'] ** 4) * (self.dic['nr'] * u * r + \
                                      self.dic['n|v|r'] * r * abs(v)) + \
            (self.dic['rho'] / 2) * (self.dic['lpp'] ** 3) * \
            (self.dic['nv'] * v * u + self.dic['nv|v|'] * v * abs(v))
        
        return N

if __name__ == "__main__":
    import doctest
    doctest.testmod()                        