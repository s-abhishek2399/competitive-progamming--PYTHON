l = int(input())
r = int(input())
list=[]
for i in range(l,r+1):
    for j in range(i,r+1):
        x=i^j
        list.append(x)
print(max(list)) 
