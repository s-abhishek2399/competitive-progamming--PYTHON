n=int(input())
fact=1
if(n==0):
     print("factorial of a 0  is 1")
if(n>0):    
    for i in range(1,n+1):
        fact=fact*i
    print(fact)    
