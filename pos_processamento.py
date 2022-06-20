import sys
import os
import numpy
import matplotlib.pyplot as plt 
import math

velocidade_u =numpy.loadtxt('velocidade_u.txt')
velocidade_v =numpy.loadtxt('velocidade_v.txt')

coordenadas_velocidade = numpy.loadtxt('coordenadas_velocidade.txt')
cordenadas_vx = coordenadas_velocidade[:,0]
cordenadas_vy = coordenadas_velocidade[:,1]
NNC = len(cordenadas_vx)
print(NNC)

vel_v_normalizada = numpy.zeros(NNC)
vel_u_normalizada = numpy.zeros(NNC)



for i in range(0,NNC):
       norma = math.sqrt(velocidade_u[i]*velocidade_u[i] + velocidade_v[i]*velocidade_v[i]) 
       if norma > 0.0:
             vel_u_normalizada[i] = velocidade_u[i]/norma
             vel_v_normalizada[i] = velocidade_v[i]/norma


x= []
y=[]
vx =[]
vy =[]
for i in range (0,NNC,10):
    x.append(cordenadas_vx[i] )
    y.append(cordenadas_vy[i] )
    vx.append( vel_u_normalizada[i]   )
    vy.append(vel_v_normalizada[i])

      
        




plt.figure()
plt.quiver(cordenadas_vx,cordenadas_vy,velocidade_u,velocidade_v, width=.001)
plt.show()