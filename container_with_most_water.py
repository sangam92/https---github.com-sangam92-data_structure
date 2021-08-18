"""
11. Container With Most Water

"""

class Solution:
    def maxArea(self, height) -> int:
        area=0
        max_area=0
        left=0
        right= len(height)-1

        while left < right:
            w=right-left
            h=min(height[left],height[right])
            area= w*h
            max_area=max(max_area,area)
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
s=Solution()

print(s.maxArea([1,8,6,2,5,4,8,3,7]))