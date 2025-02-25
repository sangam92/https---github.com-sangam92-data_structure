"""
1356. Sort Integers by The Number of 1 Bits
"""

class Solution:
    def sortByBits(self, arr):
        """
        res=[]
        new_res=[]
        arr.sort()
        for i in arr:
            res.append(bin(i)[2:])

        #for k in res:
         #   new_res.append(int(k,2))
        return sorted(res,key=res.count("1"))

        """
        arr.sort()
        return(sorted(arr,key = lambda x: bin(x)[2:].count("1")))


s=Solution()

print(s.sortByBits([0,1,2,3,4,5,6,7,8]))

