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
    """
    Classe leme
    """
    tipo = 'Genérico'
    data = '10-11-2010'
    autor = 'Alex'
    def __init__(self):
        """"
        Construtor do leme

        """
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        self.lemeCom = sp.array(0.)
        self.leme = sp.array(0.)

    def MostraVel(self):
        """
        Retorna a velocidade
        """        
        return self.vel
        
    
    def MostraLeme(self):
        """
        Retorna o leme
        """
        return self.leme
        
    def MostraLemeCom(self):
        """
        Retorna o leme comandado
        """
        return self.lemeCom        
    
    def MostraPos(self):
        """
        Retorna a posição do casco
        """
        return self.pos

    def MudaLemeCom(self,  AngLeme):
        """
        Muda o leme comandado
        """
        self.lemeCom = AngLeme.copy()


    def MudaLeme(self, dt):
        """
        Muda o leme avançando um passo 'dt' no tempo
        """
        self.leme = self.leme + (self.lemeCom - self.leme)*(1-sp.exp(-self.dic['lambdaleme']*dt))
    def MudaVel(self,  Velocidade):
        """
        Muda a velocidade do casco
        """
        self.vel = Velocidade.copy()

    def MudaPos(self,  Posicao):
        """
        Muda a posição do casco
        """
        self.pos = Posicao.copy()
   
    def fx(self):
        """
        Retorna força em surge
        """
    def fy(self):
        """
        Retorna força em sway
        """
    def K(self):
        """
        Retorna o momento de roll
        """

    def N(self):
        """
        Retorna o momento de yaw
        """
