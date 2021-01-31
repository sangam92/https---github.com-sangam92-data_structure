"""
10. Regular Expression Matching

"""

def all_check(s):
    for i in s:
        if i == '*':
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) < 0 or len(s) > 20:
            return 'false'
        if len(p) < 0 or len(p) > 30:
            return 'false'
        if s.isupper:
            return 'false'
        if p.isupper:
            return 'false'
        for i in p:
            

