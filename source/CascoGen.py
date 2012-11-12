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
    """Classe casco"""

    def __init__(self):
        """Construtor do caso"""
        
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))


    def MostraVel(self):
        """Mostra a Velocidade do casco"""
        
        return self.vel
        
    def MostraPos(self):
        """Mostra a posição do casco"""
        
        return self.pos


    def MudaVel(self,  Velocidade):
        """Muda a velocidade do casco"""
        
        self.vel = Velocidade

    def MudaPos(self,  Posicao):
        """Muda a posição do casco"""
        
        self.pos = Posicao

    def Ma (self,  GrausDeLib = 4):
        r"""Retorna um  sp.array de  massa adicional.
        
        No caso do modelo matemático escolhido ser o 'MARAD' 
        retorna a matriz:
        
        .. math::
      
            M = \begin{bmatrix}
            \dfrac{\rho L^3}{2}X_{\dot u} &0 &0 \\
            0 &\dfrac{\rho L^3}{2}Y_{\dot v} &\dfrac{\rho L^4}{2}Y_{\dot r}\\
            0 &\dfrac{\rho L^4}{2}N_{\dot v} & \dfrac{\rho L^5}{2}N_{\dot r}
            \end{bmatrix}
       
        :param GrausDeLib: Valor dos graus de liberdade do modelo matemático;
        :type GrausDeLib: int
        :return: Matriz de massa adicional. Não retorna nada se o valor dos
                 graus de liberdade for diferente de 4 ou 3.
        :rtype: numpy.ndarray
        
        """
        
        saida = None
        
        #coeficiente para dimensionalizar os termos de massa
        coefm = (self.dic['rho'] * (self.dic['lpp'] ** 3)) / 2
        
        if GrausDeLib == 4:
            saida= sp.array([[self.dic['xdotu'], 0, 0, 0 ],
                   [0, self.dic['ydotv'], self.dic['ydotp'],
                   self.dic['ydotr']], [0, self.dic['kdotv'],
                   self.dic['kdotp'], self.dic['kdotr']], [0,
                   self.dic['ndotv'], self.dic['ndotp'], self.dic['ndotr']]])  
            saida[:2, :2] = saida[:2, :2] * (self.dic['rho'] * 
                            (self.dic['lpp'] ** 3)) / 2
            saida[2:,:2] = saida[2:,:2] * (self.dic['rho'] * 
                           (self.dic['lpp'] ** 4)) / 2
            saida[:2,2:] = saida[:2,2:] * (self.dic['rho'] * 
                           (self.dic['lpp'] ** 4)) / 2
            saida[2:, 2:] = saida[2:, 2:] * (self.dic['rho'] * 
                            (self.dic['lpp'] ** 5)) / 2    
        elif GrausDeLib == 3:
            saida= sp.array([[self.dic['xdotu'] * coefm,
            0,
            0,
            0,
            0,
            0],
            # 
            [0,
            self.dic['ydotv'] * coefm,
            0,
            0,
            0,
            self.dic['ydotr'] * coefm * self.dic['lpp']],
            ## w, p, q são zerados em 3 graus de liberdade 
            [0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.],
            #
            [0,
            self.dic['ndotv'] * coefm * self.dic['lpp'],
            0,
            0,
            0,
            self.dic['ndotr'] * coefm * self.dic['lpp'] ** 2]])
        
        return saida 

    def Massa(self,  GrausDeLib = 4):
        """Retorna a matriz de massa e inercia"""
        
        saida = None
        
        #coeficiente para dimensionalizar os termos de massa
        coefm = (self.dic['rho'] * (self.dic['lpp'] ** 3)) / 2
        
        if GrausDeLib == 4:
            saida = sp.array([[self.dic['m'], 
            0.,
            0., 
            0.
            ],
            #
            [0., 
            self.dic['m'], 
            -(self.dic['m'] * self.dic['zg'] / self.dic['lpp']),
            self.dic['m'] * self.dic['xg'] / self.dic['lpp']],
            #
            [0., 
            -(self.dic['m'] * self.dic['zg'] / self.dic['lpp']),
            self.dic['ixx'], 
            0.],
            #
            [0., 
            self.dic['m'] * self.dic['xg'] / self.dic['lpp'] ,
            0.,
            self.dic['izz']]
            ])
            
            saida[:2, :2] = saida[:2, :2] * \
                            (self.dic['rho'] * (self.dic['lpp'] ** 3)) / 2
            
            saida[2:,:2]= saida[2:, :2] * \
                          (self.dic['rho'] * (self.dic['lpp'] ** 4)) / 2
            
            saida[:2,2:]= saida[:2,2:] * \
                          (self.dic['rho'] * (self.dic['lpp'] ** 4)) / 2
            
            saida[2:, 2:] = saida[2:, 2:] * \
                            (self.dic['rho'] * (self.dic['lpp'] ** 5)) / 2
                            
        elif GrausDeLib == 3:
            saida = sp.array([[self.dic['m'] * coefm,
            0.,
            0.,
            0.,
            0.,
            0.],
            #
            [0.,
            self.dic['m'] * coefm,
            0.,
            0.,
            0.,
            self.dic['m'] * self.dic['xg'] * coefm],
            # w, p, q são zerados em 3 graus de liberdade
            [0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0.],
            #
            [0.,
            self.dic['m'] * self.dic['xg'] * coefm,
            0.,
            0.,
            0.,
            self.dic['izz'] * coefm * self.dic['lpp'] ** 2]
            ])
                    
        return saida
   
    def fx(self):
        """Retorna força em Surge"""
        
        return sp.array([0.])
    
    def fy(self):
        """Retorna força em Sway"""
        
        return sp.array([0.])

    def fz(self):
        """Retorna força em Heave"""
        
        return sp.array([0.])
    
    def K(self):
        """Retorna o momento de Roll"""
        
        return sp.array([0.])

    def fy(self):
        """Retorna força em Pitch"""
        
        return sp.array([0.])              

    def N(self):
        """Retorna o momento de Yaw"""
        
        return sp.array([0.])

if __name__ == "__main__":
    import doctest
    doctest.testmod()                        