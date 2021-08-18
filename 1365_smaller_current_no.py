"""
1365. Numbers smaller than current Numbers

"""
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result=[]
        for i in nums:
            count=0
            for j in  nums:
                if i > j:
                    count=count+1
            result.append(count)
        return result
s=Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))