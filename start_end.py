"""
1450. Number of Students Doing Homework at a Given Time

"""

class Solution:
    def busyStudent(self, startTime, endTime, queryTime) -> int:
        count=0
        for i in range(len(startTime)):
            
            if startTime[i] < queryTime and endTime[i] > queryTime:
                count=count+1
        return count

s=Solution()

print(s.busyStudent([1,2,3],[3,2,7],4))

        