"""
Trie Data Structure

"""
class TrieNode:
    def __init__(self):
        self.children=None
        self.iswordend=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currnode=self.root
        for ch in word:
            #dic.get(parameter, default value)
            node=currnode.children.get(ch,TrieNode())
            currnode.children[ch]=node
            currnode=node
        
        currnode.iswordend=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.

        we will start from root node and check for all the characters
        if we could not find a node for a character we will return False there
        once we iterate through all character we will check if that is a word end
        
        """
        currnode=self.root

        for ch in word:
            node=currnode.children.get(ch)
            if node is None:
                return False

        return currNode.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currnode=self.root

        for ch in prefix:
            node=currnode.children.get(ch)

            if not node:
                return False
            currnode=node
        
        return True
        

 