"""
739. Daily Temperatures
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        res=[]
        if len(temperatures)==1:
            return [0]
        for i in range(len(temperatures)):
            count=1
            for j in range(i,len(temperatures)):
            #    if j==len(temperatures)-1:
            #       res.append(0)
                if temperatures[i] < temperatures[j]:
                    res.append(count)
                    break
                else:
                    count+=1
        return res

s=Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))

