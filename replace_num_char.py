"""
1844. Replace All Digits with Characters
"""

class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        s1=""
        for i in range(len(s)):
            if i%2==0:
                idx=alpha.index(s[i-1])
                print(s[i-1])
                val= s[i-1+idx]
                s1+=val
            else:
                s1+=s[i]

        return s1
s=Solution()
print(s.replaceDigits("a1c1e1"))