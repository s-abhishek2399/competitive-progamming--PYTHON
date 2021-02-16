nth_term=int(input())
n1=0
n2=1
count=0
while count<nth_term:
    print(n1)
    x=n1+n2
    n1=n2
    n2=x
    count+=1