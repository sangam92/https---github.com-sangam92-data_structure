"""
8. String to integer

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = [1,2,3,4,5,6,7,8,9,0,'-']
        if len(s)> 200 or len(s) < 0:
            return 0
        else:
            print("length is ok")
            str1=s.strip(" ")

            if str1[1] not in numbers:
                return 0
            else:

        return s1



s1=Solution()
print(s1.myAtoi("  -42"))
