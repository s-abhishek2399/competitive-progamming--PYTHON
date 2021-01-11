import numpy as np
x,y= map(int, input().split())
z=np.array([input().split() for _ in range(x)],int)
p=np.min(z,axis=1)
print(np.max(p))
