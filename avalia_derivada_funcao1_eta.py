def avalia_derivada_funcao1_eta (indice, ksi, eta):
 import numpy


 if  indice ==0 : #Correto
     derivada_funcao_eta_0 =-0.25*(1-ksi)
     return(derivada_funcao_eta_0)

 elif indice ==1: #Correto
     derivada_funcao_eta_1 =-0.25*(1+ksi)
     return(derivada_funcao_eta_1)


 elif indice ==2: #Correto
     derivada_funcao_eta_2 =0.25*(1+ksi)
     return(derivada_funcao_eta_2)

 elif indice ==3:#Correto
     derivada_funcao_eta_3 =0.25*(1-ksi)
     return(derivada_funcao_eta_3)

 