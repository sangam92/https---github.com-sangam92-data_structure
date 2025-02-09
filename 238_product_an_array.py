class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=1
        n=len(nums)
        output=[]

        for i in range(0,n):
            output.append(p)
            p=p*nums[i]
        p=1

        for j in range(n-1,-1,-1):
            output[j]=p*output[j]
            p=p*nums[j]
        return output




s=Solution()
print(s.productExceptSelf( nums = [1,2,3,4]))

print(s.productExceptSelf(nums = [-1,1,0,-3,3]))

print(s.productExceptSelf(nums = [0,0]))
