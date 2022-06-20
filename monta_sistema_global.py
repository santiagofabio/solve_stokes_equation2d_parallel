def monta_sistema_global(k11_global, k12_global,k13_global,k21_global,k22_global,k23_global,k31_global,k32_global,k33_global, vetor_fu, vetor_fv, vetor_p):

    import numpy as np 

    from scipy.sparse import csc_matrix ,hstack,vstack

    C1 = vstack( (k11_global,k21_global,k31_global))
    C2 = vstack((k12_global,k22_global,k32_global))
    C3 = vstack((k13_global,k23_global,k33_global))
    
   


    KGLOBAL = hstack((C1,C2,C3))


  
    VETOR_B=[]
    VETOR_B.extend(vetor_fu)
    VETOR_B.extend(vetor_fv)
    VETOR_B.extend(vetor_p)



    return(KGLOBAL,VETOR_B)

 












