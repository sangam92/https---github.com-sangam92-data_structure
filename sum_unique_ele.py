"""
1748. Sum of Unique Elements

"""

class Solution:
    def sumOfUnique(self, nums) -> int:
        dic ={}
        count=0
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
       
        for key,value in dic.items():
            if value==1:
                count=count+key
           

        
        return count

s=Solution()
print(s.sumOfUnique([1,2,3,2]))
