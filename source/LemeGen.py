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
import numpy  as np

class leme:
    """Classe leme"""

    def __init__(self):
        
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        self.lemeCom = sp.array(0.)
        self.leme = sp.array(0.)

    def MostraVel(self):
        """Retorna a velocidade"""        
        
        return self.vel
        
    
    def MostraLeme(self):
        """Retorna o leme"""
        
        return self.leme
        
    def MostraLemeCom(self):
        """Retorna o leme comandado"""
        
        return self.lemeCom        
    
    def MostraPos(self):
        """Retorna a posição do casco"""
        
        return self.pos

    def MudaLemeCom(self,  AngLeme):
        """Muda o leme comandado"""
        
        self.lemeCom = AngLeme.copy()

    def MudaLeme(self, dt):
        """Muda o leme avançando um passo 'dt' no tempo"""
        
        self.leme = self.leme + (self.lemeCom - self.leme) * (1 -
                    sp.exp(-self.dic['lambdaleme'] * dt))
                    
    def MudaVel(self,  Velocidade):
        """Muda a velocidade do casco"""
        
        self.vel = Velocidade.copy()

    def MudaPos(self,  Posicao):
        """Muda a posição do casco"""
        
        self.pos = Posicao.copy()
   
    def Fx(self):
        """Retorna força em Surge"""
        
        return sp.array([0.])
    
    def Fy(self):
        """Retorna força em Sway"""
        
        return sp.array([0.])

    def Fz (self):
        """Retorna a força no eixo z do sistema solidário
        
        O modelo matemático é de 3 graus de liberdade, assim esta força não é calculado. Esta função retorna um array de valor *zero*
        apenas para suprir alguma compatibilidade do programa"""
       
        return sp.array([0.])
      
    def K (self):
        """Retorna o momento em torno do eixo x
        
        O modelo matemático é de 3 graus de liberdade, assim o momento em torno do eixo y não é calculado. Esta função retorna um array de valor *zero*
        apenas para suprir alguma compatibilidade do programa"""
       
        return sp.array([0.])
        
    def M (self):
        """Retorna o momento em torno do eixo y
        
        O modelo matemático é de 3 graus de liberdade, assim o momento em torno do eixo y não é calculado. Esta função retorna um array de valor *zero*
        apenas para suprir alguma compatibilidade do programa"""
       
        return sp.array([0.])

    def Fy(self):
        """Retorna força em Pitch"""
        
        return sp.array([0.])              

    def N(self):
        """Retorna o momento de Yaw"""
        
        return sp.array([0.])

if __name__ == "__main__":
    import doctest
    doctest.testmod()                        