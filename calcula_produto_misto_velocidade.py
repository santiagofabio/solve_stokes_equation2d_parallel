def calcula_produto_misto_velocidade(cordenadas_x,cordenadas_y, nl, nc,NNE):
  import numpy
  from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
  from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi
  from calcula_derivadas_locais import calcula_derivadas_locais
  

  raizes = numpy.zeros(5)
  pesos = numpy.zeros(5)
  matriz_velocidade_deta_dksi = numpy.zeros((nl,nc))
  matriz_velocidade_dksi_deta = numpy.zeros((nl,nc))
  npg =5

  #raizes do método de Gauss
  raizes[0]= 0.9061798459
  raizes[1]= 0.5384693101
  raizes[2]=0.0
  raizes[3]= -0.5384693101
  raizes[4]= -0.9061798459
    

    #pesos método de Gausss

  pesos[0]=0.2369268850 
  pesos[1]=0.4786286705
  pesos[2]=0.5688888889
  pesos[3]=0.4786286705
  pesos[4]=0.2369268850 



 
  # Intervalo de integraçao
  ax = 0.0
  bx = 1.0
  ay = 0.0
  


  for i in range(0,nl):
        for j in range(0,nc):
              
              #Inicio integração Gaussiana 
                h1= (bx-ax)*0.5
                h2 =(bx+ax)*0.5
                somatorio_integral_derivada_deta_dksi =0.0
                somatorio_integral_derivada_dksi_deta =0.0
                
              
               
                for ig in range(0,npg):
                    integral_derivada_funcao_deta_dksi =0.0
                    integral_derivada_funcao_dksi_deta =0.0
                            
                    ksi =h1*raizes[ig]+ h2
                    by = 1-ksi 
                    k1 =(by-ay)*0.5
                    k2 = (by+ay)*0.5
                    
                      
                             
                    
                    
                    for jg in range(0,npg):
                            eta =k1*raizes[jg]+k2  
                                      
                             
                            [x_dpsi_dksi,x_dpsi_deta,y_dpsi_dksi,y_dpsi_deta ] = calcula_derivadas_locais(cordenadas_x,cordenadas_y,ksi, eta, NNE)
                            jacobiano  = abs(y_dpsi_deta*x_dpsi_dksi- y_dpsi_dksi*x_dpsi_deta)
                            
                            inv_jacobiano = 1.0/jacobiano

                            
            
                            #Estamos calculando a integral de df_deta_dksi (df_eta_i,df_ksi_j )
                            df_eta_i=   -avalia_derivada_funcao_ksi(i,ksi,eta)*x_dpsi_deta +avalia_derivada_funcao_eta(i,ksi,eta)*x_dpsi_dksi
                            df_ksi_j =   avalia_derivada_funcao_ksi(j,ksi,eta)*y_dpsi_deta   -avalia_derivada_funcao_eta(j,ksi,eta)*y_dpsi_dksi
                            valor_derivada_funcao_deta_dksi = df_eta_i*df_ksi_j*inv_jacobiano
                            integral_derivada_funcao_deta_dksi = integral_derivada_funcao_deta_dksi + pesos[jg]*valor_derivada_funcao_deta_dksi

                            #Estamos calculando a integral de df_dksi_deta (df_ksi_i,df_eta_j )
                            df_ksi_i =   avalia_derivada_funcao_ksi(i,ksi,eta)*y_dpsi_deta   -avalia_derivada_funcao_eta(i,ksi,eta)*y_dpsi_dksi
                            df_eta_j =   -avalia_derivada_funcao_ksi(j,ksi,eta)*x_dpsi_deta +avalia_derivada_funcao_eta(j,ksi,eta)*x_dpsi_dksi
                            valor_derivada_funcao_dksi_deta = df_ksi_i*df_eta_j*inv_jacobiano
                            integral_derivada_funcao_dksi_deta = integral_derivada_funcao_dksi_deta + pesos[jg]*valor_derivada_funcao_dksi_deta


             


                     # Estamos calculando a integral de df_deta_dksi   
                    somatorio_integral_derivada_deta_dksi = somatorio_integral_derivada_deta_dksi +pesos[ig]*k1*integral_derivada_funcao_deta_dksi
                    # Estamos calculando a integral de df_deta_dksi 
                    somatorio_integral_derivada_dksi_deta = somatorio_integral_derivada_dksi_deta +pesos[ig]*k1*integral_derivada_funcao_dksi_deta

                    
                # Estamos calculando a integral df_deta_dksi 
                somatorio_integral_derivada_deta_dksi = h1*somatorio_integral_derivada_deta_dksi
                somatorio_integral_derivada_dksi_deta = h1*somatorio_integral_derivada_dksi_deta


                
                #Alocando em ksi
                matriz_velocidade_deta_dksi[i][j] =somatorio_integral_derivada_deta_dksi
                matriz_velocidade_dksi_deta[i][j] =somatorio_integral_derivada_dksi_deta
               

  return(matriz_velocidade_deta_dksi,matriz_velocidade_dksi_deta ) 




  










