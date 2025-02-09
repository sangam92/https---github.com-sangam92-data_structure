class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        return [self.findFirst(nums, target), self.findLast(nums, target)]

    def findFirst(self, nums, target: int) -> int:
        idx, start, end = -1, 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == target:
                idx = mid
        return idx

    def findLast(self, nums, target: int) -> int:
        idx, start, end = -1, 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
            if nums[mid] == target:
                idx = mid
        return idx
s=Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
