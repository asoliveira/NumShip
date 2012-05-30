# -*- coding: utf-8 -*-
 
import  scipy as sp

class  prop:
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
        self.Rot = sp.array(0.)
    def MostraVel(self):
        """
        Retorna a Velocidade do casco
        """
        return self.vel
        
        
    def MostraPos(self):
        """
        Retorna a posição do casco
        """
        return self.pos

    def MostraRot(self):
        """
        Muda a posição do casco
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


    def MudaRot(self,  dt):
        """
        """
        
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
