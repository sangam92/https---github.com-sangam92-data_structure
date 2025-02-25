"""
922. Sort Array By Parity II

"""


class Solution:
    def sortArrayByParityII(self, nums):

        result=[None] * len(nums)
        x=0
        y=1

        for i in nums:
            if i%2==0:
                result[x]=i
                x+=2
            else:
                result[y]=i
                y+=2
        return result

s=Solution()

print(s.sortArrayByParityII([3,4]))


        
