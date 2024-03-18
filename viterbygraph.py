import matplotlib.pyplot as plt
import numpy as np
import imageio

inmod = [[0.2,0.16,0.16,0.16,0.16,0.16],
         [0.16,0.16,0.16,0.16,0.16,0.2]]
intr = [[0.55,0.45],
        [0.45,0.55]]

def graphexp(modlist, n):
    #Graph
    counts1 = modlist[0] #model list 1
    counts2 = modlist[1] #model list 2
    nbins = []
    for i in range(len(counts1)):
        nbins.append(i+1)
    
    fig, axs = plt.subplots(2,1,sharex=True,tight_layout=True)
    axs[0].bar(height = counts1, x = nbins, width = 0.9)
    axs[1].bar(height = counts2, x = nbins, width = 0.9)
    
    #plt.show()
    #Export with a naming element based on n
    plt.savefig(f'img{n}.png')

def generategif(inputlist, k):
    #compile images into one gif
    imglist = []
    for i in range(k+1):
        imglist.append(imageio.imread(f"img{i}.png"))

graphexp(inmod, 0)
