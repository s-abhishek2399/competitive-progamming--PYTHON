def count_substring(string, sub_string):
    count=0
    l1=[string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
    for x in l1:
        if x==sub_string:
            count+=1
       
    return count

