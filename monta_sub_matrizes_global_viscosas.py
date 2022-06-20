def monta_sub_matrizes_global_viscosas(conectividade_interna,MATRIZ_vel,contorno_u, contorno_v, vetor_f1,vetor_f2, k11_torre,k12_torre,k21_torre,k22_torre,NNEV,NEFT,NNTEV):
                            
    
    # Importar os arquivos de malha
    import numpy as np
    from scipy.sparse import csc_matrix
   
    NNT =   NEFT*NNEV*NNEV
   
    #Monta Matriz Viscosa 
    contador =0
    linhas_global = np.zeros( (NNT), dtype =np.int64)
    colunas_global = np.zeros((NNT),dtype =np.int64)

    k11_global_valor = np.zeros((NNT), dtype =np.longdouble)
    k12_global_valor = np.zeros((NNT), dtype =np.longdouble)
    k22_global_valor = np.zeros((NNT),  dtype =np.longdouble)
    k21_global_valor = np.zeros((NNT), dtype = np.longdouble)
    
 



    for elemento in range(0,NEFT):


           #Montagem Termos viscosos    
          
            for i_local in range(0,NNEV):
                   linha =int(conectividade_interna[elemento][i_local]) 
                   for j_local in range(0,NNEV):
                           coluna = int (conectividade_interna[elemento][j_local])
                           if linha>-1 and coluna >-1 :
                                #Preenchendo K11_Global   
                               linhas_global[contador]= int(linha)
                               colunas_global[contador]= int (coluna)

                               k11_global_valor[contador] =  k11_torre[elemento][i_local][j_local]
                               k12_global_valor[contador]  = k12_torre[elemento][i_local][j_local]  
                               k21_global_valor[contador]   = k21_torre[elemento][i_local][j_local]
                               k22_global_valor[contador]  =  k22_torre[elemento][i_local][j_local]
                               contador = contador+1

                                         
                           if linha>-1 and coluna == - 1 :
                               posicao =int(MATRIZ_vel[elemento][j_local]) 
                               vetor_f1[linha] =vetor_f1[linha] -contorno_u[posicao]*k11_torre[elemento][i_local][j_local] -contorno_v[posicao]*k12_torre[elemento][i_local][j_local]
                              
                               vetor_f2[linha] =vetor_f2[linha] -contorno_u[posicao]*k21_torre[elemento][i_local][j_local] -contorno_v[posicao]*k22_torre[elemento][i_local][j_local]
                              
    k11_global = csc_matrix((k11_global_valor, (linhas_global,colunas_global)), shape=(NNTEV,NNTEV), dtype=np.longdouble ) 
    k12_global = csc_matrix((k12_global_valor,(linhas_global,colunas_global)), shape=(NNTEV,NNTEV), dtype=np.longdouble ) 
    k21_global = csc_matrix((k21_global_valor,(linhas_global,colunas_global)), shape=(NNTEV,NNTEV), dtype=np.longdouble )    
    k22_global = csc_matrix((k22_global_valor,(linhas_global,colunas_global)), shape=(NNTEV,NNTEV), dtype=np.longdouble )                        





 


            
         
                  



   
                   
    return(k11_global, k12_global,k21_global,k22_global,vetor_f1,vetor_f2)