n = int(input())
a = list(map(int, input().rstrip().split()))
c=0
for i in a:
    c=c^i
print(c)    
