import numpy as np
x,y= map(int, input().split())
z=np.array([input().split() for _ in range(x)],int)
np.set_printoptions(legacy='1.13')
print(np.mean(z,axis=1))
print(np.var(z,axis=0))
print(np.std(z,None))

