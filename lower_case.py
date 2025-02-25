"""
lower case

""" 
class Solution:
    def toLowerCase(self, s: str) -> str:
        new_str=""
        for i in s:
            ord_num =ord(i)
            if 64 < ord_num < 91:
                ord_num=ord_num + 32
                s=s.replace(i,chr(ord_num))
        return s
s= Solution()
print(s.toLowerCase("Hello"))