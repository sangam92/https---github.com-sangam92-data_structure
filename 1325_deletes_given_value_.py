"""
1325. Delete Leaves With a Given Value
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def removeLeafNodes(self, root, target: int) :

        def dfs(r):
            if r is None:
                return None
            if r.left == target:
                re
