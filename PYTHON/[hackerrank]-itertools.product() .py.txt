# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
l=[a,b]
l1=list(product(*l))
print(" ".join(map(str, l1)))
