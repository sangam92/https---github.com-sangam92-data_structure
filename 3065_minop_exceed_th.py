class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        operation=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<k:
                operation+=1
        
        return operation
    
s=Solution()
print(s.minOperations(nums = [2,11,10,1,3], k = 10))


