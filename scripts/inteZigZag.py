# -*- coding: utf-8 -*-

p = (Multbeta,  Multr,  Multl,  Multbrl)

#Coloque as derivadas no modelo nomeado pelo arquivo derivada.dat
arq = os.path.abspath('./dados/derivada.dat')
  
en = ('Navioteste', arq, 'inputtab.dat')
io = es(en)

DicionarioDerivadas = io.lerarqder()
del io,  en,  arq

navio1 = navio(DicionarioDerivadas, nome = nome,   tipo = TipoModelo )

#navio1.MudaVel(sp.ones((6,1)))
#saida, fbeta, fr, fleme, fbetarl, fu = navio1.VetF((3,p))

listaz = navio1.getCurvaZigZag(met = metodo, peso = p,  t = tmax, t0 = tini,dt=passo,
                        tipo= tipoc,  GrausDeLib = GrausDeLib,  
                        leme = lemezz, proa = proazz,   rotcom=Rot,  saida =
saida, arqs = scgarq)



if  saida == 'txt':
    os.chdir(scgarq)
    lemehis = np.genfromtxt('leme.dat')
    prophis = np.genfromtxt('propulsor.dat')
    velhis = np.genfromtxt('velo.dat')
    velinhis = np.genfromtxt('veloiner.dat')
    etahis = np.genfromtxt('eta.dat')
    forhis = np.genfromtxt('forcas.dat')
    poshis = np.genfromtxt('pos.dat')
    acelhis = np.genfromtxt('acel.dat')
    os.chdir('..')    
    os.chdir('..')

else:
    velhis, poshis, acelhis, forhis, velinhis, lemehis, prophis, \
    etahis, listaz = a 
    del a

if adi :
    cont = 0
    for linha in velhis:
        v = sp.sqrt(linha[1]**2 + linha[2]**2)
        rho = DicionarioDerivadas['rho']
        lpp =  DicionarioDerivadas['lpp']
        
        lemehis[cont, 0] = lemehis[cont, 0]*(v/lpp)
        prophis[cont, 0] = prophis[cont, 0]*(v/lpp)
        etahis[cont, 0] = etahis[cont, 0]*(v/lpp)
        
        prophis[cont, 1] = prophis[cont, 1]*(lpp/v)
        
        for coluna in sp.arange( len(velhis[cont,  :])):
            if coluna == 0:
                velhis[cont, coluna] = velhis[cont, coluna]*(v/lpp)
            else:
                velhis[cont, coluna] = velhis[cont, coluna]*(1/v)
                if coluna > 3:
                    velhis[cont, coluna] = velhis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(acelhis[cont,  :])):
            if coluna == 0:
                acelhis[cont, coluna] = acelhis[cont, coluna]*(v/lpp)
            else:
                acelhis[cont, coluna] = acelhis[cont, coluna]*(lpp/v**2)
                if coluna > 3:
                    acelhis[cont, coluna] = acelhis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(poshis[cont,  :])):
            if coluna == 0:
                poshis[cont, coluna] = poshis[cont, coluna]*(v/lpp)
            else:            
                poshis[cont, coluna] = poshis[cont, coluna]*(1/lpp)
                if coluna > 3:
                    poshis[cont, coluna] = poshis[cont, coluna]*(lpp)
        for coluna in sp.arange( len(forhis[cont,  :])):
            if coluna == 0:
                forhis[cont, coluna] = forhis[cont, coluna]*(v/lpp)
            else:            
                if coluna==1 or coluna ==2:
                    forhis[cont, coluna] = forhis[cont,
coluna]*(2/(rho*lpp*(v**2)))
                elif coluna > 2:
                    forhis[cont, coluna] = forhis[cont,
coluna]*(2/(rho*((lpp*v)**2)))
        cont += 1 
    for valor in sp.arange(len(listaz)):
        listaz[valor]['ospath'] = listaz[valor]['ospath']*(1/lpp)