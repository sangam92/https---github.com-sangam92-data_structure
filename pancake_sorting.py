"""
969. Pancake Sorting

"""

class Solution:
    def pancakeSort(self, A):

        len_A = len(A)
        answer = []

        for a in range(len_A, 0, -1):
            idx = A.index(a)
            if idx < a - 1:
                if idx > 0:
                    A[:idx + 1] = A[:idx + 1][::-1]
                    answer.append(idx + 1)
                A[:a] = A[:a][::-1]
                answer.append(a)
        return answer

s=Solution()


print(s.pancakeSort([3,2,4,1]))

        


