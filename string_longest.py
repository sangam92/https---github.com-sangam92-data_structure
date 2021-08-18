"""
longest sub string

"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0

        dct ={}
        max_length=start=0

        for i in range(len(s)):
            if s[i] in dct and start <=dct[s[i]]:
                    print(dct[s[i]])
                    start=dct[s[i]] + 1
            else:
                max_length = max(max_length,i-start +1 )
            dct[s[i]] =i
        return max_length


s1=Solution()
res=s1.lengthOfLongestSubstring("abcbacba")
print(res)
