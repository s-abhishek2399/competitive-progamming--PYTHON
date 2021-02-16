
def calc(l,i):
    x=l.pop()
    y=l.pop()
    if(i=="+"):
        return x+y
    elif(i=='-'):
        return x-y    
    elif(i=='*'):
        return x*y
    elif(i=='/'):
        return x/y
    else:
        pass             
s=input("Enter expression :")
s=s[-1::-1]    
l=[]
for i in s:
    if(i.isnumeric()):
        l.append(int(i))
    else:
        v=calc(l,i)
        l.append(v)
print("value :", l.pop())            