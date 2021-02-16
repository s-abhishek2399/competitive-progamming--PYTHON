def sort_e_o(a):
    odd=[a[1]]
    even=[a[0]]
    for i in range(2,len(a)):
        if i%2==0:
            even.append(a[i])
        else:
            odd.append(a[i])
    even.sort()
    odd.sort()
    even.extend(odd)
    return even
a=[1,93,0,5,8]
print(sort_e_o(a))