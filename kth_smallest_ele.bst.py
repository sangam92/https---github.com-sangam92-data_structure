"""
Kth Smallest Element in the BST

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res=None
        self.k=k
        self.search(root)
        return self.res
        #count=0
    def search(self,root):
        if root is None:
            return 
        self.search(root.left)
        self.k-=1
        if self.k==0:
            self.res=root.val
            return 
        self.search(root.right)
        
 """
class Solution:
    def kthSmallest(self,root:TreeNode,k:int) -> int:
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                
                root=root.left
        
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right

        


n=TreeNode(10)
n.left=TreeNode(7)
n.right=TreeNode(12)
n.left.left=TreeNode(3)
n.left.right=TreeNode(8)
n.right.left=TreeNode(11)
s=Solution()
print(s.kthSmallest(n,3))
