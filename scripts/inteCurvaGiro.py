# -*- coding: utf-8 -*-


p = (Multbeta,  Multr,  Multl,  Multbrl)

if TipoModelo== 'MARAD':
    Arq =  './dados/MarAdinputder.dat'
elif   TipoModelo== 'TP':  
    Arq =  './dados/TPinputder.dat'



In = ('Navioteste', Arq, 'inputtab.dat')
io = es(entrada = In)

DicionarioDerivadas = io.lerarqder()
del io,  In,  Arq

navio1 = navio(DicionarioDerivadas, Nome = nome,   Tipo = TipoModelo )


b = navio1.getCurvaGiro(met = metodo, peso = p,  t = tmax, t0 = tini,dt=passo,
                        tipo= tipoc,  GrausDeLib = GrausDeLib,  
                        leme = LemeCom,  RotCom=Rot,  saida = saida)


if  saida == 'txt':
    os.chdir(scgarq)
    lemeHis = np.genfromtxt('leme.dat')
    propHis = np.genfromtxt('propulsor.dat')
    velHis = np.genfromtxt('velo.dat')
    velinHis = np.genfromtxt('veloiner.dat')
    etaHis = np.genfromtxt('Eta.dat')
    forHis = np.genfromtxt('forcas.dat')
    posHis = np.genfromtxt('pos.dat')
    acelHis = np.genfromtxt('acel.dat')
    betaHis = np.genfromtxt('beta.dat')
    os.chdir('..')    
    os.chdir('..')
    listacg = b
    del b
else:
    velHis, posHis,  acelHis, forHis,  velinHis,  lemeHis,  propHis,  EtaHis,  listacg,  betaHis = b
    del b
try:
  dircg = scgarq + '/figuras/Curva_de_Giro/' 
  os.makedirs(dircg)
except NameError:
  print 'houve algum problema na criação do diretório' + dircg


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
        
        for coluna in sp.arange( len(velHis[cont,  :])):
            if coluna == 0:
                velHis[cont, coluna] = velHis[cont, coluna]*(v/lpp)
            else:
                velHis[cont, coluna] = velHis[cont, coluna]*(1/v)
                if coluna > 3:
                    velHis[cont, coluna] = velHis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(acelHis[cont,  :])):
            if coluna == 0:
                acelHis[cont, coluna] = acelHis[cont, coluna]*(v/lpp)
            else:
                acelHis[cont, coluna] = acelHis[cont, coluna]*(lpp/v**2)
                if coluna > 3:
                    acelHis[cont, coluna] = acelHis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(posHis[cont,  :])):
            if coluna == 0:
                posHis[cont, coluna] = posHis[cont, coluna]*(v/lpp)
            else:
                posHis[cont, coluna] = posHis[cont, coluna]*(1/lpp)
                if coluna > 3:
                    posHis[cont, coluna] = posHis[cont, coluna]*(lpp)

        for coluna in sp.arange( len(forHis[cont,  :])):
            if coluna == 0:
                forHis[cont, coluna] = forHis[cont, coluna]*(v/lpp)
            else:            
                if coluna==1 or coluna ==2:
                    forHis[cont, coluna] = forHis[cont, coluna]*(2/(rho*lpp*(v**2)))
                elif coluna > 2:
                    forHis[cont, coluna] = forHis[cont, coluna]*(2/(rho*((lpp*v)**2)))
        cont += 1 

    listacg [0]['transfer'] = listacg [0]['transfer']*(1/lpp)
    listacg [0]['advance'] = listacg [0]['advance']*(1/lpp)
    listacg [0]['taticalDiameter'] = listacg [0]['taticalDiameter']*(1/lpp)
    
