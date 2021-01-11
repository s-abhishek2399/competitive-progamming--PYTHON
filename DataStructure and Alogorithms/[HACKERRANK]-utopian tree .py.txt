t=int(input())
l=[]
for y in range(t):
    n=int(input())
    l.append(n)
for a in l:
    z=0
    for i in range(a+1):
        x=z
        if((i%2)==0):
            z=x+1
        if((i%2)!=0):
            z=x*2
    print(z)
