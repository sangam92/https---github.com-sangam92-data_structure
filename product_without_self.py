"""
product without self

"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
            print(output)
            #[1,1,2,6]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            print("output",output[i],p)
            p = p * nums[i]
            print("product p ,nums[i]",p,nums[i])
        return output


s=Solution()

print(s.productExceptSelf([1,2,3,4]))

[1,1,2,6]

[24,12,4,1]

[24,12,8,6]