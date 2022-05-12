#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    if len(arr) % 2 == 0:
        element_1 = int(len(arr) / 2)
        element_2 = int(len(arr) / 2) - 1
        return (arr[element_1] + arr[element_2]) / 2
    else:
        element = int(len(arr) / 2)
        return arr[element]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
