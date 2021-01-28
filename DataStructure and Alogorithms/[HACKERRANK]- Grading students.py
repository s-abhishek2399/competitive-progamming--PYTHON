import sys


n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    
    if x >= 38:
        if x % 5 > 2:
            while x % 5 != 0: x += 1
    print(x)
