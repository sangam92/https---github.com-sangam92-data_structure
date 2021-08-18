"""
112.Path Sum

"""

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
   
        res=0
        if root is None:
            return None
        
        res=res+root.val
        if res == targetSum:
            return True
        
        
        self.hasPathSum(root.left, targetSum)
        self.hasPathSum(root.right, targetSum)
        
        
        return False