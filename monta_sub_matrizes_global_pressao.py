def monta_sub_matrizes_global_pressao(conectividade_interna,conenctividade,conectividade_pressao,contorno_u, contorno_v,k13_torre,k23_torre,k31_torre,k32_torre,NNEV,NNEP,NEFT,NNEVT,NNEPT): 
        
    import numpy as np
    from scipy.sparse import csc_matrix
  
    NNT =NNEV*NNEP*NEFT
    NNTMP = NEFT*NNEP*NNEP
    linhas_global = np.zeros((NNT), dtype = np.int64)
    colunas_global = np.zeros((NNT), dtype = np.int64)

    linhas_global2 =np.zeros((NNT),dtype = np.int64)
    coluna_global2 =np.zeros((NNT), dtype = np.int64)

    linhas_global_p = np.zeros((NNTMP), dtype = np.int64) 
    colunas_global_p = np.zeros((NNTMP), dtype = np.int64) 

    K13_valor = np.zeros((NNT),dtype = np.longdouble)
    K23_valor = np.zeros((NNT), dtype = np.longdouble)
    K31_valor = np.zeros((NNT), dtype = np.longdouble)
    K32_valor = np.zeros((NNT),dtype = np.longdouble  )
    k33_valor= np.zeros(( NNTMP), dtype = np.longdouble)

    #Linha 1  Matriz Global
    
    vetor_p =   np.zeros((NNEPT),  dtype=np.longdouble)
    
    contador =0
    for elemento in range (0,NEFT):
          for i_local in range(0,NNEV):
               linha  =int (conectividade_interna[elemento][i_local]) 
               
               for j_local in range (0,NNEP):   
                      coluna = int (conectividade_pressao[elemento][j_local])
                      if linha> -1 and coluna > -1 :
                             linhas_global[contador] = linha 
                             colunas_global[contador] = coluna
                                                     
                             K13_valor[contador ] = k13_torre[elemento][i_local][j_local]
                             K23_valor[contador ] = k23_torre[elemento][i_local][j_local]

                             contador = contador +1
                             
                            
    contador = 0                         
    for elemento in range(0,NEFT):
            for i_local in range(0,NNEP):
                   linha = int(conectividade_pressao[elemento][i_local])
                   for j_local in range(0,NNEV):
                          coluna =int(conectividade_interna[elemento][j_local])
                          if linha>-1 and coluna >-1:
                                    linhas_global2[contador] = int(conectividade_pressao[elemento][i_local])  
                                    coluna_global2[contador] = int(conectividade_interna[elemento][j_local])
                                    
                                    K31_valor[contador] = k31_torre[elemento][i_local][j_local]
                                    K32_valor[contador] = k32_torre[elemento][i_local][j_local]
                                    contador = contador +1

                                    

                          if linha > -1 and coluna == -1: 
                                    posicao =int(conenctividade[elemento][j_local]) 
                                    vetor_p[linha] =vetor_p[linha] -contorno_u[posicao]*k31_torre[elemento][i_local][j_local] - contorno_v[posicao]*k32_torre[elemento][i_local][j_local]
                            
                              
                              
    k13_global= csc_matrix( (K13_valor,(linhas_global,colunas_global)), shape=(NNEVT,NNEPT), dtype=np.longdouble )
    k23_global= csc_matrix((K23_valor,(linhas_global,colunas_global)), shape=(NNEVT,NNEPT), dtype=np.longdouble )
    k31_global= csc_matrix((K31_valor,(linhas_global2,coluna_global2)), shape=(NNEPT,NNEVT), dtype=np.longdouble )
    k32_global= csc_matrix((K32_valor,(linhas_global2,coluna_global2)), shape=(NNEPT,NNEVT), dtype=np.longdouble )
    k33_global= csc_matrix((k33_valor,(linhas_global_p,colunas_global_p)), shape=(NNEPT,NNEPT), dtype=np.longdouble )

 
    return(k13_global,k23_global,k31_global, k32_global,k33_global,vetor_p )  







