class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]  # Start with the first string

        for s in strs[1:]:
            while not s.startswith(prefix):  # Trim prefix if no match
                prefix = prefix[:-1]
                if not prefix:  # If prefix becomes empty, return ""
                    return ""

        return prefix






s=Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))