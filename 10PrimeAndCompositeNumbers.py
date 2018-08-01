# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/start/
# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# has exactly three peaks: 3, 5, 10.

# We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

# A[0], A[1], ..., A[K − 1],
# A[K], A[K + 1], ..., A[2K − 1],
# ...
# A[N − K], A[N − K + 1], ..., A[N − 1].
# What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

# The goal is to find the maximum number of blocks into which the array A can be divided.

# Array A can be divided into blocks as follows:

# one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
# two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
# three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
# However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

# The maximum number of blocks that array A can be divided into is three.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

# If A cannot be divided into some number of blocks, the function should return 0.

# For example, given:

#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# the function should return 3, as explained above.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000].
# Complexity:

# expected worst-case time complexity is O(N*log(log(N)));
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    max_divisible_groups = 0
    peaks_indexes = []
    a_len = len(A)

    if a_len < 3:
        return 0

    prev_item = A[0]
    for index in range(1, a_len - 1):
        posible_peak = A[index]
        if (prev_item < posible_peak and posible_peak > A[index + 1]):
            peaks_indexes.append(index)
        prev_item = posible_peak

    peaks_number = len(peaks_indexes)
    if peaks_number == 0:
        return 0
    if a_len % peaks_number == 0:
        return peaks_number

    # ToDo missing when the peaks does not mod==0 the a_lenght
    # top of mind if the original is divided in the middle the peaks could -
    # - be in one side
    max_divisible_groups = peaks_number - 1
    while a_len % max_divisible_groups != 0:
        max_divisible_groups -= - 1

    # for index in range(0, a_len, ):
        pass
        # 12 elements and 2 peaks but just one side has the peaks
    return max_divisible_groups


# print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
print(solution([1, 1, 1, 1, 1, 1, 3, 1, 3, 1, 3, 1]))
