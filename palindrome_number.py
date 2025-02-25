"""
9. Palindrome number

"""

def palindrome_check(n,x):
    
    if n==x:
        return True
    else:
        return False

class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        rev,pop=0,0
        y=x
        if x < 0:
            return False
        while x > 0:
            

            pop = x%10
            x=x//10
            rev = rev*10+ pop
       
        return palindrome_check(rev,y)

s=Solution()
print(s.isPalindrome(10))
            
