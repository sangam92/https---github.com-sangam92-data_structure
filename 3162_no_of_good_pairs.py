class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        total_count=0
        for number in nums1:
            for number2 in nums2:
                if number%(number2*k) ==0:
                    total_count+=1
        return total_count

s=Solution()
print(s.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
print(s.numberOfPairs( nums1 = [1,2,4,12], nums2 = [2,4], k = 3))