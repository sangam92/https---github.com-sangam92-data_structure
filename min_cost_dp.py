"""
746. Min Cost Climbing Stairs

"""

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        c1,c2=cost[0],cost[1]

        for i in range(2,len(cost)):
            c1,c2=c2,cost[i]+min(c1,c2)
        return min(c1,c2)

s=Solution()

print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
        