class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n=len(citations)
        citations=sorted(citations) 

        for i in range(0,n):
            if citations[i]>=n-i:
                return n-i
        return 0

s=Solution()
print(s.hIndex(citations = [1,3,1]))     