from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagarams =defaultdict(list)

        for word in strs:
            sorted_word=tuple(sorted(word))
            anagarams[sorted_word].append(word)

        return list(anagarams.values())
      
    
s=Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))