n=int(input())
x=5
l1=[]
for i in range(1,n+1):
    a=1*x
    b=(a//2)
    c=b*3
    x=c
    l1.append(b)
print(sum(l1))    
    
