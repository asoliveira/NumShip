  def openlogfile():
    """Abre arquivos de log
    
    return: Retorma uma tupla com 9 elementos.
    """
    lemehis = open('leme.dat', 'w')#histórico do leme
    lemehis.write('#Navio {nome}\n'.format(nome=self.nome))
    lemehis.write('#Valor do leme em rad\n')
    lemehis.write('#{0:<5}{1:<7}\n'.format('tempo', 'leme'))

    velohis = open('velo.dat', 'w') #histórico da velocidade
    velohis.write('#Navio {nome}\n'.format(nome=self.nome))
    velohis.write('#Velocidade Sistema Solidário  \n#\n')
    velohis.write('#{0:<5}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
    'tempo', 'u', 'v', 'w', 'p', 'q', 'r')) 

    veloinerhis = open('veloiner.dat','w')#histórico da velocidade no
    #sistema inercial. Verificar depois a necessidade
    veloinerhis.write('#Navio {nome}\n'.format(nome=self.nome))
    veloinerhis.write('#Velocidade Inercial\n#\n')
    veloinerhis.write('#{0:<5}{1:<11}{2:<11}{3:<11}\n'.format('tempo','u',
    'v', 'r')) 

    poshis = open('pos.dat', 'w')#histórico da posição
    poshis.write('#Navio {nome}\n'.format(nome=self.nome))
    poshis.write('#Posição e Orientação\n#\n')
    poshis.write('#{0:<5}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
'tempo', 'x', 'y', 'z', 'pitch', 'roll', 'yaw')) 

    fhis = open('forcas.dat', 'w') #histórico de forças
    fhis.write('#Navio {nome}\n'.format(nome=self.nome)) 
    fhis.write('#Forças e Momentos\n#\n')
    fhis.write('#{0:<5}{1:<11}{2:<11}{3:<11}{4:<11}\n'.format('tempo', 'X',
'Y', 'K', 'N')) 

    acelhis = open('acel.dat', 'w') #histórico de acelerações
    acelhis.write('#Navio {nome}\n'.format(nome=self.nome))
    acelhis.write('#Aceleração\n#\n')
    acelhis.write('#{0:<5}{1:<11}{2:<11}{3:<11}{4:<11}{5:<11}{6:<11}\n'.format(
    'tempo', 'dot u', 'dot v', 'dot w', 'dot pitch', 'dot roll', 'dot yaw')) 

    prophis = open('propulsor.dat', 'w')#histórico Máquina
    prophis.write('#Navio {nome}\n'.format(nome=self.nome))
    prophis.write('#Rotações do propulsor\n#\n')
    prophis.write('#{0:<5}{1:<8}\n'.format('tempo', 'rotações'))

    etahis = open('eta.dat', 'w') #histórico eta
    etahis.write('#Navio {nome}\n'.format(nome=self.nome))
    etahis.write('#eta \n#\n')
    etahis.write('#{0:<5}{1:<8}\n'.format('tempo', 'eta'))

    betahis = open('beta.dat', 'w') #histórico eta
    betahis.write('#Navio {nome}\n'.format(nome=self.nome))
    betahis.write('#Beta \n#\n')
    betahis.write('#{0:<5}{1:<8}\n'.format('tempo', 'beta'))
    
    return (lemehis, velohis, veloinerhis, poshis, fhis, acelhis, prophis,
etahis, betahis)
   
  def getCurvaGiro (self, peso=None, met='euler', t0=0., dt=0.5, t=100.,
                    GrausDeLib=3, tipo='port', leme=sp.array(20.), 
                    rotcom=None, velcom= None, vel=None, eta='vel',
                    posine=None, arqs='saida'):
    r"""Simula manobras de Curva de Giro.
    
    :param GrausDeLib: Graus de liberdade de modelo matemático;
    :param met: Método de integração. (default = euler);
    :param t0: Tempo inicial;
    :param dt: Passo no tempo;
    :param t: Tempo final;
    :param leme: Ângulo do leme em graus;
    :param arqs: Nome do arquivo de saída;
    :param rotcom: Comando de rotação do propulsor[opcional];
    :param velcom: Comando de velocidade da embarcação[opcional];
    :param vel: Velocidade da embarcação[opcional];
    :return: Uma tupla (velohis, poshis, acelhis, fhis, veloinerhis, lemehis,
             prophis, etahis, dados, betahis)
             Em cada elemento da tupla a primeira coluna é o passo de tempo e
             as demais são as variáveis:
             * velohis -- histórico de velocidades;
             * poshis -- histórico de posições;
             * acelhis --- histórico de acelerações;
             * fhis -- histórico de forças;
             * veloinerhis -- histórico de velocidades no sistema inercial;
             * lemehis -- histórico do comando de leme.
             Ou simplesmente cria arquivos `txt` no diretório indicado na
             entrada com todos este valores
    :type GrausDeLib: int
    :type met: str
    :type t0: float;
    :type dt: float;
    :type t: float;
    :type leme: numpy.ndarray;
    :type arqs: str
    :type rotcom: numpy.ndarray
    :type velcom: numpy.ndarray
    :type vel: numpy.ndarray
    :rtype: tuple, file
    
    """
    
    if rotcom == None:
      rotcom = self.dic['rotnom']
    if velcom == None:
      velcom = self.dic['unom']
    if vel == None:
      vel = sp.zeros((6,1))
      vel[0] = self.dic['unom']
    if posine == None:
      posine = sp.zeros((6,1)) 
    
    self.MudaPos(posine)
    self.MudaVel(vel)
    self.MudaRotCom(rotcom)
    self.MudaVelCom(velcom)
    
    if tipo == 'port':
      self.MudaLemeCom(sp.array(leme*sp.pi/180))
    elif tipo == 'starboard':
      self.MudaLemeCom(sp.array(-leme*sp.pi/180))

    if os.path.exists(arqs):
      os.rename(arqs, arqs + '2')
    os.makedirs(arqs)
    os.chdir(arqs)
    (lemehis, velohis, veloinerhis, poshis, fhis, acelhis, prophis,
etahis, betahis) = self.openlogfile() #cria arquivos para log
    os.chdir('../..')      
    
    dados = []
    dic = {}
    posini = self.MostraPos().copy()          
    cont =0 #Contador
    
    #iteração
    for tp in sp.arange(t0, t, dt):
      if cont == 0:
        V1 = sp.sqrt(self.MostraVel()[0]**2 +
              self.MostraVel()[1]**2 + self.MostraVel()[2]**2)
      elif cont == 1:
        V2 = sp.sqrt(self.MostraVel()[0]**2 +
              self.MostraVel()[1]**2 + self.MostraVel()[2]**2)
      elif cont == 2:
        V3 = sp.sqrt(self.MostraVel()[0]**2 +
              self.MostraVel()[1]**2 + self.MostraVel()[2]**2)
      elif cont == 3:
        V4 = sp.sqrt(self.MostraVel()[0]**2 +
              self.MostraVel()[1]**2 + self.MostraVel()[2]**2)
      else:
        V1 = V2
        V2 = V3
        V3 = V4
        V4 = sp.sqrt(self.MostraVel()[0]**2 +
              self.MostraVel()[1]**2 + self.MostraVel()[2]**2)
                    
      if peso == None:
        par =   (GrausDeLib, )
      else:
        par = (GrausDeLib, peso)
      
      ft = self.VetF(par)
      MatRot = self.MatRot()
      VelIn = sp.array(MatRot*self.MostraVel()[0:3])
      posine = self.MostraPos()[0:3]
      vel = self.MostraVel()

      #Guardando os parâmetros
      #Velocidade Inercial
      if saida == 'txt':
        veloinerhis.write('{6: .2f}'.format(tp))
        for arg in VelIn:
          veloinerhis.write('{0:< .5e}'.format(arg))
        veloinerhis.write('\n')
      elif saida == 'mem':
        d = sp.hstack(VelIn)
        veloinerhis[cont, 1:] = d #
        veloinerhis[cont, 0] = tp #

      #histórico Leme
      if saida == 'txt':
        lemehis.write('%.2f'.rjust(5)%(tp) + ' ')
        lemehis.write('%.2f'.rjust(5)%(self.MostraLeme()) + '\n')
      elif saida == 'mem':
        lemehis[cont, 0] = tp
        lemehis[cont, 1] = self.MostraLeme()
      
      #histórico da posição
      if saida == 'txt':
        poshis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in self.MostraPos():
          poshis.write('%.5e'.rjust(11)%(arg) + ' ')
        poshis.write('\n')
      elif saida == 'mem':            
        temp = sp.hstack(self.MostraPos())
        poshis[cont, :] = sp.hstack((tp, temp))
        del temp
      
      #histórico da Velocidade
      if saida == 'txt':
        velohis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vel:
          velohis.write('%.5e'.rjust(11)%(arg) + ' ')
        velohis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(self.MostraVel())
        velohis[cont, :] = sp.hstack((tp, temp))
        del temp
        
      #histórico das Forças 
      if saida == 'txt':
        temp = sp.zeros((4, 1))
        if GrausDeLib == 4:
          temp = ft
        elif GrausDeLib == 3:
          temp[:2]  = ft[:2]
          temp[3]  = ft[2]
        fhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in temp:
          fhis.write('%.5e'.rjust(11)%(arg) + ' ')
        fhis.write('\n')
      elif saida == 'mem': 
        temp = sp.hstack(sp.array(ft))
        if GrausDeLib == 4:
          fhis[cont, :] = sp.hstack((tp, temp))
        elif GrausDeLib == 3:
          fhis[cont, :3] = sp.hstack((tp, temp[:2]))
          fhis[cont, 4] = temp[2]
      del temp

      #histórico Propulsor
      if saida == 'txt':
        prophis.write('%.2f'.rjust(5)%(tp) + ' ')
        prophis.write('%.2f'.rjust(5)%self.MostraRot() + '\n')
      elif saida == 'mem':
        prophis[cont, :] = sp.hstack((tp, self.MostraRot()))
        
      #histórico eta
      if saida == 'txt':
        etahis.write('%.2f'.rjust(5)%(tp) + ' ')
        if eta == 'rot':
          etahis.write('%.2f'.rjust(5) % (self.MostraRotCom() /
                                          self.MostraRot()) + '\n')
        elif eta == 'vel':
          etahis.write('%.2f'.rjust(5) % (self.MostraVelCom() /
                                          self.MostraVel()[0]) + '\n')
      elif saida == 'mem':
        if eta == 'rot':
          etahis[cont, :] = sp.hstack((tp, self.MostraRotCom() /
                                       self.MostraRot()))
        elif eta == 'vel':
          etahis[cont, :] = sp.hstack((tp, self.MostraVelCom() /
                                       self.MostraVel()[0]))

      #histórico Beta
      if saida == 'txt':
        betahis.write('%.2f'.rjust(5) % (tp) + ' ')
        betahis.write(('%.2f'.rjust(5) % sp.arctan(-self.MostraVel()[1] /
                       self.MostraVel()[0])) + '\n')  
      elif saida == 'mem':
        betahis[cont, :] = sp.hstack((tp, sp.arctan(-self.MostraVel()[1] / 
                                      self.MostraVel()[0])))

      #histórico das Acelerações 
      Acel = self.f2(ft, self.H(GrausDeLib))
      vetor = sp.zeros((6, 1))
      if GrausDeLib == 4:
        vetor[:2] = Acel[:2]
        vetor[3] = Acel[2]
        vetor [5] = Acel[3]
      elif GrausDeLib == 3:
        vetor[:2] = Acel[:2]
        vetor [5] = Acel[2]
      if saida == 'txt':
        acelhis.write('%.2f'.rjust(5)%(tp) + ' ')
        for arg in vetor:
          acelhis.write('%.5e'.rjust(11)%(arg[0]) + ' ')
        acelhis.write('\n')
      elif saida == 'mem':  
        acelhis[cont, :] = sp.hstack((tp, sp.hstack(vetor)))       
      #Criação do vetor de graus de liberdade
      if GrausDeLib == 4:
        vt = sp.zeros((6, 1))
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[3]
        vt [3] = self.MostraVel()[5]
        vt [4] = self.MostraPos()[3]
        vt [5] = self.MostraPos()[5]
      elif  GrausDeLib == 3:
        vt = sp.zeros((4, 1))
        vt [0] = self.MostraVel()[0]
        vt [1] = self.MostraVel()[1]
        vt [2] = self.MostraVel()[5]
        vt [3] = self.MostraPos()[5]         
      #integração da aceleração solidária
      if met == 'euler':
        vt = self.integrador.euler(self.f, vt, tp, dt, par)
      elif met =='rk4':
        vt = self.integrador.rk4(self.f, vt, tp, dt, par)
      
      if GrausDeLib == 4:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1] 
        v[3] = vt[2]
        v[5] = vt[3]
      elif GrausDeLib == 3:
        v = sp.zeros((6, 1))
        v[0] = vt[0] 
        v[1] = vt[1]
        v[5] = vt[2]                
      self.MudaVel(v)               

      del v
      #integração da velocidade inercial
      x = sp.zeros((6, 1))
      if met == 'euler':
        x[:3] = self.integrador.euler(self.fvein ,
                      self.MostraPos()[:3], tp, dt ,
                      (self.MostraPos()[3:] ,
                      self.MostraVel()[:3]))
      elif met == 'rk4':
        x[:3] = self.integrador.rk4(self.fvein, self.MostraPos()[:3],
                      tp, dt, (self.MostraPos()[3:],
                      self.MostraVel()[:3]))

      if GrausDeLib == 4:
        x[3] = vt[4]
        x[5] = vt[5]
      elif GrausDeLib == 3:
        x[5] = vt[3]
        
      self.MudaPos(x)
      
      del x
      cont += 1
      self.prop.MudaRot(tp)
      self.leme.MudaLeme(tp)
    if saida == 'txt':
      arq = (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
             etahis)
      for arg in arq:
        arg.close()
      return dados
    elif saida == 'mem':
      return (velohis, poshis, acelhis, fhis, veloinerhis, lemehis, prophis,
              etahis, betahis, dados)