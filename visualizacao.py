def visualizacao ():
     import sys 
     import os
     import numpy
     import matplotlib.pyplot as plt 
     import math
 
     velocidade_u=numpy.loadtxt('velocidade_u.txt')
     NNEV =len(velocidade_u)
     velocidade_v=numpy.loadtxt('velocidade_v.txt')
     cordenadas_vx2=numpy.loadtxt('coordenada_x2.txt')
     cordenadas_vy2=numpy.loadtxt('coordenada_y2.txt')

     vel_u_normalizada = numpy.zeros(NNEV)
     vel_v_normalizada = numpy.zeros(NNEV) 

    
     for i in range(0,NNEV):
          norma = math.sqrt(velocidade_u[i]*velocidade_u[i] + velocidade_v[i]*velocidade_v[i]) 
          vel_u_normalizada[i] = velocidade_u[i]/norma
          vel_v_normalizada[i] = velocidade_v[i]/norma

     plt.figure()
     plt.quiver(cordenadas_vx2,cordenadas_vy2,vel_u_normalizada, vel_v_normalizada)
     plt.show()
 
     return(0)