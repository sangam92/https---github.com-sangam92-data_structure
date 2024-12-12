from collections import Counter
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        countDict=Counter(wordDict)
        tempWord=""
        for key in countDict:
            tempWord+=key
        if tempWord==s:
            return True
        return False
    
s=Solution()
print(s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))