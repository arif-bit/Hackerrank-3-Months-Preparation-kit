#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    negative_count = len(list(filter(lambda x: (x < 0), arr)))/len(arr)
    postive_count = len(list(filter(lambda x: (x > 0), arr)))/len(arr)
    zero_count = len(list(filter(lambda x: (x == 0), arr)))/len(arr)
    sys.stdout.write(f"{postive_count}\n{negative_count}\n{zero_count}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)