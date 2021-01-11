nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
x=a[d:]
y=a[:d]
z=x+y
for i in z:
    print(i, end=" ")
