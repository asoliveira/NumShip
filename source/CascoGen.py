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

class casco:
    """
    classe casco
    """
    tipo = 'Genérico'
    data = '10-11-2010'
    autor = 'Alex'
    def __init__(self):
        """
        Construtor do cacso
        __________________________

        """
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))


    def MostraVel(self):
        """
        Mostra a Velocidade do casco
        """
        return self.vel
        
        
    def MostraPos(self):
        """
        Mostra a posição do casco
        """
        return self.pos


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

    def Ma (self,  GrausDeLib = 4):
        """
        Retorna um  sp.array de  massa adicional
        """
        saida = None
        if GrausDeLib == 4:
            saida= sp.array([[self.dic['xdotu'], 0, 0, 0 ],[0, self.dic['ydotv'],  self.dic['ydotp'], self.dic['ydotr']],[0, self.dic['kdotv'], self.dic['kdotp'], self.dic['kdotr']],[0, self.dic['ndotv'], self.dic['ndotp'], self.dic['ndotr']]])   
            saida[:2, :2] = saida[:2, :2]* (self.dic['rho']*(self.dic['lpp']**3))/2
            saida[2:,:2]= saida[2:,:2]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[:2,2:]= saida[:2,2:]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2:, 2:] = saida[2:, 2:] * (self.dic['rho']*(self.dic['lpp']**5))/2    
        elif GrausDeLib == 3:
            saida= sp.array([[self.dic['xdotu'], 0, 0 ],[0, self.dic['ydotv'],  self.dic['ydotr']],[0, self.dic['ndotv'], self.dic['ndotr']]])   
            saida[:2, :2] = saida[:2, :2]* (self.dic['rho']*(self.dic['lpp']**3))/2
            saida[1,2]= saida[1,2]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2,1]= saida[2,1]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2, 2] = saida[2, 2] * (self.dic['rho']*(self.dic['lpp']**5))/2    
        return saida 

    def M(self,  GrausDeLib = 4):
        """
        Retorna um  sp.array de  massa e massa adicional
        """
        saida = None
        if GrausDeLib == 4:
            saida = sp.array([   [self.dic['m'] ,  0., 0., 0. ],
            [0., self.dic['m'],   -(self.dic['m'] *self.dic['zg']/self.dic['lpp'] ),     self.dic['m']*self.dic['xg']/self.dic['lpp']   ],  
            [0., -(self.dic['m']*self.dic['zg']/self.dic['lpp'] ), self.dic['ixx'], 0. ],
            [0., self.dic['m']*self.dic['xg'] /self.dic['lpp'] , 0., self.dic['izz'] ]])
            saida[:2, :2] = saida[:2, :2]* (self.dic['rho']*(self.dic['lpp']**3))/2
            saida[2:,:2]= saida[2:,:2]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[:2,2:]= saida[:2,2:]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2:, 2:] = saida[2:, 2:] * (self.dic['rho']*(self.dic['lpp']**5))/2
        elif GrausDeLib == 3:
            saida = sp.array([   [self.dic['m'] ,  0., 0.],
            [0., self.dic['m'],  self.dic['m']*(self.dic['xg']/self.dic['lpp'])   ],  
            [0., self.dic['m']*(self.dic['xg']/self.dic['lpp'])  , self.dic['izz']]])
            saida[:2, :2] = saida[:2, :2]* (self.dic['rho']*(self.dic['lpp']**3))/2
            saida[1, 2] = saida[1, 2]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2, 1] = saida[2, 1]* (self.dic['rho']*(self.dic['lpp']**4))/2
            saida[2, 2] = saida[2, 2]* (self.dic['rho']*(self.dic['lpp']**5))/2
        return saida
   
    def Fx(self):
        """
        Devolve a força em surge
        """
    def Fy(self):
        """
        Devolve a força em sway
        """
    def K(self):
        """
        Devolve o momento de roll
        """

    def N(self):
        """
        Devolve o momento de yaw
        """
