#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks = sorted(sticks, reverse=True)
    sticks = zip(sticks, sticks[1:], sticks[2:])
    return next(([x3, x2, x1] for (x1, x2, x3) in sticks if x3 + x2 > x1), [-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
