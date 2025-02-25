"""
1402 Reducing Dishes
"""

class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        l=sorted(satisfaction)
        a=b=0

        for i in reversed(l):
            a+=i
            b=max(b,a+b)

        return b

s=Solution()
print(s.maxSatisfaction([-1,-8,0,5,-9]))
