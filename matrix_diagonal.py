"""
Matrix Diagonal Sum

"""

class Solution:
    def diagonalSum(self, mat) -> int:
        sum =0
        for i in range(len(mat)):

            sum = sum + mat[i][i]
            sum= sum + mat[i][-i-1]
        if len(mat) %2!=0:
            return sum - mat[len(mat)//2][len(mat)//2]
        else:

            return sum
s=Solution()

print(s.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))
        