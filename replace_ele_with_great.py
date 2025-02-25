"""
1299. Replace Elements with Greatest Element on Right Side

"""

class Solution:
    def replaceElements(self, arr):
        res=[]
        for i in range(1,len(arr)):
           
            sort_ele=max(arr[i:])
            res.append(sort_ele)
            print(sort_ele)
        res.append(-1)
        return res
s=Solution()
print(s.replaceElements([17,18,5,4,6,1]))
        