#PROBLEM 1 
#euler website
import numpy as np

N= np.arange(1,1000,1)


SUM_A = sum(N[np.argwhere(N%3==0)])+sum(N[np.argwhere(N%5==0)])-sum(N[np.argwhere(N%15==0)])

SUM_B = sum(i for i in range(1,1000) if i%3==0 or i%5==0)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


print(type(SUM_A), type(SUM_B))
print(SUM_A, SUM_B)

