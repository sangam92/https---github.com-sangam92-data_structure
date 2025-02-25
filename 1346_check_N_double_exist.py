"""
1346. Check If N and Its Double Exist
"""

class Solution:
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                print(2*j,i)
                if 2*arr[j]==arr[i] and i!=j:
                    return True
        else:
            return False

s=Solution()
print(s.checkIfExist([-2,0,10,-19,4,6,-8]))



