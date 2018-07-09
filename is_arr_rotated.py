# Implement your function below.
def is_rotation(list1, list2):
    # check if the list have the same length
    max_len = len(list1) - 1 
    if max_len != len(list2)-1:
        return False

    dictionary = {}
    for index, item in enumerate(list1):
        dictionary[item] = index

    index_offset = dictionary[list2[0]]

    for index, item in enumerate(list2):
        if index_offset > max_len:
            index_offset = 0

        # print('index {}'.format(index_offset))
        dict_item = list1[index_offset]
        
        if dict_item != item:
            return False
        index_offset += 1

    return True


# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.

print("list2a should return False and return {}".format(is_rotation(list1, list2a)))
print("list2b should return True and return {}".format(is_rotation(list1, list2b)))
print("list2c should return False and return {}".format(is_rotation(list1, list2c)))
print("list2d should return False and return {}".format(is_rotation(list1, list2d)))
print("list2e should return False and return {}".format(is_rotation(list1, list2e)))
print("list2f should return True and return {}".format(is_rotation(list1, list2f)))
