"""
Slowest Key
"""
class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        temp=[releaseTimes[0]]

        for i in range(1,len(releaseTimes)):
            temp.append(releaseTimes[i]-releaseTimes[i-1])
        res=""
        for i in range(len(temp)):
            if temp[i]==max(temp):
               #idx.append(i)
                res+=keysPressed[i]

        return max(res)

s=Solution()
print(s.slowestKey([9,29,49,50],"cbcd"))
