"""
1403. Minimum Subsequence in Non-Increasing Order
"""
class Solution:
    def minSubsequence(self, nums):
        temp=[]
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if sum(nums[:i+1]) > sum(nums[i+1:]):
                temp.append(nums[:i+1])

        return temp[0]
s=Solution()
print(s.minSubsequence([4,3,10,9,8]))


