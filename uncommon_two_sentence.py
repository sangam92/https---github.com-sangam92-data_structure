"""
884. Uncommon Words from Two Sentences
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        dic={}
        res=[]
        s1=list((s1+" " +s2).split(" "))

        for i in s1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        for i,v in dic.items():
            if v==1:
                res.append(i)

        return res

s=Solution()
print(s.uncommonFromSentences( "this apple is sweet","this apple is sour"))