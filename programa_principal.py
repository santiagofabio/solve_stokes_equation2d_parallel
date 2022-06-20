import sys
import os

import numpy
from resolve_equacao_stokes import resolve_equacao_stokes 
from imprime_matriz import imprime_matriz
from  monta_sub_matrizes_global_viscosas import  monta_sub_matrizes_global_viscosas
from  monta_sub_matrizes_global_pressao import  monta_sub_matrizes_global_pressao
from monta_sistema_global import monta_sistema_global
from conta_nos import conta_nos
import matplotlib.pyplot as plt 
from scipy.sparse import csc_matrix ,hstack
from scipy.sparse.linalg import spsolve
from visualizacao import visualizacao 
from monta_torres import monta_torres
from joblib import delayed
from joblib import Parallel
import math
import time 

os.system('cls')

start = time.time() 
print("****INICIO EXECUSSAO*****")

from scipy import linalg

# Parametroz fisicos
alpha =1.0


# Componnetes da velocidade 
conenctividade =numpy.loadtxt('conectividade.txt')
conectividade_interna =numpy.loadtxt('conectividade_interna.txt')
coordenadas_velocidade = numpy.loadtxt('coordenadas_velocidade.txt')
vetor_id =numpy.loadtxt('vetor_id.txt')

#Informações sobre o contorno de velocidade 
contorno_u =numpy.loadtxt('contorno_u.txt')
contorno_v =numpy.loadtxt('contorno_v.txt')
#configura coordenadas velocidade 
cordenadas_vx = coordenadas_velocidade[:,0]
cordenadas_vy = coordenadas_velocidade[:,1]

#Dimesnoes do Sistema Global
NEFT, NNEV = conenctividade.shape


NNT = len(cordenadas_vx )
NND = conta_nos(vetor_id,-1)
NNEVT =NNT -NND

vetor_f1 =numpy.zeros((NNEVT))
vetor_f2 =numpy.zeros((NNEVT))

print(f'Numeros de nós Dirichilet {NND}')
print (f' Informações elmento de velocidade')
print(f'Numero total de Elementos finitos {NEFT} , NNNEV {NNEV} , NNEVT {NNEVT} ')
#********************************************************************************



#Componnetes de Pressao 
conectividade_pressao =numpy.loadtxt('conectividade_pressao.txt')
#coordenadas_pressao = numpy.loadtxt('coordenadas_pressao.txt')
#configura coordenadas pressao 
#coordenadas_px = coordenadas_pressao[:,0]
#coordenadas_py = coordenadas_pressao[:,1]


NETP,NNEP =conectividade_pressao.shape
NNEPT=  753
vetor_p = numpy.zeros(NNEPT)
print (f' Informações elmento de pressao')
print(f'Numero total de Elementos finitos {NETP} , NNNEP {NNEP} , NNEPT{NNEPT} ')

print(conectividade_pressao.shape)


#*******************************************************************************




#***************************************************************
k_torre_elmento = numpy.zeros((7,NNEP,NNEV), dtype=numpy.longdouble)
#**************************************************************
k_pilha =[]
print(f'****Processamento dos elementos***** ')
# inicio do calculos sobre a malha

k_pilha = Parallel(n_jobs = -1 )(delayed(resolve_equacao_stokes)(elemento,conenctividade,conectividade_pressao,cordenadas_vx, cordenadas_vy,alpha,NNEV,NNEP,k_pilha) for elemento in range(0,NEFT) )

print(f'{k_pilha[0][0][1][0][0]}')

k11_torre,k12_torre,k13_torre,k21_torre,k22_torre,k23_torre,k31_torre,k32_torre = monta_torres(k_pilha, NNEV, NNEP,NEFT)




       
    
    






print(f'*** Fim processamento elementos*******')                                                                                                                                                                                     


print(f'Montagem matri global viscosa')
k11_global, k12_global,k21_global,k22_global,vetor_f1,vetor_f2 = monta_sub_matrizes_global_viscosas (conectividade_interna,conenctividade,contorno_u, contorno_v, vetor_f1,vetor_f2, k11_torre,k12_torre,k21_torre,k22_torre,NNEV,NEFT,NNEVT)

print(f'Montagem matri global pressão')
k13_global,k23_global,k31_global, k32_global,k33_global,vetor_f3 = monta_sub_matrizes_global_pressao(conectividade_interna,conenctividade,conectividade_pressao,contorno_u, contorno_v,k13_torre,k23_torre,k31_torre,k32_torre,NNEV,NNEP,NEFT,NNEVT,NNEPT) 



print(f'Montagem sistema global')
KGLOBAL,VETOR_B = monta_sistema_global(k11_global, k12_global,k13_global,k21_global,k22_global,k23_global,k31_global,k32_global,k33_global, vetor_f1, vetor_f2, vetor_f3)
print(f'Sistema global finalizado')

print(f'Resolucao do sistema linear')
solucao= spsolve(KGLOBAL,VETOR_B)
print(f'Sistema linear resolvido')


print(f'************FIM DA EXECUSSAÃO*******************')

velocidade_u =numpy.zeros(NNT)
velocidade_v =numpy.zeros(NNT)

for elemento in range(0,NEFT):
       for linha in range (0, NNEV):
             no_local = int (conectividade_interna[elemento][linha])
             if no_local !=-1:
                    no_global =int (conenctividade[elemento][ linha])
                    contorno_u[no_global] =solucao[no_local]
                    contorno_v[no_global] =solucao[no_local+NNEVT]
                                  
                  




velocidade_u= contorno_u
velocidade_v= contorno_v

vel_u_normalizada = numpy.zeros(NNT)
vel_v_normalizada = numpy.zeros(NNT) 
arquivo_vel_u = open('velocidade_u.txt', 'w')
arquivo_vel_v = open('velocidade_v.txt', 'w')

for i in range(0,NNT):
        arquivo_vel_u.write(f' {float(velocidade_u[i])}   ')
        arquivo_vel_v.write(f'{float(velocidade_v[i])} ')
        arquivo_vel_u.write('\n')
        arquivo_vel_v.write('\n')

arquivo_vel_u.close()
arquivo_vel_v.close()




vel_u_normalizada = numpy.zeros(NNEVT+NND)
vel_v_normalizada = numpy.zeros(NNEVT+NND) 
end = time.time() 

print(f'{end - start}')

for i in range(0,NNT):
       norma = math.sqrt(velocidade_u[i]*velocidade_u[i] + velocidade_v[i]*velocidade_v[i]) 
       if norma != 0.0:
             vel_u_normalizada[i] = velocidade_u[i]/norma
             vel_v_normalizada[i] = velocidade_v[i]/norma

plt.figure()
plt.quiver(cordenadas_vx,cordenadas_vy,velocidade_u,velocidade_v)
plt.show()


