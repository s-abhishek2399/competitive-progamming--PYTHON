st=input().split()
s=int(st[0])
t=int(st[1])
ab=input().split()
a=int(ab[0])
b=int(ab[1])
n1n2=input().split()
n1=int(n1n2[0])
n2=int(n1n2[1])
l1=list(map(int,input().rstrip().split()))
l2=list(map(int,input().rstrip().split()))
x=[]
y=[]
c1=0
c2=0
for i in l1:
    c=a+i
    x.append(c)
for c in x:
    if c in range(s,t+1):
        c1=c1+1
for j in l2:
    d=b+j
    y.append(d)
for d in y:
    if d in range(s,t+1):
        c2=c2+1

print(c1)        
print(c2)
