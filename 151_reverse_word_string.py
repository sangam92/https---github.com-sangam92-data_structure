class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        word= s.split()
        for i in range(len(word)-1,-1,-1):
            res=res+word[i]
            res=res+' '
        return res.strip()



s=Solution()
print(s.reverseWords(s = "a good   example"))