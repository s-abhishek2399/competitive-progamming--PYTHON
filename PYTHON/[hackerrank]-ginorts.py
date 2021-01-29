

s=input()
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(len(s)):
    if s[i].islower():
        l1.append(s[i])
    elif s[i].isupper():
        l2.append(s[i])
    elif s[i].isdigit():
        if(int(s[i])%2!=0):
            l3.append(s[i])
        else:
            l4.append(s[i])
    else:
        pass
l1.sort()
l2.sort()
l3.sort()
l4.sort()
x=l1+l2+l3+l4
c=""
y=c.join(x)
print(y)
