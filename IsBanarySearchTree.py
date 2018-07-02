""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import math

def checkBST(root, Min = 0, Max = 10000):
    if root == None:
        return True
    elif (root.data < Min or root.data > Max):
        # print("min max root {}".format(root.data))
        
        return False
    # print("root {}".format(root.data))
        
    
    return checkBST(root.left, Min, root.data - 1) and checkBST(root.right, root.data + 1, Max)
