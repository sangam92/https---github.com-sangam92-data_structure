"""
844 . backspace String Compare

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while '#' in s or '#' in t:
            if '#' in s:
                x = s.index('#')
                if x - 1 < 0:
                    s = s[x+1:]
                else:
                    s = s[:x-1] + s[x+1:]
            if '#' in t:
                x = t.index('#')
                if x - 1 < 0:
                    t = t[x+1:]
                else:
                    t = t[:x-1] + t[x+1:]
        return s == t

s=Solution()
print(s.backspaceCompare("ab##","c#d#"))
            