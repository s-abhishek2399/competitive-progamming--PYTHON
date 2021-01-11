x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
k_1=x1+v1   
k_2=x2+v2
x=0
for i in range(10000):
    if(k_1 == k_2):
        x=1
        break
    k_1=k_1+v1
    k_2=k_2+v2    
if(x==0):
    print("NO")   
else:
    print("YES")    
