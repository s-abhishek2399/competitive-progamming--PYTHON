# Enter your code here. Read input from STDIN. Print output to STDOUT
np=input().split()
n=int(np[0])
p=int(np[1])
l1=[]
for i in range(p):
    l=list(map(float,input().split()))
    l1.append(l)
for i in zip(*l1):
    a=sum(i)/len(i)
    print(a)
