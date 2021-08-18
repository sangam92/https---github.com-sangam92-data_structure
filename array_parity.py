"""
905. Sort Array By Parity
"""

class Solution:
    def sortArrayByParity(self, A):
        new_a=[]
        for i in A:
            
            if i%2==0:
                new_a.append(i)
        for i in A:
            if i%2==1:
                new_a.append(i)
        
        
        return new_a 

s=Solution()

print(s.sortArrayByParity([3,1,2,4]))

