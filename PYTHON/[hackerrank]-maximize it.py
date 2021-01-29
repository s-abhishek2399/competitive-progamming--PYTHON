from itertools import product
k,m=map(int,input().split())
l1=(list(map(int,input().split()))[1:] for _ in range(k))
h=map(lambda x: sum(i**2 for i in x )%m ,product(*l1))
print(max(h))
