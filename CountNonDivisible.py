#  https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
  dictionary = {}
  popedItems = {}
  arr = list(A)

  for dicKey in arr:
    actual_number = A.pop(0)

    if actual_number in popedItems:
      continue

    if not dicKey in dictionary:
      dictionary[dicKey] =  0

    for n in A:
      if actual_number % n != 0:
        dictionary[actual_number] +=  1

      if (n % actual_number != 0) and not n in dictionary:
        dictionary[n] =  1
    popedItems[actual_number] = True
  res = []
  print('arr ', arr)
  for num in arr:
      res.append(dictionary[num])


  print('res ', res)
  return res

solution([3, 1, 2, 3, 6])