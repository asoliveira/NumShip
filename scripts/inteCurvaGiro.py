# -*- coding: utf-8 -*-

import os

#Multiplicador para a força
p = (Multbeta, Multr, Multl, Multbrl)

#Dependenpo do modelo que esteja usando temos que colocar os dados de entrada
#nos arquivos na pasta dados
if TipoModelo == 'MARAD':
    arq = os.path.abspath('./dados/marad_derivada.dat')
elif   TipoModelo == 'TP':  
    arq = os.path.abspath('./dados/tp_derivada.dat')
else:
  arq = os.path.abspath('./dados/derivada.dat')

entrada = ('Navioteste', arq, 'inputtab.dat')
io = es(entrada)

DicionarioDerivadas = io.lerarqder()
del io, entrada, arq

navio1 = navio(DicionarioDerivadas, nome = nome,  tipo = TipoModelo )


b = navio1.getCurvaGiro(met = metodo, peso = p, t = tmax, t0 = tini, 
                        dt = passo, tipo = tipoc, GrausDeLib = GrausDeLib, 
                        leme = lemecg, rotcom = Rot, saida = saida, 
                        arqs = scgarq)


if  saida == 'txt':
    os.chdir(scgarq)
    lemeHis = np.genfromtxt('leme.dat')
    propHis = np.genfromtxt('propulsor.dat')
    velHis = np.genfromtxt('velo.dat')
    velinHis = np.genfromtxt('veloiner.dat')
    etaHis = np.genfromtxt('eta.dat')
    forHis = np.genfromtxt('forcas.dat')
    posHis = np.genfromtxt('pos.dat')
    acelHis = np.genfromtxt('acel.dat')
    betaHis = np.genfromtxt('beta.dat')
    os.chdir('..')    
    os.chdir('..')
    listacg = b
    del b
else:
    velHis, posHis, acelHis, forHis, velinHis, lemeHis, propHis, EtaHis, \
    listacg, betaHis = b
    del b

if adi :
    cont = 0
    for linha in velHis:
        v = sp.sqrt(linha[1]**2 + linha[2]**2)
        rho = DicionarioDerivadas['rho']
        lpp = DicionarioDerivadas['lpp']
        
        lemeHis[cont, 0] = lemeHis[cont, 0]*(v/lpp)
        propHis[cont, 0] = propHis[cont, 0]*(v/lpp)
        etaHis[cont, 0] = etaHis[cont, 0]*(v/lpp)
        betaHis[cont, 0] = betaHis[cont, 0]*(v/lpp)
        
        propHis[cont, 1] = propHis[cont, 1]*(lpp/v)
        
        for coluna in sp.arange( len(velHis[cont, :])):
            if coluna == 0:
                velHis[cont, coluna] = velHis[cont, coluna]*(v/lpp)
            else:
                velHis[cont, coluna] = velHis[cont, coluna]*(1/v)
                if coluna > 3:
                    velHis[cont, coluna] = velHis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(acelHis[cont, :])):
            if coluna == 0:
                acelHis[cont, coluna] = acelHis[cont, coluna]*(v/lpp)
            else:
                acelHis[cont, coluna] = acelHis[cont, coluna]*(lpp/v**2)
                if coluna > 3:
                    acelHis[cont, coluna] = acelHis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(posHis[cont, :])):
            if coluna == 0:
                posHis[cont, coluna] = posHis[cont, coluna]*(v/lpp)
            else:
                posHis[cont, coluna] = posHis[cont, coluna]*(1/lpp)
                if coluna > 3:
                    posHis[cont, coluna] = posHis[cont, coluna]*(lpp)

        for coluna in sp.arange( len(forHis[cont, :])):
            if coluna == 0:
                forHis[cont, coluna] = forHis[cont, coluna]*(v/lpp)
            else:            
                if coluna==1 or coluna ==2:
                    forHis[cont, coluna] = forHis[cont, coluna]*(2/(rho*lpp*(v**2)))
                elif coluna > 2:
                    forHis[cont, coluna] = forHis[cont, coluna]*(2/(rho*((lpp*v)**2)))
        cont += 1 

    listacg[0]['transfer'] = listacg[0]['transfer']*(1/lpp)
    listacg[0]['advance'] = listacg[0]['advance']*(1/lpp)
    listacg[0]['taticalDiameter'] = listacg[0]['taticalDiameter']*(1/lpp)
    
