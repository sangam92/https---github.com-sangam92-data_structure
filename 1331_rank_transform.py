"""
Rank Transform in a array
"""

class Solution:
    def arrayRankTransform(self, arr):
        res =[]
        dic={}
        arr1=sorted(set(arr))
        for i in range(len(arr1)):
            if arr1[i] not in dic:
                dic[arr1[i]]=i+1

        for i in range(len(arr)):
            res.append(dic.get(arr[i]))

        return res

s=Solution()
print(s.arrayRankTransform([40,10,20,30]))
print(s.arrayRankTransform([37,12,28,9,100,56,80,5,12]))
