class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic={}
        counter=0
        for _ in range(len(nums)):
            if nums[_] not in dic.values():
                dic[counter]=nums[_]
                counter+=1
        
        print(dic)

        for k,v in dic.items():
            nums[k]=v
        return counter
    

s=Solution()
print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))


