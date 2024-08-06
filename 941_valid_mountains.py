class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False

        x=0
        y=len(arr)-1

        while x < y:
            if arr[x] < arr[x+1]:
                x=x+1
          
            elif arr[y] <  arr[y-1]:
                y=y-1
            else:
                break          
        return x==y and (x>0 and y<len(arr)-1)
    
s=Solution()
print(s.validMountainArray(arr = [0,3,2,1]))
print(s.validMountainArray(arr = [3,5,5]))
print(s.validMountainArray(arr =[0,1,2,3,4,5,6,7,8,9]))