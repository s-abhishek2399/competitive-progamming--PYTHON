# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l1=[]
for _ in range(n):
    s=input()
    l1.append(s)
x=set(l1)    
print(len(x))
