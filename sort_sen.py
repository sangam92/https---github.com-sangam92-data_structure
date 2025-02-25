from collections import OrderedDict
class Solution:
    def sortSentence(self, s: str) -> str:
        s1=""
        val = s.split(" ")
        dic = {}
        for i in val:

            char = i[-1]
            word = i[:len(i)-1]
            print(char)
            dic[char]= word

        for k,v in sorted(dic.items()):
            s1+=v+" "

        return s1[:-1]
s=Solution()

print((s.sortSentence("is2 sentence4 This1 a3")))