#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    x = False
    y = 0
    height = 0
    
    for step in s:
        if step == 'U':
            height += 1
        else:
            height -= 1
            
        if not x:
            if height < 0:
               x = True
        elif height == 0:
            x = False
            y += 1
            
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
