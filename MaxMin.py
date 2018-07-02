#!/bin/python3
# https://www.hackerrank.com/challenges/angry-children/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=greedy-algorithms

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    diff_sorted_arr = []
    sorted_arr = sorted(arr)
    print("sorted_arr: {}".format(sorted_arr))
    print()
    
    for i in range((k-1), len(sorted_arr)):
        print("sorted_arr[{}]: {}".format(i, sorted_arr[i]))
        print("sorted_arr[{}]: {}".format(i-k, sorted_arr[i - k +1]))
        print("------")
        diff = sorted_arr[i] - sorted_arr[i-k+1]
        diff_sorted_arr.append(diff)
        
    diff_sorted_arr = sorted(diff_sorted_arr)
    print()
    print("diff_sorted_arr: {}".format(diff_sorted_arr))

    return(diff_sorted_arr[0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
