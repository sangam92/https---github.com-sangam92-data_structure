"""
Add Word / Data Structure

"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}

    def addWord(self, word: str) -> None:
        self.dic[word]=word

    def search(self, word: str) -> bool:
        if '.' in  word and self.dic is not None:
            return True

        if word in self.dic.keys():
                return True
            else:
                return False
        else:
