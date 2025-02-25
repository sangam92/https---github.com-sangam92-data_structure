"""
 validate the BST
"""


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class Binarysearchvalid:

    def insert(root,data):
        if root is None:
            return Node(data)
        else:
            if root.data < data:
                root.right = insert(data)
            else:
                root.left = insert(data)

        return root
