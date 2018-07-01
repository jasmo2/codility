""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
class NotBSTError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        # Now for your custom code...
        self.errors = errors

def check_sub_left_tree(left_node, root, right_node):
    if (left_node):
        if root.data > left_node.data:
            check_sub_left_tree(left_node.left, left, left_node.right_node)
            check_sub_right_tree(left_node.left, left, left_node.right_node)
        else:
            raise NotBSTError("False", Exception)
    else 
        return 

def check_sub_right_tree(left_node, root, right_node):
    if (left_right):
        if root.data < right_node.data:
            check_sub_left_tree(left_node.left, left, left_node.right_node)
            check_sub_right_tree(left_node.left, left, left_node.right_node)
        else:
            raise NotBSTError("False", Exception)
    else 
        return 
    
def checkBST(root):
    # print("root  ",format(root.data))
    # print("left  ",format(root.left.left.left))
    # print("right ",format(root.right.data))
    try:
        check_sub_left_tree(root.left, root, root.right)
        return "True"        
    except NotBSTError:
        return "False"
