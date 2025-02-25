class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic={}
        for i  in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        res=[]
        count=0
        for i,v in sorted(dic.items(),key=lambda v:v[1],reverse=True):
            if count<k:
                res.append(i)
                count+=1
        return res
    
s=Solution()
print(s.topKFrequent( nums = [1,1,1,2,2,3], k = 2))