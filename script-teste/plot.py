import os
import sys
sys.path.insert(0, os.path.abspath('../source'))

import scipy as sp
import matplotlib.pyplot as plt

import Es

entrada = ('NavioTeste', '../dados/bemformatado.dat', 'inputtab.dat')
en = Es.es(entrada)

en.plotfxb()