"""
53. Maximum Subarray

"""

class Solution:
    def maxSubArray(self, nums) -> int:
        newNum = maxTotal = nums[0]        
	
        for i in range(1, len(nums)):
            print(nums[i],newNum)
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)
            print(maxTotal)
        return maxTotal	



s=Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))