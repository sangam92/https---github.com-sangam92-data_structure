"""
Median of two sorted array

"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        num = nums1 + nums2
        num = sorted(num)
        len_num = len(num)

        if len_num%2==1:
            return num[len_num/2]
        else:
            val= num[len_num/2-1]+ num[(len_num/2)]
            return round(val,2)/2



s1=Solution()
nums1=[1,2]
nums2=[3,4]
res=s1.findMedianSortedArrays(nums1,nums2)
print(res)
