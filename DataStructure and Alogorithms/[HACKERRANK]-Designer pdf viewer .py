l1=list(map(int, input().rstrip().split()))
s=input()
l2=[]
for i in range(len(s)):
    l2.append(l1[ord(s[i])-97])
y=max(l2)
area=len(s)*y
print(area)
    
