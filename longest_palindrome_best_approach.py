"""
5. Longest Palindromic Substring

"""
class Solution:

    def expand(self,left,right,s):
	    leftindex= 0
	    rigtindex =0
	    while(left >0 and right < len(s)):
		    if s[left]==s[right]:
			    leftindex=left
			    rigtindex=right
				
		    else:
			    break			
			left= left -1
			right = right + 1
		return [leftindex:rigtindex+1]
		
		
    def longestPalindrome(self, s):
	
	    for i in range(len(s)):
		    oddpalindrome =self.expand(i,i,s)
			evenpalindrome = self.expand(i,i+1,s)
			
		if len(oddpalindrome)>len(evenpalindrome):
		    return oddpalindrome
		else:
		    return evenpalindrome

s1 = Solution()
s="abcbabcb"
res=s1.longestPalindrome()
print(res)