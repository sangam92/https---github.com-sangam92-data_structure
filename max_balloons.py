"""
1189. Maximum Number of Balloons

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        for i in text:
            if i in ['b','a','l','o','n']:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
        count=0
        if len(dic) < 5 or dic['l'] == 1 or dic['o'] == 1:
            return 0
        dic['l'] = int(dic['l'] / 2)
        dic['o'] = int(dic['o'] / 2)
        return min(dic.values())
s=Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))
        
