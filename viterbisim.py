import math
import random
#SIMULATION
em = [[0,0,0,0,0,0,0,0,0,0,1,2,3,4,5],[0,1,2,3,4,5,5,5,5,5,5,5,5,5,5]]
tr = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
cs = int(random.random()+0.5)
x = []
f=open("sim.txt", "w")

for i in range(100000):
    a = random.choice(em[cs])
    x.append(a)
    f.write('%s\n' % a)
    tcs = random.choice(tr[cs])
    cs = tcs
    
f.close()
