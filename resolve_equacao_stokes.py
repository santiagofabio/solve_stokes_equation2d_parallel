def resolve_equacao_stokes (elemento,matriz_vel,matriz_pressao,cordenadas_x, cordenadas_y,alpha,NNEV,NNEP,k_pilha):
                           
    import math 
    import numpy
    from joblib import Parallel
    from calcula_termo_difusivo import calcula_termo_difusivo
    from avalia_funcao import avalia_funcao
    from  calcula_elementos_pressao import calcula_elementos_pressao
    from calcula_produto_misto_velocidade import calcula_produto_misto_velocidade 

    
    k11_elemento = numpy.zeros((NNEV, NNEV)) 
    k12_elemento = numpy.zeros((NNEV, NNEV))
    k13_elemento = numpy.zeros((NNEV, NNEP))
    k21_elemento = numpy.zeros((NNEV, NNEV))
    k22_elemento = numpy.zeros((NNEV, NNEV))
    k23_elemento = numpy.zeros((NNEV, NNEP))
    k31_elemento = numpy.zeros((NNEP, NNEV))
    k32_elemento = numpy.zeros((NNEP, NNEV))
    
    
    

    
    #Coordenadas elementos de velocidade
    elemento_coord_x = numpy.zeros(NNEV)
    elemento_coord_y = numpy.zeros(NNEV)

    #Coordenadas elementos pressao
    pressao_coord_x = numpy.zeros(NNEP)
    pressao_coord_y = numpy.zeros(NNEP)
    


    for  i in range(0,NNEV):
        no = int(matriz_vel[elemento,i]) 
        elemento_coord_x[i]= float(cordenadas_x[no])
        elemento_coord_y[i]= float(cordenadas_y[no])



    for  i in range(0,NNEP):
        no = int (matriz_pressao[elemento,i])
        pressao_coord_x[i]= float(cordenadas_x[no])
        pressao_coord_y[i]= float(cordenadas_y[no])
        
    matriz_difusivo_ksi,matriz_difusivo_eta = calcula_termo_difusivo( elemento_coord_x, elemento_coord_y,NNEV, NNEV, NNEV)
    #matriz_difusivo_ksi-> Correto
    #matriz_difusivo_eta -> Correto



    k11_elemento[:,:] = 2.0*alpha*matriz_difusivo_ksi + alpha*matriz_difusivo_eta      
    k22_elemento[:, :] = alpha*matriz_difusivo_ksi +2.0*alpha*matriz_difusivo_eta

    

    

    matriz_velocidade_deta_dksi,matriz_velocidade_dksi_deta  = calcula_produto_misto_velocidade( elemento_coord_x, elemento_coord_y, NNEV, NNEV,NNEV)  
    
    # matriz_velocidade_deta_dksi -Correto 
    #matriz_velocidade_dksi_deta - Correto
  
    
   # k12_torre[elemento, : ,: ] =alpha*matriz_velocidade_deta_dksi
   # k21_torre[elemento,:,:] = alpha*matriz_velocidade_dksi_deta

    k12_elemento[:,:] =alpha*matriz_velocidade_deta_dksi
    k21_elemento[:,:] = alpha*matriz_velocidade_dksi_deta

   
    matriz_pressao_ksi,matriz_pressao_eta = calcula_elementos_pressao(elemento_coord_x, elemento_coord_y, NNEV,NNEP)
    # matriz_pressao_ksi - Correto
   # matriz_pressao_eta - Coreeto


   
    k13_elemento[:,:] = matriz_pressao_ksi
    k31_elemento[:,:] = matriz_pressao_ksi.T
  
    k23_elemento[:,:] = matriz_pressao_eta
    k32_elemento[:,:] = matriz_pressao_eta.T
    
    
    linhas =[]
    linhas.append(int(elemento))
    linhas.append(k11_elemento)
    linhas.append(k12_elemento)
    linhas.append(k13_elemento)
    linhas.append(k21_elemento)
    linhas.append(k22_elemento)
    linhas.append(k23_elemento)
    linhas.append(k31_elemento)
    linhas.append(k32_elemento)
    k_pilha.append(linhas)
    
  
    return(k_pilha)












    
   
   
   
   
   
   
   
  
