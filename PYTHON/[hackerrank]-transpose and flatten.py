import numpy as np
x,y=map(int,input().split())
a=np.array([input().split() for _ in range(x)],int)
print(np.transpose(a))
print(a.flatten())

