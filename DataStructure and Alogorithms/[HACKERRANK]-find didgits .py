#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    x=str(n)
    output =[int(d) for d in str(x)]
    count=0
    for a in output:
        if(a!=0):
            if(n%int(a)==0):
                count+=1
    return count   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
