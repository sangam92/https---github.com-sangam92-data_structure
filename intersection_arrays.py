"""
349. Intersection of Two Arrays

"""

class Solution:
    def intersection(self, nums1, nums2):
        dic={}

        nums1=set(nums1)
        nums2=set(nums2)

        return list(nums1.intersection(nums2))
        
s=Solution()

print(s.intersection([1,2,2,1],[2,2]))