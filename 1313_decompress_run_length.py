"""
1313. decompress run length encoded

"""

class Solution:
    def decompressRLElist(self, nums):
        new_list=[]
        for i in range(0,len(nums),2):
            print(nums[i])
            for j in range(0,nums[i]):
                print(j)
                new_list.append(nums[i]+1)
        return new_list

s=Solution()
print(s.decompressRLElist([1,2,3,4]))



