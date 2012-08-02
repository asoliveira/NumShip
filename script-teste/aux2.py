# -*- coding: utf-8 -*-

#Este script plota o valor da velocidade no leme ud de acordo com u. Todo o
#módelo e os dados são do MARAD

import scipy as sp
import matplotlib.pyplot as plt

dv = {}

d = 0.26
e = 0.22
f = -0.001
dp = 10.05
intervalo = 5
vel = 12.7
Rot = 0.62
Eta = sp.array([1.])

u = sp.zeros(180/intervalo)
ud = sp.zeros(180/intervalo)
contlin = 0
for beta in sp.linspace(0. , sp.pi/2, 90/intervalo):
    u[contlin] = sp.array([vel]) * sp.cos(beta)
    ud[contlin] = sp.sqrt(d * (u[contlin] **  2) + e * u[contlin] * Rot *  
                          dp + f * (Rot * dp) ** 2)
    contlin += 1
print 'este é u', u
print 'este é ud', ud

plt.clf()    
plt.plot(u, ud)
plt.show()

#Verificar este valor 12,7 pois ele parece dizer respeito a
#velocidade. Sendo este o caso, talvez seja necessário colocar ele
#como parâmetro de entrada para dar mais flexibilidade ao código.