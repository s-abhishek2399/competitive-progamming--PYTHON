import numpy as np
N,M,P=map(int,input().rstrip().split())
x=np.array([input().split() for _ in range(N)],int)
y=np.array([input().split() for _ in range(M)],int)
print(np.concatenate((x,y),axis=0))



