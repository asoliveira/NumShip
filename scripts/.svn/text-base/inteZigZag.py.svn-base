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

#navio1.MudaVel(sp.ones((6,1)))
#saida, fbeta, fr, fleme, fbetarl, fu = navio1.VetF((3,p))

listaz = navio1.getCurvaZigZag(met = metodo, peso = p,  t = tmax, t0 = tini,dt=passo,
                        tipo= tipoc,  GrausDeLib = GrausDeLib,  
                        leme = LemeCom, proa = Proa,   RotCom=Rot,  saida = saida)



if  saida == 'txt':
    os.chdir('./saida/ZigZag')
    lemeHis = np.genfromtxt('leme.dat')
    propHis = np.genfromtxt('propulsor.dat')
    velHis = np.genfromtxt('velo.dat')
    velinHis = np.genfromtxt('veloiner.dat')
    etaHis = np.genfromtxt('Eta.dat')
    forHis = np.genfromtxt('forcas.dat')
    posHis = np.genfromtxt('pos.dat')
    acelHis = np.genfromtxt('acel.dat')
    os.chdir('..')    
    os.chdir('..')

else:
    velHis, posHis,  acelHis, forHis,  velinHis,  lemeHis,  propHis,  etaHis,  listaz =a 
    del a
dirzz = './figuras/Curva_Zig_Zag/'
os.makedirs(dirzz)

if adi :
    cont = 0
    for linha in velHis:
        v = sp.sqrt(linha[1]**2 + linha[2]**2)
        rho = DicionarioDerivadas['rho']
        lpp =  DicionarioDerivadas['lpp']
        
        lemeHis[cont, 0] = lemeHis[cont, 0]*(v/lpp)
        propHis[cont, 0] = propHis[cont, 0]*(v/lpp)
        etaHis[cont, 0] = etaHis[cont, 0]*(v/lpp)
        
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
    for valor in sp.arange(len(listaz)):
        listaz[valor]['ospath'] = listaz[valor]['ospath']*(1/lpp)