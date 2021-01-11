nk=input().split()
n=int(nk[0])
k=int(nk[1])
l1=list(map(int, input().rstrip().split()))
z=max(l1)
if(z>k):
    print(z-k)
else:
    print("0")
    
