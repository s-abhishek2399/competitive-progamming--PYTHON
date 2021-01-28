
n = int(input())

x = list(map(int, input().rstrip().split()))
z=x[::-1]

for i in z:
    print(i, end=" ")
  
