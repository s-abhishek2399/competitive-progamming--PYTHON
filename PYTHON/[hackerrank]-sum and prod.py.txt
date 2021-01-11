import numpy as np
x,y= map(int, input().split())
z=np.array([input().split() for _ in range(x)],int)
p=np.sum(z,axis=0)
print(np.prod(p))
