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

    def N(self):
        """Retorna o momento de Yaw"""
        
        return sp.array([0.])
