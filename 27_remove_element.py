"""
27. Remove Element

"""

class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0:
            return 0
        
        else:
            i=0           
            while i in range(len(nums)):
                if nums[i]==val:
                    nums.remove(val)
                else:
                    i=i+1
            return len(nums)
s=Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))