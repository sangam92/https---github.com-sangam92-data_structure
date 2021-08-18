"""
1464. Maximum Product of Two Elements in an Array

"""

class Solution:
    def maxProduct(self, nums) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
        
        return (int(MAX_2)-1) * (int(MAX_1)-1)

      
s=Solution()

print(s.maxProduct([3,4,5,2]))


  