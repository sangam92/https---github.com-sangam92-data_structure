"""
279. Perfect Squares

"""

class Solution:
    def numSquares(self, n: int) -> int:
        left=0
        right=n
        mid=0
        while (left<=right):
            mid=left+right/2

            

