def kthSmallest(a,k):
    for i in range(len(a)): 
        min = i 
        for j in range(i+1, len(a)): 
            if a[min] > a[j]: 
                min= j       
        a[i], a[min] = a[min], a[i]
    print(a)
    return a[k-1]
a = [12, 3, 5, 7, 19]
k = 2
print("K'th smallest element is",kthSmallest(a,k))
