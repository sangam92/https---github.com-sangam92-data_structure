"""

1374.leetcode

"""
class Solution:
    def generateTheString(self, n: int) -> str:
        result=""
        if n%2==1:
            for i in range(0,n):
                result+='a'
            return result
        else:
            for i in range(0,n-1):
                 result+='a'
            return result+'b'               
s=Solution()
print(s.generateTheString(4))