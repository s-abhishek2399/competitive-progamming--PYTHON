import numpy as np
def rotate(arr,d):
    m = np.array(arr,int)
    if d == 90:
        return np.rot90(m,1)
    return np.rot90(m,-3)

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(rotate(a,90))
print(rotate(a,270))
