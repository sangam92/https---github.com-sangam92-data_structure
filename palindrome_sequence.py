"""
1332. Remove Palindromic Subsequences

"""



class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s=="":
            return 0
        elif s==s[::-1]:
            return 1
        else:
            return 2

s=Solution()
print(s.removePalindromeSub("ababa"))