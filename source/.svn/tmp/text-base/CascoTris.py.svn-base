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

from CascoGen import *

class cascoTris(casco):
    """Subclasse de casco seguindo o modelo do Paper de Tristan Perez"""
      
    def __init__(self, DicionarioDerivadas):
        """"Cria uma instancia do casco com o modelo de `Tristan Perez`
        
        :param DicionarioDerivadas: Dicionário com os coeficientes do casco e
                                    outros dados.
        :type DicionarioDerivadas: dic

        """
        
        casco.__init__(self)
        self.dic = DicionarioDerivadas
        
    def MudaVel(self,  Velocidade):
        """Muda a velocidade da embarcação
        
        :param Velocidade: Velocidade do casco a ser implementada.
        :type Velocidade: numpy.ndarray
        
        """
        
        vel = Velocidade.copy()
        self.V = sp.sqrt(vel[0] ** 2 + vel[1] ** 2)
        vel[0] = vel[0] - self.dic['unom']
        vel [:3]= vel[:3] / self.V
        vel[3:]= vel[3:] * self.dic['lpp'] / self.V 
        self.vel = vel
        
    def MudaPos(self, Posicao):
        """Muda a posição e orientação do casco
        
        :param Posicao: Array de posição e orientação a ser implementada.
        :type Posicao: numpy.ndarray
        
        """
        
        pos = Posicao.copy()
        pos[:3] = pos[:3] / self.dic['lpp']
        self.pos = pos

    def filtrar(self, eixo):
        """Testa se todos as variáveis necessárias estão no parâmetro
           DicionarioDerivadas.
        
        *Ainda não implementada*
        
        Com o dicionário passado na criação da classe com valores como 
        {'xvr' = 54,...} e testa se todos os valores necessários para a
        implementação da classe foram passados lista= ['yur', 'rtu',...] 
        estão em dic caso não estejam devolve a uma lista *return*.
        
        :param eixo: Eixo a ser analisado.
        :type eixo: str.
        :return:
        :rtype: list
        """

        #Ainda é necessário implementar as função self.listaf* e self.listam*
        
        outofdic = []
        
        if eixo.lower() == 'x':
            lista = list(self.listafx)
        elif eixo.lower()=='y':
            lista = list(self.listafy)
        elif eixo.lower()=='k':
            lista = list(self.listamk)
        elif eixo.lower()=='n':
            lista = list(self.listamn)
          
        #teste se está na lista

        for arg in lista:
            if arg not in self.dic:
                outofdic.append(arg)
      
        return outofdic

    def gz (self):
        """Calcula a função Gz"""

        bm = self.dic['km']-self.dic['kb']
        
        return (self.dic['gm'] + bm*0.5*sp.tan(self.pos[3])**2)*sp.sin(self.pos[3])/self.dic['lpp']

      
    def Fx (self):
        """Forças em Surge"""

        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]

        X = self.dic['xu'] * ua + self.dic['xuu'] * ua * ua + \
            self.dic['xuuu'] * (ua ** 3) + self.dic['xvr'] * v * r + \
            self.dic['xrr'] * (r ** 2) + self.dic['xv'] * v + \
            self.dic['xvv'] * (v ** 2) + self.dic['xvroll'] * v * \
            self.pos[3] + self.dic['xroll'] * self.pos[3] + \
            self.dic['xrroll'] * (self.pos[3] ** 2) + self.dic['xpp'] * \
            p ** 2 + self.dic['xppu'] * (p ** 2) * ua
            
        return X * ((self.dic['rho'] * (self.V * self.dic['lpp']) ** 2) / 2)
    
    def Fy (self):
        """Forcas em Sway"""

        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        Y = self.dic['yv'] * v + self.dic['yvv'] * (v ** 2) + \
            self.dic['yv|v|'] * v * abs(v) + self.dic['yv|r|'] * v * \
            abs(r) + self.dic['yvrr'] * v * (r ** 2) + self.dic['yr'] * \
            r + self.dic['yr|r|'] * r * abs(r) + self.dic['yrrr'] * \
            (r ** 3) + self.dic['yr|v|'] * r * abs(v) + self.dic['yrvv'] * \
            r * (v ** 2) + self.dic['yp'] * p + self.dic['yppp'] * \
            (p ** 3) + self.dic['ypu'] * p * ua + self.dic['ypu|pu|'] * p * \
            ua * abs(p *ua) + self.dic['yroll'] * self.pos[3] + \
            self.dic['yvroll'] * v * \
            self.pos[3] + self.dic['yvrroll'] * v * (self.pos[3] ** 2) + \
            self.dic['yrollvv'] * self.pos[3] * (v ** 2) + self.dic['y0'] + \
            self.dic['y0u'] * ua
        
        return Y * ((self.dic['rho'] * (self.V * self.dic['lpp']) ** 2) / 2)

    def K (self):
        """Momento de Roll"""

        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        K = self.dic['kv'] * v + self.dic['kvv'] * (v ** 2) + \
            self.dic['kv|v|'] * v * abs(v) + self.dic['kv|r|'] * v * \
            abs(r) + self.dic['kvrr'] * v * (r ** 2) + self.dic['kr|r|'] * \
            r * abs(r) + self.dic['krrr'] * (r ** 3) + self.dic['krvv'] * \
            r * (v ** 2) + self.dic['kr|v|'] * r * abs(v) + self.dic['kp'] * \
            p + self.dic['kp|p|'] * p * abs(p) + self.dic['kppp'] * \
            (p ** 3) + self.dic['kpu'] * p * ua + self.dic['kpu|pu|'] * \
            abs(p * ua) * p * ua + self.dic['kvroll'] * v * self.pos[3] + \
            self.dic['kvrroll'] * v * self.pos[3] ** 2 + \
            self.dic['krollvv'] * self.pos[3] * v ** 2 + self.dic['k0'] + \
            self.dic['k0u'] * ua + self.dic['kr'] * r - (self.dic['g'] * \
            self.dic['deslo'] * self.gz()) / (((self.V * \
            self.dic['lpp']) ** 2) / 2)
        
        return K * (self.dic['rho'] * (self.V ** 2) * (self.dic['lpp'] ** \
                                                        3) / 2)

    def N (self):
        """Momento de Yaw"""
        
        ua = self.vel[0]
        v = self.vel[1]
        #w = self.vel[2] utilizar somente no caso de visualização
        p = self.vel[3]
        #q = self.vel[4] utilizar somente no caso de visualização
        r = self.vel[5]
        
        #ua = (u - self.dic['unom'])/u
        
        N = self.dic['nv'] * v + self.dic['nvv'] * v ** 2 + \
            self.dic['nv|v|'] * v * abs(v) + self.dic['nv|r|'] * v * \
            abs(r) + self.dic['nvrr'] * v * r ** 2 + self.dic['nr'] * r + \
            self.dic['nr|r|'] * r * abs(r) + self.dic['nrrr'] * r ** 3 + \
            self.dic['nrvv'] * r * v ** 2 + self.dic['nr|v|'] * r * \
            abs(v) + self.dic['np'] * p + self.dic['nppp'] * p ** 3 + \
            self.dic['npu'] * p * ua + self.dic['npu|pu|'] * p * ua * \
            abs(p * ua) + self.dic['nroll']    * self.pos[3] + \
            self.dic['nvroll'] * v * self.pos[3] + self.dic['nvrroll'] * \
            v * self.pos[3] ** 2 + self.dic['nrollvv'] * self.pos[3] * \
            v ** 2 + self.dic['n0'] + self.dic['n0u'] * ua
        
        return N * (self.dic['rho'] * (self.V ** 2) * \
                (self.dic['lpp'] ** 3) / 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()                                    