"""
557. Reverse String

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        part = s.split(" ")
        result=[]
        for i in part:
            result.append(i[::-1])
        str_res=" ".join(result)
        return str_res

s=Solution()

print(s.reverseWords("Let's take LeetCode contest"))