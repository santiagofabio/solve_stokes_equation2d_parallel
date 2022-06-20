def avalia_derivada_funcao1_ksi (indice, ksi, eta):

 if  indice ==0 : #correto
     funcoes_0 =-0.25*(1-eta)
     return(funcoes_0)

 elif indice ==1: #Correto
     funcoes_1 =0.25*(1-eta)
     return(funcoes_1)

 elif indice ==2: #Correto
     funcoes_2 =0.25*(1+eta)
     return (funcoes_2)

 elif indice ==3: #Correto
     funcoes_3 =-0.25*(1+eta)
     return (funcoes_3)

