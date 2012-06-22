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

class lemeTris(leme):
    """Subclasse de leme seguindo o modelo do Paper de Tristan Perez"""
    
    tipo = 'Modelo paper Tristan'
    data = '10-10-2010'
    autor = 'Alex'
  
    def __init__(self, DicionarioDerivadas):
        """"Construtor do leme
        
        :param DicionarioDerivadas: Dicionário com os coeficientes do leme e
                                    outros dados [#f1]_ /.
        :type DicionarioDerivadas: dict
        
        .. rubric:: Footnotes
        
        .. [#f1]_ Para o *DicionarioDerivadas* pode se utilizar a função
                  Es.es.lerarqder como entrada e a função Es.gertemplate para
                  colocar os parâmetros necessários.

        """
        
        leme.__init__(self)
        self.dic = DicionarioDerivadas
        self.vel = sp.zeros((6, 1))
        self.pos = sp.zeros((6, 1))
        

    def MostraCoef(self,  chave):
        """Mostra o valor de um coeficiente do dicionário.
        
        :param chave: Chave do valor.
        :type chave: str
        
        """
        
        return self.dic[chave]
    
    def MudaVel(self,  velocidade):
        """Muda a velocidade da embarcação.
        
        :param velocidade: Nova velocidade.
        :type velocidade: numpy.ndarrray
        
        """
        
        vel =  velocidade.copy()

        self.V = sp.sqrt(vel[0] ** 2+ vel[1] ** 2)
        vel[0] = vel[0] -  self.dic['unom']
        vel [:3] = vel[:3] / self.V
        vel[3:] = vel[3:] * self.dic['lpp'] / self.V 
        self.vel = vel
        
    def MudaPos(self,  posicao):
        """Muda a posição e orientação do casco.
        
        :param posicao: Nova posição.
        :type posicao: numpy.ndarrray
        
        """
        pos = posicao.copy()
        pos[:3] = pos[:3]/self.dic['lpp']
        self.pos = pos
  
    def Fx (self):
        """Calcula o valor da forcas em surge"""
        
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        #ua = (u - self.dic['unom'])/u
    
        X = self.dic['xd'] * self.MostraLeme() + self.dic['xdd'] * \
            self.MostraLeme() ** 2 + self.dic['xdu'] * self.MostraLeme() * \
            ua + self.dic['xddu'] * ua * self.MostraLeme() ** 2 + \
            self.dic['xvd'] * v * self.MostraLeme() + self.dic['xvdd'] * \
            v * self.MostraLeme() ** 2
        
        return X * ((self.dic['rho'] * (self.V * self.dic['lpp']) ** 2) / 2)
    
    def Fy (self):
        """Calcula o valor da forcas em sway"""
        
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        Y = self.dic['yd'] * self.MostraLeme() + self.dic['ydd'] * \
            self.MostraLeme() ** 2 + self.dic['yddd'] * \
            self.MostraLeme() ** 3 + self.dic['ydv'] * self.MostraLeme() * \
            v + self.dic['ydvv'] * self.MostraLeme() * (v ** 2) + \
            self.dic['ydu'] * self.MostraLeme() * ua + self.dic['yddu'] * \
            ua * (self.MostraLeme() ** 2) + self.dic['ydddu'] * ua * \
            (self.MostraLeme() ** 3)
        
        return Y * ((self.dic['rho'] * (self.V * self.dic['lpp']) ** 2) / 2)
      
    def K (self):
        """Calcula o valor do momento de roll"""
        
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        P = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5] 
        #ua = (u - self.dic['unom'])/u
    
        K = self.dic['kd'] * self.MostraLeme() + self.dic['kdd'] * \
            self.MostraLeme() ** 2 + self.dic['kddd'] * \
            self.MostraLeme() ** 3 + self.dic['kdv'] * self.MostraLeme() * \
            v + self.dic['kdvv'] * self.MostraLeme() * v ** 2 + \
            self.dic['kdu'] * self.MostraLeme() * ua + self.dic['kddu'] * \
            ua * self.MostraLeme() ** 2 + self.dic['kdddu'] * ua * \
            self.MostraLeme() ** 3
    
        return K * (self.dic['rho'] * (self.V ** 2) * (self.dic['lpp'] ** \
                    3) / 2)
    
    def N (self):
        """Calcula o valor do momento de yaw"""
        
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]  
        #ua = (u - self.dic['unom'])/u
    
        N = self.dic['nd'] * self.MostraLeme() + self.dic['ndd'] * \
            self.MostraLeme() ** 2 + self.dic['nddd'] * \
            self.MostraLeme() ** 3 + self.dic['ndv'] * self.MostraLeme() * \
            v + self.dic['ndvv'] * self.MostraLeme() * v ** 2 + \
            self.dic['ndu'] * self.MostraLeme() * ua + self.dic['nddu'] * \
            ua * self.MostraLeme() ** 2 + self.dic['ndddu'] * ua * \
            self.MostraLeme() ** 3
        
        return N * (self.dic['rho'] * (self.V ** 2) * (self.dic['lpp'] ** \
                    3)/2)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod() 