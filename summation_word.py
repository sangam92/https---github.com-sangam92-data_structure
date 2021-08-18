"""
1880. Check if Word Equals Summation of Two Words
"""

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str):
        ch=""
        sum=""
        sum1=""
        sum2=""
        for i in firstWord:
            ch= str(ord(i) - 97)
            print(ch)
            sum+=ch

        for j in secondWord:
            ch =str(ord(j) -97)
            sum1+=ch

        res=int(sum) + int(sum1)
        print(res)

        for k in targetWord:
            ch = str(ord(k) - 97)
            sum2+=ch
        print(sum2)
        if int(res)==int(sum2):
            return True
        else:
            return False


s=Solution()
print(s.isSumEqual("acb","cba","cdb"))