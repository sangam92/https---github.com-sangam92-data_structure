"""
Three Sum Problem

"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=set()
        for i in range(len(nums)-2):
            x=i+1
            
            y=len(nums)-1

            while x<y:
                if nums[x]+nums[y]+nums[i]==0:
                    res.add((nums[x],nums[y],nums[i]))
                    
                    x+=1
                    y-=1
                   
                elif nums[x]+nums[y]+nums[i]<0:
                    x+=1
                else:
                    y-=1
        return list(res)
s=Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))

