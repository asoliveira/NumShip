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

"""
Módulo Es
=========

Biblioteca com o propósito de auxiliar na leitura dos dados de entrada

"""

#Bibliotecas do python
import os
#Bibliotecas de terceiros
import matplotlib.pyplot as plt
import scipy as sp
#Bibliotecas do NumShip
from Navio import *

def gerartemplate(nome = 'inputder.dat', valor = ' <valor>,'):
    """Gera um `template` para o arquivo de derivadas hidrodinâmicas.
            
    :param nome: Nome do arquivo de saída. (default 'inputder.dat');
    :param valor: Preenchimento do campo para ser substituído pelo valor das
                  derivadas.default ' <valor>'
    :type nome: str
    :type valor: str
    
    """
    listafx = ('xdotu', 'xu', 'xuu', 'xuuu', 'xvr', 'xrr', 'xv', 'xvv',
    'xvroll', 'xroll', 'xrroll', 'xpp', 'xpp', 'xppu')
    listafy = ('ydotv', 'ydotr', 'ydotp', 'yv', 'yvv', 'yv|v|', 'yv|r|',
    'yrvv', 'yp', 'yppp', 'ypu', 'ypu|pu|', 'yroll', 'yvroll', 'yvrroll',
    'yrollvv', 'y0', 'y0u')
    listak = ('kdotp', 'kdotv', 'kdotr', 'kv', 'kvv', 'kv|v|', 'kv|r|',
    'kvrr', 'kr|r|', 'krrr', 'krvv', 'kr|v|', 'kp', 'kp|p|', 'kppp', 'kpu',
    'kpu|pu|', 'kv', 'kvroll', 'kvrroll', 'krollvv', 'k0', 'k0u', 'kr',
    'deslo', 'rho','g')
    listan = ('ndotv', 'ndotr', 'ndotp', 'nv', 'nvv', 'nv|v|', 'nv|r|',
    'nvrr', 'nr', 'nr|r|', 'nrrr', 'nrvv', 'nr|v|', 'np', 'nppp', 'npu',
    'npu|pu|', 'nroll', 'nvroll', 'nvrroll', 'nrollvv', 'n0', 'n0u') 
    
    f = open(nome, 'w')
    
    f.write('#\n'), f.write('#\n')
    f.write('#\t Modelo de arquivo para entrada das derivadas \
    hidrodinâmicas')
    f.write('#\n'), f.write('#\n')
    
    f.write('\n \n')
    
    f.write('#'+'Surge'.center(29)+ '\n')
    cont = 0
    for arg in listafx:
        impre = arg.ljust(8) + '=' + valor
        f.write ( impre.ljust(26),)
        cont += 1
    
        if cont == 3:
            f.write('\n')
            cont = 0
    
    f.write('\n \n')
    
    f.write('#'+'Sway'.center(29)+ '\n')
    cont = 0
    for arg in listafy:
        impre = arg.ljust(8) + '=' + valor
        f.write ( impre.ljust(26),)
        cont += 1
    
        if cont == 3:
            f.write('\n')
            cont = 0
    
    f.write('\n \n')
    
    f.write('#'+'Roll'.center(29)+ '\n')
    cont = 0
    for arg in listak:
        impre = arg.ljust(8) + '=' + valor
        f.write ( impre.ljust(26),)
        cont += 1
    
        if cont == 3:
            f.write('\n')
            cont = 0
    
    
    f.write('\n \n')
    
    f.write('#'+'Yaw'.center(29)+ '\n')
    cont = 0
    for arg in listan:
        impre = arg.ljust(8) + '=' + valor
        f.write ( impre.ljust(26),)
        cont += 1
    
        if cont == 3:
            f.write('\n')
            cont = 0
    
    f.close()
        
class es (object) :
    """Classe para auxiliar na entrada e saída de dados."""
    
    def __init__(self, entrada):
        """
        :param entrada: Tupla com 3 argumentos:
            
            * entrada[0] -- Nome do navio. *Tipo string*\;        
            * entrada[1] -- Caminho do arquivo de entrada contendo o valor 
              das derivadas hidrodinâmicas. *Tipo string*\;
            * entrada[2] -- Caminho do arquivo de entrada contendo o valor    
              das forças tabeladas. *Tipo string*\;
                            
        :type entrada: tuple
        
        .. seealso:: Caso queira saber como é a forma do arquivo entrada[1]
                     utilize a função `gerartempder([nome,valor])` \. Esta
                     função gera um template para entrada dos valores.
        
        """
        
        self. nomenavio1 = entrada[0]
        self.arqder = entrada[1]
        self.arqtab =  entrada[2]
        self.bdder = ''
        self.bdtab = ''
        self.log = 'line'
            
    def listararq(self, separator=',', comment='#'):
        """Processa o arquivo de entrada.
        
        Lê o arquivo *entrada[0]* e devolve uma lista com todas as letras
        minúsculas sem "enter" e sem espaço separada pela marcação do
        separador.
        
        :param separator: Separa um valor do outro. default(',');
        :param comment: O indicador do comentário. default('#');
        :return: Retorna uma lista com os valores do arquivo de entrada;
        :type separator: str
        :type comment: str
        :rtype: list
        
        :Example:
        
            >>> import Es
            >>> entrada = ('NavioTeste', '../dados/bemformatado.dat',
            ... 'inputtab.dat')
            >>> en = Es.es(entrada)
            >>> en.listararq()[:3]
            ['xdotu=-8.59e-4', 'xvr=1.095e-2', 'xvv=2.87e-3']
        
        """
        
        f = file(self.arqder , 'r' )

        output = []

        for line in f:
            if '#' in line:
                line = line.replace(line[line.index('#'):-1],'')
            line = line.replace(' ','')
            line = line.replace('\n','')
            line = line.replace('\t','')
            output.extend(line.split(separator))

        while '' in  output:
            output.remove('')

        return output
    
        
    def checkformat(self):
        """Verifica se os dados do arquivo de entrada estão corretos.
        
        Os erros de formatação mais de comuns que são verificados por esta
        função são mais de um ‘.’ ou ‘-‘ ou valores alfanuméricos (exceto
        obviamente os    números em notação científica como 10e5). Exemplo: 
        xu = 10–e3, yv = 23ee4.
        
        :return: Retorna uma lista dos valores formatados errados no arquivo 
                 de entrada (entrada[1]).
        
        :Exemple:

            >>> import Es
            >>> entrada = ('NavioTeste', '../dados/mauformatado.dat',
            ... 'inputtab.dat')
            >>> en = Es.es(entrada)
            >>> en.checkformat()
            ['ndotv']
            >>> #Neste caso 'xdotv' foi escrito assim:
            >>> #'ndotv = --5.0e-5,', ou seja, possui mais de um sinal '-'
        
        """
        
        lista = self.listararq()
        erro =[]
        for arg in lista:
          arg = arg.partition('=')
          a = arg[2].replace('.','')
          a = a.replace('-','')
          a = a.replace('e','')
        
          if not ((arg[2][arg[2].find('e'):].count('-') < 2) and      
                (arg[2][:arg[2].find('e')].count('-') < 2) and
                (arg[2][arg[2].find('e'):].count('.') < 2) and
                (arg[2][:arg[2].find('e')].count('.') < 2) and
                (arg[2].count('e') < 2) and
                (a.isdigit()) and len(arg) == 3):
            erro.append(arg[0])
                    
        return erro
    
    def lerbdtab(self):
        """ Lê o banco de dados com os valores de força tabelados
        
        Ainda não implementado
        
        """
        pass
    
    def lerarqder(self, separator=',', comment='#'):
        """Processa a entrada das derivadas hidrodinâmicas.

        Devolve um dicionário de `sp.array` com os valores possuindo como 
        chaves o nome das variáveis em letra minúscula.
                
        :param separator: Separador de uma variável da outra. (default ',');
        :param comment: Indicativo de linha para comentário. (default '#');
        :return: Devolve um dicionário de sp.array com os valores possuindo
                 como chaves o nome das derivadas hidrodinâmicas em letra
                 minúscula;
        :type separator: str
        :type comment: str
        :rtype: dict
        
        :Exemple:
        
            >>> import Es
            >>> entrada = ('NavioTeste', '../dados/bemformatado.dat',
            ... 'inputtab.dat')
            >>> en = Es.es(entrada)
            >>> en.lerarqder()['rotnom']
            array(0.62)

        """
                  
        temp = []
        
        f = self.listararq(separator, comment)
                
        for i in f:
            temp.append(i.split('='))
        
        while '' in  temp:
            temp.remove('')

        output = {}
        
        for i in range (len(temp)):
          output[temp[i][0].lower()] = sp.array(float(temp[i][1]))
            
        return output
    
    def lerarqtab(self):
        
        """Lê o arquivo de forças tabeladas.
        
        Ainda não implementado.
        
        """
        pass
    
    def lerbdder(self):
        """Lê banco de dados de derivadas hidrodinâmicas.
        
        Ainda não implementado.
        """
        pass
    
    def fxdertotab (self, intervalo=5, Tipo = 'MARAD', rot=sp.array(1.23), 
                    vel=12.7):
        """ Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma matriz tabelada de forças em surge do tipo `sp.array`. 
        
        É necessário carregar um arquivo de derivadas em entrada [1].
         
        :param intervalo: Intervalo do ângulo beta em graus(default = 5);
        :param Tipo: Tipo de modelo matemático a ser 
                     utilizado(‘MARAD’, ‘TP’);
        :param rot: Número de rotações por do propulsor;
        :param vel: Velocidade "u"  inicial. Não coloque "0.0"(zero), pois
                    retornará um array com coluna de valor "nan"(infinito);
        :return: Um sp.array do tipo; sp.array[beta, Fx]), onde:

                 * Beta -- Ângulo de ataque;
                 * Fx -- Forças em Surge.
                
        :type intervalo: int
        :type Tipo: str
        :type rot: sp.array
        :type vel: float
        :rtype: sp.array
        
        :Example:
        
            >>> import Es
            >>> entrada = ('NavioTeste', '../dados/bemformatado.dat',
            ... 'inputtab.dat')
            >>> en = Es.es(entrada)
            >>> print en.fxdertotab()[:2,]
            [[  0.00000000e+00  -7.74662690e+06]
             [  5.29411765e+00  -7.47437622e+06]]
        
        """
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome='Teste', Tipo=Tipo)
        navio1.MudaRotCom(rot)
        
        
        saida = sp.zeros([sp.size(sp.linspace(0. , sp.pi/2, 90/intervalo)), 2])
        
        posicao = sp.zeros((6, 1))
        velocidade = sp.zeros((6, 1))
        velocidade[0] = vel
        leme= sp.array(0.)
        
        navio1.MudaVel(velocidade)
        navio1.MudaPos(posicao)
        navio1.MudaLemeCom(leme)
        
        
        a = []
        contlinha = 0
        for beta in sp.linspace(0. , sp.pi/2, 90/intervalo):
            velocidade[0] = sp.array([vel])*sp.cos(beta)
            velocidade[1] = -sp.array([vel])*sp.sin(beta)
            navio1.MudaVel(velocidade)
            a.append(navio1.CalcFx())
            saida[contlinha] = sp.array([beta * 180. / sp.pi, 
                                        navio1.CalcFx()])
            contlinha += 1
            
        return saida
        
    def fydertotab (self, intervalo = 5., Tipo = 'MARAD', Rot=sp.array(1.23)):
        """Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma tabela de forças em sway do tipo sp.array. 
        
        É necessário carregar um arquivo de derivadas em entrada [1].
       
        Variáveis de entrada
       
        Intervalo = intervalo do ângulo beta em graus (default = 5).
       
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        Fy = Forças em Sway.
        
        """
        
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome='Teste', Tipo=Tipo)
        navio1.MudaRotCom(Rot)
       
        
        saida = sp.zeros([len(sp.arange(0., sp.pi, intervalo * sp.pi/180)),
        2])
        
        Posicao = sp.zeros((6, 1))
        Velocidade = sp.zeros((6, 1))
        Leme= sp.array(0.)
        
        navio1.MudaVel(Velocidade)
        navio1.MudaPos(Posicao)
        navio1.MudaLeme(Leme)
        
        contlinha = 0
        for beta in sp.arange(0., sp.pi, intervalo * sp.pi / 180):
            Velocidade[0] = sp.array([12.7]) * sp.cos(beta)
            Velocidade[1] = -sp.array([12.7]) * sp.sin(beta)
            navio1.MudaVel(Velocidade)
            saida[contlinha] = sp.array([beta * 180/sp.pi, navio1.CalcFy()])
            contlinha += 1
            
        return saida
    
    def kdertotab (self, intervalo = 5, Tipo = 'MARAD', Rot=sp.array(1.23)):
        """Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma tabela de Momento de roll do tipo sp.array. 
        
        Variáveis de entrada
        
        Intervalo = intervalo do ângulo beta em graus
        Default = 5.
        
        É necessário carregar um arquivo de derivadas em entrada [1].
        
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        K = Momento de roll.
        
        """    
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome='Teste', Tipo=Tipo)
        navio1.MudaRotCom(Rot)
        
        
        saida = sp.zeros([len(sp.arange(0., sp.pi, intervalo * sp.pi / 180)),
        2])
        
        Posicao = sp.zeros((6, 1))
        Velocidade = sp.zeros((6, 1))
        Leme= sp.array(0.)
        
        navio1.MudaVel(Velocidade)
        navio1.MudaPos(Posicao)
        navio1.MudaLeme(Leme)
        
        contlinha = 0
        for beta in sp.arange(0. , sp.pi, intervalo* sp.pi/180):
            Velocidade[0] = sp.array([12.7])*sp.cos(beta)
            Velocidade[1] = -sp.array([12.7])*sp.sin(beta)
            navio1.MudaVel(Velocidade)
            saida[contlinha] = sp.array([beta*180/sp.pi, navio1.CalcK()])
            contlinha += 1
            
        return saida
  
    def ndertotab (self, intervalo=5, Tipo='MARAD', Rot=sp.array(1.23)):
        """Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma tabela de Momento de yaw do tipo sp.array. 
        
        É necessário carregar um arquivo de derivadas em entrada [1].
        
        Variáveis de entrada
        
        Intervalo = intervalo do ângulo beta em graus
        Default = 5.
        
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        N = Momento de yaw.
        
        """     
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome='Teste', Tipo='TP')
        navio1.MudaRotCom(Rot)
        
        
        saida = sp.zeros([len(sp.arange(0., sp.pi, intervalo * sp.pi / 180)),
        2])
        
        Posicao = sp.zeros((6, 1))
        Velocidade = sp.zeros((6, 1))
        Leme= sp.array(0.)
        
        navio1.MudaVel(Velocidade)
        navio1.MudaPos(Posicao)
        navio1.MudaLeme(Leme)
        
        contlinha = 0
        for beta in sp.arange(0. , sp.pi, intervalo* sp.pi/180):
            Velocidade[0] = sp.array([12.7])*sp.cos(beta)
            Velocidade[1] = -sp.array([12.7])*sp.sin(beta)
            navio1.MudaVel(Velocidade)
            saida[contlinha] = sp.array([beta*180/sp.pi, navio1.CalcN()])
            contlinha += 1
            
        return saida
    def plotfxb (self, intervalo = 5., save= True , formato = 'eps', Tipo
= 'MARAD'):
        
        """
        Plota o gráfico de forças em surge contra beta
        
        Variáveis de entrada:
        
        Intervalo (Float)-- intervalo do ângulo beta em graus. Default = 5.;
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura; 
        
        É necessário carregar um arquivo de derivadas em entrada [1];
        Salva as figuras  no diretório './figuras/tab/
        
        """
        temp = self.fxdertotab(intervalo = intervalo, Tipo= Tipo)
        plt.plot(temp[0:,0] * (180/sp.pi), temp[0:,1], 'r--')
        
        plt.ylabel(r'$F_x$')
        plt.xlabel(r'$\beta$')
        plt.title (r'$F_x \quad X \quad \beta$')
        
        if save:
            plt.savefig('./figuras/tab/pltfxb', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
        

    def plotfyb (self, intervalo=5., save=True, formato='eps', Tipo='MARAD'):
        """Plota o gráfico de forças em sway contra beta
        
        Variáveis de entrada:
        
        Intervalo (Float)-- intervalo do ângulo beta em graus. Default = 5.;
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura; 
        
        É necessário carregar um arquivo de derivadas em entrada [1];
        Salva as figuras  no diretório './figuras/tab/
        """
        temp = self.fydertotab(intervalo = intervalo, Tipo= Tipo)
        plt.plot(temp[0:,0] * (180/sp.pi), temp[0:,1], 'r--')

        plt.ylabel(r'$F_y$')
        plt.xlabel(r'$\beta$')
        plt.title (r'$F_y$ x $\beta$')
        
        if save:
            plt.savefig('./figuras/tab/pltfyb', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
      

    def plotkb (self, intervalo=5., save= True, formato='eps', Tipo='MARAD'):
        """Plota o gráfico de momento  de roll em surge contra beta
        
        Variáveis de entrada:
        
        Intervalo (Float)-- intervalo do ângulo beta em graus. Default = 5.;
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura; 
        
        É necessário carregar um arquivo de derivadas em entrada [1];
        Salva as figuras  no diretório './figuras/tab/
        """
        temp = self.kdertotab(intervalo = intervalo, Tipo= Tipo)
        plt.plot(temp[0:,0] * (180/sp.pi), temp[0:,1], 'r--')
        
        
        plt.ylabel(r'$M_{\phi}$')
        plt.xlabel(r'$\beta$')
        plt.title (r'$M_{\phi}$ x $\beta$')
        
        if save:
            plt.savefig('./figuras/tab/pltkb', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
        
    def plotnb (self, intervalo=5., save= True, formato='eps', Tipo='MARAD'):
        """Plota o gráfico de momento de yaw em surge contra beta
        
        Variáveis de entrada:
        
        Intervalo (Float)-- intervalo do ângulo beta em graus. Default = 5.;
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura; 
        
        É necessário carregar um arquivo de derivadas em entrada [1];
        Salva as figuras  no diretório './figuras/tab/
        """
        temp = self.ndertotab(intervalo = intervalo, Tipo= Tipo)
        plt.plot(temp[0:,0] * (180/sp.pi), temp( intervalo)[0:,1], 'r--')

        plt.ylabel(r'$M_{\psi}$')
        plt.xlabel(r'$\beta$')
        plt.title (r'$M_{\psi}$ x $\beta$')
        
        if save:
            plt.savefig('./figuras/tab/pltnb', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()


    def plotzz(self, save=True, formato='eps', passo=0.5, tmax=200, tini= 0,
        metodo='euler', TipoModelo='TP', GrausDeLib=4, LemeCom=sp.array(10.), 
        Proa=sp.array(10.)):
        """Plota curva de ZigZag
        
        Variáveis de entrada:
        
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da 
        figura;
        passo (float) -- Paso de tempo da integração;
        tmax  (integer) -- Tempo  máximo;
        tini (integer) -- Tempo inicial;
        metodo ('euler') -- Método de integração;
                
        Salva as figuras  no diretório './figuras/Curva_de_Giro/curva_de_giro'
        
        """ 
        
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome = 'Teste', Tipo = TipoModelo
)
        
        
        a = navio1.simula(met = metodo, t = tmax, t0 = tini, dt=passo, 
GrausDeLib = GrausDeLib, tipo ='ZigZag', leme = LemeCom, proa = Proa)
        dir = './figuras/Zig_Zag/' + TipoModelo + '/' 
        os.makedirs(dir)
####################################
##
##       Velocidade em Surge
##
####################################        
        plt.plot(a[0][:, 0], a[0][:, 1], 'bo')
        plt.ylabel(r'$u$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltut', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Velocidade em Sway
##
####################################
        plt.plot(a[0][:, 0], a[0][:, 2], 'g^')#v 

        plt.ylabel(r'$v$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltvt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
###################################
#
#       Velocidade de yaw
#
###################################   
        plt.plot(a[0][:, 0], a[0][:, 6])
        
        plt.ylabel(r'$\dot\psi$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltvelyawt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
####################################
##
##       Velocidade de roll
##
####################################   
        plt.plot(a[0][:, 0], a[0][:, 4], '--')#r 
        
        plt.ylabel('$\dot\phi$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltvelrollt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
##
##
##       Posição
##
####################################
##
##       Posição x
##
####################################        
        plt.plot(a[1][:, 0], a[1][:, 1], '--')
        plt.ylabel(r'$x$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltxt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Posição y
##
####################################
        plt.plot(a[1][:, 0], a[1][:, 2], 'g^')#v 

        plt.ylabel(r'$y$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltyt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###       Posição Psi
###
#####################################   
        plt.plot(a[1][:, 0], a[1][:, 6] * (180/sp.pi), 'o-', a[5][:, 0], 
        a[5][:, 1] * (180/sp.pi), '-.')
        
        plt.ylabel(r'$\psi$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltyawt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       orientação roll
###
#####################################   
        plt.plot(a[1][:, 0], a[1][:, 4], 'o-')
        
        plt.ylabel(r'$\phi$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltrollt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
##
##
##       Aceleração
##
##



####################################
##
##       dotu
##
####################################        
        plt.plot(a[2][:, 0], a[2][:, 1], '--')
        plt.ylabel(r'$\dot u$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltdotut', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       dot v
##
####################################
        plt.plot(a[2][:, 0], a[2][:, 2], 'g^')#v 

        plt.ylabel(r'$\dot v$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltdotvt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###      Acerleração Yaw
###
#####################################   
        plt.plot(a[2][:, 0], a[2][:, 6] * (sp.array([180] / sp.pi), 'o-',
        a[5][:, 0], a[5][:, 1] * (180 / sp.pi), '-.'))
        
        plt.ylabel(r'$\dot r$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltdotrt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       Aceleração Roll
###
#####################################   
        plt.plot(a[2][:, 0], a[2][:, 4] * (sp.array([180]) / sp.pi), 'o-')#r 
        
        plt.ylabel(r'$\dot p$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltdotpt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
            
            
##
##
##       Força
##
##



####################################
##
##       Força de Surge
##
####################################        
        plt.plot(a[3][:, 0], a[3][:, 1], '--')
        plt.ylabel(r'$F_x$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltforsurget', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Força de Yaw
##
####################################
        plt.plot(a[3][:, 0], a[3][:, 2], 'g^')#v 
        plt.ylabel(r'$F_y$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltforswayt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###      Momento de Yaw
###
#####################################   
        plt.plot(a[3][:, 0], a[3][:, 4], 'o-', a[5][:, 0], a[5][:, 1] *
        (180 / sp.pi), '-.')        
        plt.ylabel(r'$N$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltNt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       Momento de Roll
###
#####################################   
        plt.plot(a[3][:, 0], a[3][:, 3], 'o-')#r 
        plt.ylabel(r'$K$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltKt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 



## ###################################
###
###       Rotação da Máquina
###
#####################################   
        plt.plot(a[6][:, 0], a[6][:, 1], 'o-')#r
        plt.ylabel(r'$n$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltnt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
            
## ###################################
###
###       Leme
###
#####################################   
        plt.plot(a[5][:, 0], a[5][:, 1] * (180/sp.pi), '-.')
        plt.ylabel(r'$\delta_R$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo +'pltlemet', format=formato)
            plt.clf()
        else: 
            plt.show()
            plt.clf() 
    def plotcg(self, save=True, tipoc='port', formato='eps', passo=0.5,
        tmax=200, tini=0, metodo='euler', TipoModelo='TP', GrausDeLib=4):
        """Plota curva de Giro
       
        Variáveis de entrada
        
        save (True/False) -- Opção para salvar as figuras ou somente mostrar 
        os gráficos, utilizar somente True até o momento;
        tipoc ('port'/'starboard') -- Opção para o tipo de curva de giro para
        bombordo o boreste;
        formato ('png'/'pdf'/'ps'/'eps'/'svg') -- formatos de saída da figura;
        passo (float) -- Paso de tempo da integração;
        tmax  (integer) -- Tempo  máximo;
        tini (integer) -- Tempo inicial;
        metodo ('euler') -- Método de integração;
        
        Salva as figuras  no diretório 
        './figuras/Curva_de_Giro/curva_de_giro'
        
        """
        
        DicionarioDerivadas = self.lerarqder()
        
        navio1 = navio(DicionarioDerivadas, Nome='Teste', Tipo=TipoModelo
)
        
        
        if tipoc == 'port':
            tipoc = 'Curva_de_Giro_port'
        else:
            tipoc = 'Curva_de_Giro_starboard'
            
        a = navio1.simula(met=metodo, t=tmax, t0=tini, dt=passo, tipo=tipoc,
        GrausDeLib=GrausDeLib)
        dir = './figuras/Curva_de_Giro/' + TipoModelo + '/' 
        os.makedirs(dir)
####################################
##
##       Posição y
##
####################################
        plt.plot(a[1][:, 2], a[1][:, 1], 'o')#v 

        plt.ylabel('X')
        plt.xlabel('Y')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'curva_de_giro', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()



####################################
##
##       Velocidade em Surge
##
####################################        
        plt.plot(a[0][:, 0], a[0][:, 1], 'bo')
        plt.ylabel(r'$u$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltut', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Velocidade em Sway
##
####################################
        plt.plot(a[0][:, 0], a[0][:, 2], 'g^')#v 

        plt.ylabel(r'$v$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltvt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
###################################
##
##       Velocidade de yaw
##
###################################   
        plt.plot(a[0][:, 0], a[0][:, 6] * (sp.array([180]) / sp.pi))
        
        plt.ylabel(r'$\dot\psi$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltvelyawt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
####################################
##
##       Velocidade de roll
##
####################################   
        plt.plot(a[0][:, 0], a[0][:, 4] * (sp.array([180]) / sp.pi), '--')#r 
        
        plt.ylabel('$\dot\phi$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltvelrollt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
            
####################################
##
##       Velocidade de Yaw
##
####################################   
        plt.plot(a[0][:, 0], a[0][:, 6] * (sp.array([180]) / sp.pi), '--')#r 
        
        plt.ylabel('$r$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltdotspsit', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()             
##
##
##       Posição
##
####################################
##
##       Posição x
##
####################################        
        plt.plot(a[1][:, 0], a[1][:, 1], '--')
        plt.ylabel(r'$x$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltxt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Posição y
##
####################################
        plt.plot(a[1][:, 0], a[1][:, 2], 'g^')#v 

        plt.ylabel(r'$y$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltyt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###       Posição Psi
###
#####################################   
        plt.plot(a[1][:, 0], a[1][:, 6] * (180 / sp.pi), 'o-', a[5][:,0],
        a[5][:, 1] * (180 / sp.pi), '-.')
        
        plt.ylabel(r'$\psi$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltyawt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       Orientação Roll
###
#####################################   
        plt.plot(a[1][:, 0], a[1][:, 4] * (sp.array([180]) / sp.pi), 'o-')#r 
        
        plt.ylabel(r'$\phi$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltrollt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 


##
##
##       Aceleração
##
##



####################################
##
##       dotu
##
####################################        
        plt.plot(a[2][:, 0], a[2][:, 1], '--')
        plt.ylabel(r'$\dot u$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltdotut', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       dot v
##
####################################
        plt.plot(a[2][:, 0], a[2][:, 2], 'g^')#v 

        plt.ylabel(r'$\dot v$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltdotvt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###      Acerleração Yaw
###
#####################################   
        plt.plot(a[2][:, 0], a[2][:, 6] * (sp.array([180]) / sp.pi), 'o-',
        a[5][:, 0], a[5][:, 1] * (180 / sp.pi), '-.')
        plt.ylabel(r'$\dot r$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltdotrt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       Aceleração Roll
###
#####################################   
        plt.plot(a[2][:, 0], a[2][:, 4] * (sp.array([180]) / sp.pi), 'o-')#r 
        
        plt.ylabel(r'$\dot p$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltdotpt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
            
            
##
##
##       Força
##
##



####################################
##
##       Força de Surge
##
####################################        
        plt.plot(a[3][:, 0], a[3][:, 1], '--')
        plt.ylabel(r'$F_x$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltforsurget', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
####################################
##
##       Força de Yaw
##
####################################
        plt.plot(a[3][:, 0], a[3][:, 2], 'g^')#v 

        plt.ylabel(r'$F_y$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltforswayt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()
    
## ###################################
###
###      Momento de Yaw
###
#####################################   
        plt.plot(a[3][:, 0], a[3][:, 4], 'o-', a[5][:, 0], a[5][:, 1] * 
        (180 / sp.pi ), '-.')        
        plt.ylabel(r'$N$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltNt', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf()        
            
## ###################################
###
###       Momento de Roll
###
#####################################   
        plt.plot(a[3][:, 0], a[3][:, 3], 'o-')#r 
        
        plt.ylabel(r'$K$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltKt', format=formato)
            plt.clf()
        else:
            plt.show()

## ###################################
###
###       Rotação da Máquina
###
#####################################   
        plt.plot(a[6][:, 0], a[6][:, 1], 'o-')#r 
        
        plt.ylabel(r'$n$')
        plt.xlabel(r'$t$')
        plt.title ('ZigZag10/10')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltnVert', format=formato)
            plt.clf()
        else:
            plt.show()
            plt.clf() 
## ###################################
###
###       Leme
###
#####################################   
        plt.plot(a[5][:, 0], a[5][:, 1] * (180/sp.pi), '-.')
        
        plt.ylabel(r'$\delta_R$')
        plt.xlabel(r'$t$')
        plt.title ('Curva de Giro')
        
        if save:
            plt.savefig(dir + TipoModelo + 'pltlemet', format=formato)
            plt.clf()
        else: 
            plt.show()
            plt.clf() 

    def setarqder(self, arq):
        """
        Entra com o caminho do arquivo de derivadas hidrodimâmicas.
        
        @return  :
        @author
        """
        
        self.arqder = arq
        pass
        
    def setarqtab(self, arq):
        """
         Entra com o caminho do arquivo de forças tabeladas.
         Não implementado na versão 191010.
        
        @return  :
        @author
        """
        
        self.arqtab = arq
        pass
        
    
    def setbd(self):
        """
        Entra com o caminho do banco de dados.
        Não implementado na versão 191010.
        @return  :
        @author
        """
        pass


    
    def conad(self, tipo='snae', var='beta', dic={}, vel=sp.array(0),
        r=sp.array(0), p=sp.array(0)):
        """
        Retorna o coeficiente de adimencionalisação
        
        Variáveis de entrada
        
        Tipo = 'snae' ou 'dmi'; 
        Default = 'snae'

        _
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        Fx = Forças em Surge 
        
        """
        den = dic['rho']
        L = dic['lpp']
        B = dic['b'] 
        T = (dic['df'] + dic['da'])/2
        
        saida = None
        if tipo == 'snae' or (tipo == 'dmi' and (var == 'beta' or 
        var == 'phi' or var == 'betaphi')):
            saida = sp.array(0.5*den*(vel*L)**2)
        elif tipo == 'dmi' and (var == 'gamma' or var == 'betagamma' or 
        var == 'gammaphi'):
            saida = sp.array(0.5*den*((vel +(r*L/2)**2)*L*T))
        elif tipo == 'dmi'and var =='epsilon':
            saida = sp.array(0.5 * den * ((vel +(T ** 2 + (B / 2) ** 2) * 
            (p)) ** 2) * L * T)#falta o elemento de área
        return saida
        
    def coefdertotab2 (self, dic, forge='fx', intervalo=5, coef='betagamma', 
        ConstAdOr='snae', ConstAdDes='dmi' ):
        """
        Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma tabela de forças em surge do tipo sp.array. 
        
        É necessário carregar um arquivo de derivadas em entrada [1].
        _
        Variáveis de entrada
        
        Intervalo = intervalo do ângulo beta em graus
        Default = 5.

        _
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        Fx = Forças em Surge 
        """
        
        navio1 = navio()
        navio1.dic= self.lerarqder()

        navio1.x = sp.array([[0.], [0.], [0.], [0.], [0.], [0.] ])
        navio1.dotx = sp.array([[dic['unom']], [0.], [0.], [0.], [0.], [0.]  ])
        navio1.angleme = sp.array([0.] )

        if  'beta' in coef:
            maxint1 = 1.
        else:
            maxint1 = 2.
        
        
        saida = sp.zeros([len( sp.arange(0., sp.pi / maxint1, intervalo * 
        sp.pi/180)) * len(sp.arange(0., sp.pi / 2., intervalo * sp.pi / 
        180)), 3])
        
        contlinha = 0
        for ang1 in sp.arange(0. , sp.pi/maxint1, intervalo* sp.pi/180):
            for ang2 in sp.arange(0. , sp.pi/2., intervalo* sp.pi/180):
                if   ConstAdOr =='snae':
                    coeforpf = self.conad(tipo='snae', dic=dic, vel=
                    dic['unom'])
                    coeforpm = coeforpf* dic[ 'lpp']
                if 'beta' in coef:
                    u = dic['unom']*sp.cos(ang1)
                    v = - dic['unom']*sp.sin(ang1)

                    navio1.dotx[0] = u
                    navio1.dotx[5] = v

                    coefdes = self.conad(tipo='dmi', var='beta', dic=dic, 
                    vel=dic['unom'])
                
                    if forge == 'fx':
                        f1 = sp.array( navio1.calcforcx() * 
                        (coeforpf /coefdes))
                    elif forge == 'fy':
                        f1 = sp.array( navio1.calcforcy() * (coeforpf/coefdes))
                    elif forge == 'k':
                        f1 = sp.array(ang, navio1.calck() * (coeforpm /
                        (coefdes * dic['lpp'])))
                    elif forge == 'n':
                        f1 = sp.array(ang, navio1.calcn() * (coeforpm /
                        (coefdes * dic['lpp'])))
                        
                    navio1.dotx[0] = dic['unom']
                    navio1.dotx[5] = 0.
                else:
#                    Caso gamma
                    r = sp.tan(ang1) * 2 * dic['unom'] / dic['lpp']
                    navio1.dotx[5] = r
                    coefdes = self.conad(tipo='dmi', var='gamma', dic=dic, 
                    vel=dic[ 'unom'], r = navio1.dotx[5])
                    
                    if forge == 'fx':
                        f1 = sp.array([ang, navio1.calcforcx() * (coeforpf /
                        coefdes)])
                    elif forge == 'fy':
                        f1 = sp.array([ang, navio1.calcforcy() * (coeforpf /
                        coefdes)])
                    elif forge == 'k':
                        f1 = sp.array([ang, navio1.calck() * (coeforpm /
                        (coefdes * dic['lpp']))])
                    elif forge == 'n':
                        f1 = sp.array([ang, navio1.calcn() * (coeforpm / 
                        (coefdes * dic['lpp']))])
                    
                    navio1.dotx[5]= 0.

#                    Caso phi
                    navio1.x[3] = ang2
                    coefdes = self.conad(tipo='dmi', var='gamma', dic=dic, 
                    vel=dic['unom'], r=navio1.dotx[5])

                    if forge == 'fx':
                        f2 = sp.array([ang, navio1.calcforcx() *
                        (coeforpf/coefdes)])
                    elif forge == 'fy':
                        f2 = sp.array([ang, navio1.calcforcy() *
                        (coeforpf/coefdes)])
                    elif forge == 'k':
                        f2 = sp.array([ang, navio1.calck() * (coeforpm /
                        (coefdes * dic['lpp']))])
                    elif forge == 'n':
                        f2 = navio1.calcn() * (coeforpm/(coefdes*dic['lpp']))
                    
#
#
                    navio1.dotx[5] = r
                    navio1.x[3]= ang2                        
                    if forge == 'fx':
                        saida[contlinha] = sp.array([ang1, and2,
                        navio1.calcforcx() * (coeforpf/coefdes) - (f1+f2)])
                    elif forge == 'fy':
                        saida[contlinha] = sp.array([ang1, and2, 
                        navio1.calcforcy() * (coeforpf/coefdes) - (f1+f2)])
                    elif forge == 'k':
                        saida[contlinha] = sp.array([ang1, and2, 
                        navio1.calck() * (coeforpm/(coefdes*dic['lpp'])) - 
                        (f1+f2)])
                    elif forge == 'n':
                        saida[contlinha] = sp.array([ang1, and2,
                        navio1.calcn() * (coeforpm/(coefdes*dic['lpp'])) - 
                        (f1+f2)])
                    
#               Procedimento de cálculo final

               
                
#                    Caso gamma
                if 'gamma' in coef:
                    r = sp.tan(ang1) * 2 * dic['unom'] / dic['lpp']
                    navio1.dotx[5] = r
                    
                    coefdes = self.conad(tipo = 'dmi', var = 'gamma', 
                    dic = dic, vel = dic['unom'], r = navio1.dotx[5])
                    
                    if forge == 'fx':
                        f2 = sp.array(navio1.calcforcx() * 
                        (coeforpf/coefdes))
                    elif forge == 'fy':
                        f2 = sp.array(navio1.calcforcy() * (coeforpf /
                        coefdes))
                    elif forge == 'k':
                        f2 = sp.array(navio1.calck() * (coeforpm / (coefdes *
                        dic['lpp'])))
                    elif forge == 'n':
                        f2 = sp.array(navio1.calcn() * (coeforpm / (coefdes *
                        dic['lpp'])))




#                  
#
                if 'phi' in coef:
#                    Caso phi
                    navio1.x[3] = ang2
                    coefdes = self.conad(tipo = 'dmi', var = 'gamma', dic =
                    dic, vel = dic['unom'], r = navio1.dotx[5])
                    if forge == 'fx':
                        f2 = sp.array(navio1.calcforcx() * (coeforpf/coefdes))
                    elif forge == 'fy':
                        f2 = sp.array( navio1.calcforcy() * (coeforpf/coefdes))
                    elif forge == 'k':
                        f2 = sp.array(navio1.calck() * (coeforpm / (coefdes *
                    dic['lpp'])))
                    elif forge == 'n':
                        f2 = sp.array(navio1.calcn() * (coeforpm / (coefdes *
                        dic['lpp'])))
                
#
#
                    navio1.dotx[0] = u
                    navio1.dotx[5] = v                       
                if forge == 'fx':
                    saida[contlinha] = sp.array([ang1, ang2, 
                    navio1.calcforcx() * (coeforpf / coefdes) - (f1+f2)])
                elif forge == 'fy':
                    saida[contlinha] = sp.array([ang1, ang2, 
                    navio1.calcforcy() * (coeforpf / coefdes) - (f1+f2)])
                elif forge == 'k':
                    saida[contlinha] = sp.array([ang1, ang2, navio1.calck() *
                    (coeforpm / (coefdes * dic['lpp'])) - (f1+f2)])
                elif forge == 'n':
                    saida[contlinha] = sp.array([ang1, ang2, navio1.calcn() *
                    (coeforpm / (coefdes * dic['lpp'])) - (f1 + f2)])
            contlinha += 1
            
        return saida
    
    def coefdertotab (self, dic, forge='fx', intervalo=5, coef='beta',
    coef2='gamma' , ConstAdOr='snae', ConstAdDes='dmi' ):
        """
        Transforma os valores de derivadas hidrodinâmicas em entrada[1]
        para uma tabela de forças em surge do tipo sp.array. 
        
        É necessário carregar um arquivo de derivadas em entrada [1].
        _
        Variáveis de entrada
        
        Intervalo = intervalo do ângulo beta em graus
        Default = 5.

        _
        Saída
        
        Saida é um sp.array[beta, Fx]):
        Beta - Ângulo de ataque
        Fx = Forças em Surge 
        """
        
        navio1 = navio()
        navio1.dic= self.lerarqder()

        navio1.x = sp.array([[0.], [0.], [0.], [0.], [0.], [0.] ])
        navio1.dotx = sp.array([[dic['unom']], [0.], [0.], [0.], [0.], [0.]  ])
        navio1.angleme = sp.array([0.] )

        if coef == 'beta':
            maxint = 1.
        else:
            maxint = 2.
        
        
        saida = sp.zeros([len( sp.arange(0. , sp.pi/maxint, intervalo*
sp.pi/180)), 2])
        
        contlinha = 0
        for ang in sp.arange(0. , sp.pi/maxint, intervalo* sp.pi/180):
            if   ConstAdOr =='snae':
                coeforpf = self.conad(tipo = 'snae', dic = dic, vel = dic[
'unom'])
                coeforpm = coeforpf* dic[ 'lpp']
            if coef =='beta':
                navio1.dotx[0] = dic['unom']*sp.cos(ang)
                navio1.dotx[1] = - dic['unom']*sp.sin(ang)
                
                coefdes = self.conad(tipo = 'dmi', var ='beta', dic = dic, 
vel= dic[ 'unom'])
                
            elif coef == 'gamma':
                navio1.dotx[5] = sp.tan(ang)*2*dic['unom']/dic['lpp']
                
                coefdes = self.conad(tipo = 'dmi', var = 'gamma', dic = dic, 
vel= dic[ 'unom'], r = navio1.dotx[5])
            
            elif coef == 'epsilon':
                navio1.dotx[3] = sp.tan(ang)*dic['unom'] / sp.sqrt((((dic['df']
+ dic['da'])/2)**2 + (dic['b']/2)**2))
            
                coefdes = self.conad(tipo = 'dmi', var = 'epsilon', dic =
dic, vel= dic[ 'unom'], p = navio1.dotx[3])
            
            elif coef == 'phi':
                navio1.x[3] = ang
                
                coefdes = self.conad(tipo = 'dmi', var = 'phi', dic = dic, 
vel= dic[ 'unom'])
                
            if forge == 'fx':
                saida[contlinha] = sp.array([ang, navio1.calcforcx() *
(coeforpf/coefdes)])
            elif forge == 'fy':
                saida[contlinha] = sp.array([ang, navio1.calcforcy() *
(coeforpf/coefdes)])
            elif forge == 'k':
                saida[contlinha] = sp.array([ang, navio1.calck() *
(coeforpm/(coefdes*dic['lpp']))])
            elif forge == 'n':
                saida[contlinha] = sp.array([ang, navio1.calcn() *
(coeforpm/(coefdes*dic['lpp']))])
            
            contlinha += 1
            
        return saida
    def plotcoefdertotab(self, formato = 'eps'):
        
        """
        """
        listf = [ 'fx', 'fy', 'k', 'n']
        listcoef = ['beta', 'gamma', 'epsilon', 'phi']
        
        dic = self.lerarqder()
        
        for f in listf:
           for  coef in listcoef:
                temp = self.coefdertotab (dic, forge = f, intervalo = 5, coef
= coef, ConstAdOr = 'snae', ConstAdDes = 'dmi' )
                plt.plot(temp[:, 0], temp[:, 1], 'g^')#v 
                plt.ylabel(f.capitalize())
                temp = '$\$ '
                plt.xlabel( temp.replace('$ ', coef + '$'))
                
                if 'f' in f:
                    plt.title ('Forca ' + f.capitalize() + ' Versus ' +
temp.replace('$ ', coef + '$'))
                else:
                    plt.title ('Momento ' + f.capitalize() + ' Versus ' +
temp.replace('$ ', coef + '$'))
                nomedoarq = './figuras/TabelaDmi/'+f +coef
                plt.savefig( nomedoarq , format=formato)
                plt.clf()

if __name__ == "__main__":
    import doctest
    doctest.testmod()                