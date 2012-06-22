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


import scipy as sp
import numpy  as np

from LemeGen import * 

class lemeMarAd(leme):
    """Classe com o modelo matemático de leme do MARAD"""
    
    def __init__(self,  DicionarioDerivadas):
        """
        :param DicionarioDerivadas: Dicionário contendo as variáveis para a
                                    implementação da classe.
        
        """
        
        leme.__init__(self)
        self.dic = DicionarioDerivadas
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))


    def MudaVel(self,  velocidade):
        """Muda a velocidade do casco
        
        :param velocidade: Novo valor da velocidade.
        :type velocidade: numpy.ndarray
        
        """
        
        self.vel = velocidade.copy()
    
    def MudaLemeDir(self,  leme):
        """Muda o leme de maneira instantânea
        
        Utilizar em casos específicos, isto não acontece na realidade
        
        :param leme: Novo valor do leme.
        :type leme: numpy.ndarray
        
        """
        self.leme = leme.copy()

    def Fx (self,  rot= None,  eta =None):
        """Retorna  a força em surge.
        
        :param rot: rotação do propulsor da embarcação;
        :param eta: Valor :math:`\eta`
        :type rot: numpy.ndarray
        :type eta: numpy.ndarray
        
        """
        u = self.MostraVel()[0] 
        
        if rot == None:
            rot = self.dic['rotnom']
        if eta == None:
            eta = sp.array([1.])

        if rot >= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d * (u ** 2) + e * u * rot * self.dic['dp'] + f * \
                    (rot * self.dic['dp']) ** 2)
                    
        X = ((self.dic['rho'] / 2) * (self.dic['lpp'] * ud) ** 2) * \
             (self.dic['xdrdr'] * (self. MostraLeme() ** 2) + \
             self.dic['xdrdretaetaeta'] * ((self.MostraLeme() * eta) ** \
             2))

        return X
    
    def Fy (self,  rot=None):
        """Retorna  a força em sway.
        
        :param rot: rotação do propulsor da embarcação;
        :type rot: numpy.ndarray
        
        """
        u = self.MostraVel()[0]
        if rot == None:
            rot = self.dic['rotnom']

        if rot>= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d * (u ** 2) + e * u * rot * self.dic['dp'] + \
                     f * (rot * self.dic['dp']) ** 2)

        Y = (self.dic['rho'] / 2) * (self.dic['lpp'] ** 2) * \
            (self.dic['ydr'] * (ud ** 2) * self.MostraLeme())
        
        return Y
      
    def K (self, rot=None):
        """Retorna  o momento de  roll
        
        :param rot: rotação do propulsor da embarcação.
        :type rot: numpy.ndarray
        
        """
       
        return sp.array([0.])
    
    def N (self,  rot=None):
        """Retorna  momento de yaw
        
        :param rot: Rotação do propulsor da embarcação.
        :type rot: numpy.ndarray
        
        """
        u = self.MostraVel()[0]
        if rot == None:
            rot = self.dic['rotnom']
        
        if rot >= sp.array([0.]):
            d = self.dic['d1']
            e = self.dic['e1']
            f = self.dic['f1']
        elif rot < sp.array([0.]):
            d = self.dic['d0']
            e = self.dic['e0']
            f = self.dic['f0']
            
        ud = sp.sqrt(d * (u ** 2) + e * u * rot * self.dic['dp'] + f * \
                    (rot * self.dic['dp']) ** 2)
        N = (self.dic['rho'] / 2) * (self.dic['lpp'] ** 3) * \
            (self.dic['ndr'] * (ud ** 2) * self.MostraLeme())
        
        return N

if __name__ == "__main__":
    import doctest
    doctest.testmod() 