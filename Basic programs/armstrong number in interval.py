start=int(input())
end=int(input())
for num in range(start,end+1):
    sum=0
    temp=num
    while temp>0:
        digit = temp % 10
        sum =  sum + (digit ** 3)
        temp //=10
        if num==sum:
             print(num)
