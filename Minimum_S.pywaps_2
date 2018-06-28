#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    if len(arr) == 1: return 0, arr
    
    count = 0
    n = len(arr)

    # create dict with {key:element , value:index}
    arr_dict = {}
    for index, ele in enumerate(arr):
        arr_dict[ele] = index

    # To keep track of visited elements (initalise False)
    visited = [False] * n

    # Sort the dictionary with the key(ele) value
    for ele, index in sorted(arr_dict.items(), key=lambda x: x[0]):
        visited_el = visited[index]
        print("visited[{1}] {2}, ele {0}, index {1}".format((visited_el), ele, index))
        # if ele already visited or if its already at correct place, ignore
        if visited_el or ele == index:
            continue

        # otherwise count the elements in present cycle
        cycle_count = 0
        i = ele - 1
        while not visited[i]:
            # element visited now
            visited[i] = True

            # visit the ele at its index
            i = arr_dict[ele]
            cycle_count += 1
            print("visited {}, cycle_count {}".format(i, cycle_count))
            

        # add the cycle_count to count (cycle-1 always for the loop)        
        count += cycle_count
        print("count {}".format(count))
        

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
