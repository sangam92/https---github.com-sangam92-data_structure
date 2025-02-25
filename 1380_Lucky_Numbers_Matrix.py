"""
1380. Lucky Numbers in a Matrix
"""

class Solution:
    def luckyNumbers (self, matrix):
        """
        max_val=0
        col=0
        for i in range(len(matrix)):
            if max_val < max(matrix[i]):
                max_val,col=max(matrix[i]),i

        return [min(matrix[col])]
        """

        mi={min(r) for r in matrix}
        print(mi)
        ma={max(c) for c in zip(*matrix)}
        print(ma)
        return mi & ma

s=Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(s.luckyNumbers([[7,8],[1,2]]))
print(s.luckyNumbers([[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]))