"""
1078. Occurrences After Bigram

"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        text=text.split(" ")
        res=[]
        for i in range(len(text)-2):
            if first==text[i] and second==text[i+1]:
                res.append(text[i+2])
        return res


s=Solution()

print(s.findOcurrences("alice is a good girl she is a good student","a","good"))