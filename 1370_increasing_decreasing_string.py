"""
1370. Increasing Decreasing String

"""

class Solution:
    def sortString(self, s: str) -> str:
        """
        new_s=""
        new_t=""
        for i in s:
            if i not in new_s:
                new_s+=i
            else:
                new_t+=i
        new_s=sorted(new_s)
        new_s="".join(new_s)
        new_t="".join(new_t)
        new_s=new_s + new_t


        return new_s
        """

        s = list(s)
        result = ''
        while s:
            for letter in sorted(set(s)):
                print(sorted(set(s)))
                s.remove(letter)
                result += letter
            """
            for letter in sorted(set(s), reverse=True):
                s.remove(letter)
                result += letter
            """
        return result
s=Solution()
print(s.sortString("aaaabbbbcccc"))