n=int(input())
list=list(map(int,input().rstrip().split()))
z=max(list)
def birthday():
    count=0
    for i in list:
        if(i==z):
            count=count+1
    return count 
x=birthday()  
print(x)
  
