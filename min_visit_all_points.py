"""
min to visit all points

"""

class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        sum=0
        for i in range(len(points)-1):
            diff1=abs(points[i][0] - points[i+1][0])
            diff2= abs(points[i][1]-points[i+1][1])
            if diff1 > diff2:
                sum= sum+ diff1
            else:
                sum= sum+ diff2
        return sum

s=Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))


        