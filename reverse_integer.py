"""
7. Reverse Integer

"""

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        y=x
        if y < 0:
            x *=-1
        while x>0:
            pop= x%10
            x=x//10
            rev = rev*10+ pop
        if y < 0:
            return "-" + str(rev)
        return rev


s1=Solution()
print(s1.reverse(-321))
