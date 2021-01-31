"""
832. Flipping an Image

"""

class Solution:
    def flipAndInvertImage(self, A):
        B=[]
        for i in range(len(A)):
            B.append(A[i][::-1])

        for j in range(len(B)):
            for k in range(len(B[j])):
                print(B[j][k])
                if B[j][k]==0:
                    
                    B[j][k]=1
                else:
                    B[j][k]=0
            
  
        return B

s=Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

        