"""
Maximum Product Sub array

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min=prev_max=global_max=nums[0]

        for num in nums[1:]:
            minn,maxx=min(num,prev_min*num,prev_max*num),max(num,prev_min*num,prev_max*num)
            prev_min,prev_max,global_max=minn,maxx,max(global_max,maxx)
        return global_max


s=Solution()

print(s.maxProduct([-2,3,-4]))

