#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    if len(arr) == 0: return 0
    
    count = 0
    n = len(arr)

    # create dict with {key:element , value:index}
    arr_dict = {}
    for index, ele in enumerate(arr):
        arr_dict[ele] = index
    
    print("arr_dict: {}".format(arr_dict))
    # To keep track of visited elements (initalise False)
    visited = [False] * n
    sorted_arr = sorted(arr_dict.items(), key=lambda x: x[0])
    print("sorted arr {}".format(sorted_arr))
    
    # Sort the dictionary with the key(ele) value
    for ele, index in sorted_arr:
        visited_el = visited[index]
        print("I {0}, visited[{0}]: {1}".format(index, visited_el))
        
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
            print("not visited {}, cycle_count {}".format(i, cycle_count))
            

        # add the cycle_count to count (cycle-1 always for the loop)        
        count += cycle_count - 1
        print("count {}".format(count))
        

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
