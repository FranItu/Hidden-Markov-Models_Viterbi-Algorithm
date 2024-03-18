import math
#num of dice
ndic = 2
#num of symbols
nsym = 6
#sample str
sample = '00000555555'
#path
pth = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def coolcounter(nd, nsy, smp, path): #number of dice, number of symbols, sample string/list , result path
    newtran = [[],[]]
    newemi = [[],[]]
    for i in range(nd):
        for j in range(nd):
            newtran[i].append(1)
        for j in range(nsy):
            newemi[i].append(1)
    for i in range(len(path)-1):
        newtran[path[i]][path[i+1]] = newtran[path[i]][path[i+1]] +1

    for i in range(len(path)):
        a = int(path[i])
        b = int(smp[i])
        newemi[a][b] = newemi[a][b] + 1

    for i in range(len(newemi)):#normalization
        s = sum(newemi[i])
        t = sum(newtran[i])
        for j in range(len(newemi[i])):
            newemi[i][j] = newemi[i][j]/s
        for j in range(len(newtran[i])):
            newtran[i][j] = newtran[i][j]/t

    for i in range(len(newemi)): #logscale
        for j in range(len(newemi[i])):
            newemi[i][j] = math.log(newemi[i][j])
        for j in range(len(newtran[i])):
            newtran[i][j] = math.log(newtran[i][j])
    
    return [newemi, newtran] #return frequency counts for transitions and emitions 

out = coolcounter(ndic,nsym,sample, pth)

