import math
import random

#VIPA
def vipa(me,mt,x):
    ml=len(me) ## model length, i.e. the no of states
    sl=len(x) ### sequence length
    tmp=[]
    for i in range(sl):
        tmp.append(20)
    visc=[] ### viterbi score matrix
    vpth=[] ### viterbi path matrix
    for i in range(ml):
        visc.append(tmp[:])
        vpth.append(tmp[:])
    ### boundary
    for i in range(ml):
        visc[i][0]= me[i][int(x[0])]
    ### loop
    for i in range(1,sl):
        for j in range(ml):
            visc[j][i]=me[j][int(x[i])]+ mt[0][j]+visc[0][i-1]
            vpth[j][i]=0
            for k in range(ml):
                a=me[j][int(x[i])]+ mt[k][j]+visc[k][i-1]
                if a>visc[j][i]:
                    visc[j][i]=a
                    vpth[j][i]=k

    op=[] ### our path
    tmpv=visc[0][sl-1]
    tmpp=0
    for k in range(ml):
        if visc[k][sl-1]>tmpv:
            tmpv=visc[k][sl-1]
            tmpp=k
    op.append(tmpp)
    for i in range(sl-1, 0, -1):
        a=vpth[tmpp][i]
        op.append(a)
        tmpp=a
    op.reverse()
    return [visc, vpth, op] #Return viterbi score matrix, path matrix and resulting path






    
