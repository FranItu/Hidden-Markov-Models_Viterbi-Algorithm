import viterbipath
import viterbicount
import math
import random
import numpy as np
import viterbygraph
import imageio

k = 100 #number of iterations

f=open("sim.txt", "r")
sx=f.readlines()
f.close()

for i in range(len(sx)):
	sx[i] = int(sx[i].rstrip())

inmod = [[0.2,0.16,0.16,0.16,0.16,0.16],
         [0.16,0.16,0.16,0.16,0.16,0.2]]
intr = [[0.55,0.45],
        [0.45,0.55]]

basemod = np.array(inmod)
viterbygraph.graphexp(inmod, 0)

for i in range(len(inmod)):
    for j in range(len(inmod[i])):
        inmod[i][j] = math.log(inmod[i][j])
    for j in range(len(intr[i])):
        intr[i][j] = math.log(intr[i][j])

print(basemod)

for i in range(k):
    a = viterbipath.vipa(inmod, intr, sx)
    b = viterbicount.coolcounter(len(inmod), len(inmod[0]), sx, a[2])
    inmod = b[0]
    hymod = (((i+1))/k)*np.exp(inmod) + ((k-(i+1))/k)*basemod #softened graphs
    print(hymod)
    viterbygraph.graphexp(hymod,i+1)
    intr = b[1]

imglist = []
for i in range(k+1):
    imglist.append(imageio.imread(f"img{i}.png"))
imageio.mimsave("movie.gif",imglist)

