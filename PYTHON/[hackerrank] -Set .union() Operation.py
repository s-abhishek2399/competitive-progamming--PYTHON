# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l1=list(map(int,input().split()))
n1=int(input())
l2=list(map(int,input().split()))
a=set(l1)
b=set(l2)
x=a.union(b)
print(len(x))
