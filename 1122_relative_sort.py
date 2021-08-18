"""
1122 Relative Sort
"""

class Solution:
    def relativeSortArray(self, arr1, arr2):
        result=[]
        j=0
        extra = set(arr1).difference(set(arr2))
        for i in range(len(arr2)):
            for j in range(len(arr1)):

                if arr2[i]==arr1[j]:
                    #arr1.pop(i)
                    result.append(arr2[i])



        return result+list(extra)

s=Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))

