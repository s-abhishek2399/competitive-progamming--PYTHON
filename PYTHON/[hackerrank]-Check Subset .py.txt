
t=int(input())
for i in range(t):
    n1=int(input())
    l1=list(map(int,input().split()))
    a=set(l1)
    n2=int(input())
    l2=list(map(int,input().split()))
    b=set(l2)
    if((a.issubset(b))==True):
        print(True)
    else:
        print(False)
