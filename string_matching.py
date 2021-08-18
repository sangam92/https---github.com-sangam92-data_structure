"""
1408. String Matching in an Array

"""

class Solution:
    def stringMatching(self, words):
        count=[]
        for i in range(len(sorted(words))-1):
            if words[i] in words[i+1:]:
                count.append(words[i])
        return count

s=Solution()
print(s.stringMatching(["mass","as","hero","superhero"]))

    


        