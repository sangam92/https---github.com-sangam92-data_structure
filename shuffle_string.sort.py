"""
1528. Shuffle String

"""

class Solution:
    def restoreString(self, s: str, indices) -> str:
        dic ={}
        res=""
        for i in range(len(indices)):
            dic[indices[i]]=s[i]
        

        for i in sorted(dic.keys()):
            res+=dic[i]
        return res
            

s=Solution()

print(s.restoreString("codeleet",[4,5,6,7,0,2,1,3]))

