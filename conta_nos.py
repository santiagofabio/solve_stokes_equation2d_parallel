def conta_nos(vetor, flag):
    NNT =len(vetor)
    NND =0
    for i in range(0,NNT):

          if vetor[i] == flag:
              NND = NND+1
    return(NND)
