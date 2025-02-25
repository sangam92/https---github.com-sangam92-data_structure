"""
1304. Find N Unique Integers Sum up to Zero

"""

class Solution:
    def sumZero(self, n: int):
        if n==1:
            return [0]
        elif n%2==0:
            result=[]
            for i in range(1,n//2+1):
                result.append(i)
                result.append(-i)
        else:
            result=[]
            for i in range(1,n//2+1):
                result.append(i)
                result.append(-i)
            result.append(0)

        return result

s=Solution()
print(s.sumZero(5))


