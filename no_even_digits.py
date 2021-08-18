"""
No of even digits

"""

class Solution:
    def findNumbers(self, nums) -> int:
        str1=""
        count=0
        for i in nums:
            
            str1=str(i)
            if len(str1)%2==0:
                count=count+1
        return count

s=Solution()
print(s.findNumbers([12,345,2,6,7896]))
            
 