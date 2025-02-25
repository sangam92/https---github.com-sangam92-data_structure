"""
344. Reverse String

"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[-i-1]=s[-i-1],s[i]
        return s

s=Solution()
print(s.reverseString(["h","e","l","l","o"]))