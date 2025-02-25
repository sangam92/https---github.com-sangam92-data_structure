"""
1200. Minimum Absolute Difference
"""

class Solution:
    def minimumAbsDifference(self, arr):

        arr=sorted(arr)
        x=0
        y=len(arr)-1
        new_arr =[]
        mi=abs(arr[i+1]-arr[i])
        for i in range(1,len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff <= mi:

                new_arr.append([arr[i+1],arr[i]])
                mi=diff






