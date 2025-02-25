"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i+1
        return -1
        
s=Solution()

print(s.isPrefixOfWord("i love eating burger","burg"))

