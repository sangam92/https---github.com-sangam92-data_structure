"""
Find Common Charaters

"""

class Solution:
    def commonChars(self, A):
        dic={}
        A1=sorted(A)
        for i,c in enumerate(A1[0]):
            for j in range(1,len(A)):
                print(c,A[j][i])
                if c in A[j][i]:
                    dic[c]=1
        print(dic)

s=Solution()

s.commonChars(["bella","label","roller"])

        