class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        
        """
        averages = []
        nums.sort()
        l = int(len(nums)/2)
        for i in range(l):
            a = nums.pop(0)
            b = nums.pop()
            averages.append((a+b)/2)
        return min(averages)
    
s=Solution()
print(s.minimumAverage(nums = [7,8,3,4,15,13,4,1]))