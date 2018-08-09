# You are playing a game with N cards. On each side of each card a positive integer is written. The score of the game is smallest positive integer that doesn't appear on the cards' front faces. You may decide which cards you want to flip over. Having flipped them, you then read the numbers on the front faces of all the cards. What is the minimum game score you can achieve?

# Write a function:


#                             def solution(A, B)


# that, given two arrays of integers A and B, both of length N, describing the numbers written on the fronts and backs of all the cards, returns the minimum possible game score.

# For example, given A = [1, 2, 4, 3] and B = [1, 3, 2, 3], your function should return 2, as we could flip second card such that the front-facing numbers were [1, 3, 4, 3] and the smallest positive integer excluded from this sequence is 2.

# Given A = [3, 2, 1, 6, 5] and B = [4, 2, 1, 3, 3], your function should return 3, as we could flip first card such that the front-facing numbers were [4, 2, 1, 6, 5].

# Given A = [1, 2] and B = [1, 2] your function should return 3, as no matter how we flip the cards the front-facing numbers will be [1, 2].

# Assume that:

# N is an integer within the range [ 1.. 100,000];
# each element of arrays A, B is an integer within the range [ 1.. 100,000];
# input arrays are of equal size.
# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


import itertools
from math import inf


def flipgame(fronts, backs):
    same = []
    # {x for i, x in enumerate(fronts) if x == backs[i]}
    for i, x in enumerate(fronts):
        if x == backs[i]:
            same.append(x)
    ans = inf.real
    print('same {}'.format(same))
    for card in itertools.chain(fronts, backs):
        if card not in same:
            ans = min(ans, card)

    print('ans {}'.format(ans))
    if ans == inf.real:
        ans = max(same) + 1
    return ans


A = [3, 2, 1, 6, 5]
B = [4, 2, 1, 3, 3]
# --
A = [1, 2, 4, 4, 7]
B = [1, 3, 4, 1, 3]
# --
A = [1, 2]
B = [1, 2]
print(flipgame(A, B))
# 2º
