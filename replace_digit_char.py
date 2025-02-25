"""
1844. Replace All Digits with Characters
"""

class Solution:
    def replaceDigits(self, s: str):
        new_s=""
        for i in s:
            if i.isalpha():
                store = ord(i)
                new_s+=i
            else:
                print(i,store)
                new_s+=chr(store+int(i))
        return new_s


s=Solution()
print(s.replaceDigits("a1c1e1"))
