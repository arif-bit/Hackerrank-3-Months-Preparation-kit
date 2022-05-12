#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res = []
    for i in grades:
        x = i
        if x < 38:
            res.append(x)
        else:
            if i % 5 == 1:
                x += 4
            elif i % 5 == 2:
                x += 3
            elif i % 5 == 3:
                x += 2
            elif i % 5 == 4:
                x += 1
            else:
                x += 5

            if abs(x - i) < 3:
                res.append(x)
            else:
                res.append(i)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
