"""
80. Remove Duplicates from Sorted Array II

"""

class Solution:
    def removeDuplicates(self, nums):
        prev=nums[0]
        count=1
        idx=1
        while idx < len(nums):
            if prev==nums[idx]:
                if count < 2:
                    count+=1
                    idx+=1
                else:
                    nums.pop(idx)
            else:
                prev=nums[idx]
                count=1
                idx+=1
        return idx


s=Solution()

print(s.removeDuplicates([1,1,1,2,2,3]))
            
