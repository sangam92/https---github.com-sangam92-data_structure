class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        MAX_COUNTER=0
        for i in nums:
            counter=0
            if i-1 not in nums:
                counter+=1
                i+=1
                
                while i in nums:
                    counter+=1
                    i+=1
            
            MAX_COUNTER=max(MAX_COUNTER,counter)
                
          
        return MAX_COUNTER
    
s=Solution()
print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
