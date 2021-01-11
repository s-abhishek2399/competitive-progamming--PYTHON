men = input().split()
m=int(men[0])
e=int(men[1])
n=int(men[2])
l1=list(map(int, input().rstrip().split()))
l2=list(map(int, input().rstrip().split()))
l3=[]
l4=[]
for i in l1:
    z=[x+i for x in l2 if (x+i)<=m]
    l3.append(z)
for i in l3:
    l4.extend(i)
if(len(l4)==0):
    print("-1")
else:    
    print(max(l4))          
