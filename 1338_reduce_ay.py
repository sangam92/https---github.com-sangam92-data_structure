"""
1338. Reduce Array Size by Half
"""

class Solution:
    def minSetSize(self, arr):
        arr_len=(len(arr)-1)//2
        dic={}

        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        sum=0
        count=0
        for key,val in sorted(dic.items(),key = lambda x: x[1], reverse = True):
            if sum >arr_len:
                return count
            else:
                sum+=val
                count+=1
        return count


s=Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7]))
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))
print(s.minSetSize([1000,1000,3,7]))