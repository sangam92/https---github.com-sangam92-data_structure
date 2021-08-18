"""
16 . 3 Sum Closet

"""

class Solution:
    def threeSumClosest(self, nums, target: int):
        diff=0
        nums.sort()
        for i in range(len(nums)):
            x=i+1
            y =len(nums)-1

            while (x<y):

                res=nums[i]+nums[x]+nums[y]
                if abs(target - res) < abs(diff):
                    diff = target - sum
                if res < target:
                    x+=1
                        
                    
                else:
                    y-=1

            if diff == 0:
                break    
            
        return target-diff

s=Solution()

print(s.threeSumClosest([-1,2,1,-4],1))



        