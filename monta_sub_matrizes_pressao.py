 
 
 
 #matriz de pressao  
            for i_local in range(0,NNEV):
                    linha = int(conectividade_velocidade[elemento][i_local])
                    for j_local in range(NNEP):
                          coluna = int (conectividade_pressao[elemento][j_local])
                          
                          
                          #Motagem K13
                          valor = float(k13_torre[elemento][i_local][j_local])
                          k13_global[linha][coluna] = k13_global[linha][coluna]+ valor

                          #Motagem K23
                          valor = float( k23_torre[elemento][i_local][j_local])
                          k23_global[linha][coluna] = k23_global[linha][coluna]+ valor
                         
                        
                          
                          #Montagem 31
                          valor = float(k31_torre[elemento][j_local][i_local])
                          k31_global[coluna][linha] = k31_global[coluna][linha]+ valor  

                          #Montagem 32 
                          k32_global[coluna][linha]= k32_global[coluna][linha]+float(k32_torre[elemento][j_local][i_local])

