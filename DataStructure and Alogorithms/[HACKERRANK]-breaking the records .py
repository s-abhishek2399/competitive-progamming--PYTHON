n = int(input())
l1= list(map(int, input().rstrip().split()))
m=l1[0]
n=l1[0]
count=0
count1=0


for i in l1:
    if(i>=m and i!=m):
        m=i
        count=count+1
for j in l1:
    if(j<=n and j!=n):
        n=j
        count1=count1+1
print(count,count1)
