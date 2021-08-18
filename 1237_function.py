"""
1237. Find Positive Integer Solution for a Given Equation

"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        if customfunction==1:
            result=[]
            for i in range(0,z-1):
                if ((i+1) + z-i-1) ==z:
                    result.append([i+1,z-i-1])
            return result
        elif customfunction==2:
            result.append([i,z],[z,i])
            return result
s=Solution()
print(s.findSolution(1,5))
        
            

