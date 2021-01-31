"""
5. Longest Palindromic Substring

"""


class Solution:
    def longestPalindrome(self, s):
	    list_str=[]
	    pal=[]
	    for i in range(len(s)):
		    for j in range(1,len(s)):
			    list_str.append(s[i:j+1])
		
	    for i in list_str:
		    if i==i[::-1]:
			    pal.append(i)
	    pal = max(pal,key=len)
	    return pal

		
		
s1=Solution()
s="google"
res=s1.longestPalindrome(s)
print(res)
			
		
        