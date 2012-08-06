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
 
import  scipy as sp

class  prop:
    
    def __init__(self):
        
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        self.Rot = sp.array(0.)
        
    def MostraVel(self):
        """Retorna a Velocidade do casco"""
        
        return self.vel
       
    def MostraPos(self):
        """Retorna a posição do casco"""
        
        return self.pos

    def MostraRot(self):
        """Muda a posição do casco
        """
        return self.Rot
        
    def MudaRotCom(self,  Rot):
        """
        Muda a posição do casco
        """
                
    def MudaVel(self,  Velocidade):
        """
        Muda a velocidade do casco
        """
        self.vel = Velocidade
        
    def MudaPos(self,  Posicao):
        """
        Muda a posição do casco
        """
        self.pos = Posicao


    def MudaRot(self, dt):
        """Muda a rotação da máquina caminhando um passo 'dt' no tempo"""
        
        self.Rot = self.Rot + (self.RotCom - self.Rot) * \
                   (1 - sp.exp( - self.dic['lambdaprop'] * dt))
                   

    def MudaRotCom(self,  Rot):
        """
        """        
        
    def Fx(self):
        """
        Devolve a força em surge
        """
        return sp.array(0.)
        
    def Fy(self):
        """
        Devolve a força em sway
        """
        return sp.array(0.)
        
    def K(self):
        """
        Devolve o momento de roll
        """
        return sp.array(0.)

    def N(self):
        """
        Devolve o momento de yaw
        """
        return sp.array(0.)
