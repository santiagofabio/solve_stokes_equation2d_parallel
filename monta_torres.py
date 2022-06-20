def monta_torres(k_pilha, NNEV, NNEP,NEFT):
    import numpy
  # Torres de paralelização
    k11_torre =numpy.zeros((NEFT,NNEV,NNEV),  dtype=numpy.longdouble)
    k12_torre =numpy.zeros((NEFT,NNEV,NNEV), dtype=numpy.longdouble)
    k21_torre =numpy.zeros((NEFT,NNEV,NNEV), dtype=numpy.longdouble)
    k22_torre =numpy.zeros((NEFT,NNEV,NNEV), dtype=numpy.longdouble )
    k23_torre= numpy.zeros((NEFT,NNEV,NNEP), dtype=numpy.longdouble)
    k32_torre = numpy.zeros((NEFT,NNEP,NNEV), dtype=numpy.longdouble)
    k13_torre = numpy.zeros((NEFT,NNEV,NNEP), dtype=numpy.longdouble)
    k31_torre = numpy.zeros((NEFT,NNEP,NNEV), dtype=numpy.longdouble)


    k11_posicao = 1
    k12_posicao = 2
    k13_posicao = 3

    k21_posicao = 4
    k22_posicao = 5
    k23_posicao = 6

    k31_posicao = 7
    k32_posicao = 8

    
    unidimensional =0
    for posicao_lista_global in range(0,NEFT):
         for linha_velocidade in range(0,NNEV):
              for coluna_velocidade  in range(0,NNEV):
                   elemento = int(k_pilha[posicao_lista_global][0][0])
                   k11_torre[elemento][linha_velocidade][coluna_velocidade]= k_pilha[posicao_lista_global][unidimensional][k11_posicao][linha_velocidade][coluna_velocidade]
                   k12_torre[elemento][linha_velocidade][coluna_velocidade]= k_pilha[posicao_lista_global][unidimensional][k12_posicao][linha_velocidade][coluna_velocidade]
                   k21_torre[elemento][linha_velocidade][coluna_velocidade]= k_pilha[posicao_lista_global][unidimensional][k21_posicao][linha_velocidade][coluna_velocidade]
                   k22_torre[elemento][linha_velocidade][coluna_velocidade]= k_pilha[posicao_lista_global][unidimensional][k22_posicao][linha_velocidade][coluna_velocidade]
         
         for linha_velocidade in range(0,NNEV):
               for coluna_pressao in range(0,NNEP):
                       k13_torre[elemento][linha_velocidade][coluna_pressao]= k_pilha[posicao_lista_global][unidimensional][k13_posicao][linha_velocidade][coluna_pressao]
                       k23_torre[elemento][linha_velocidade][coluna_pressao]= k_pilha[posicao_lista_global][unidimensional][k23_posicao][linha_velocidade][coluna_pressao]
                       k31_torre[elemento][coluna_pressao][linha_velocidade]= k_pilha[posicao_lista_global][unidimensional][k31_posicao][coluna_pressao][linha_velocidade]
                       k32_torre[elemento][coluna_pressao][linha_velocidade]= k_pilha[posicao_lista_global][unidimensional][k32_posicao][coluna_pressao][linha_velocidade]
                  
    return(k11_torre,k12_torre,k13_torre,k21_torre,k22_torre,k23_torre,k31_torre,k32_torre)

