"""
1217. Minimum Cost to Move Chips to The Same Position
"""
class Solution:
    def minCostToMoveChips(self, position):

        o, e = 0, 0

        for p in position:
            if p%2==1:
                o+=1
            else:
                e+=1
        return min(o, e)

s=Solution()
print(s.minCostToMoveChips([2,2,2,3,3]))