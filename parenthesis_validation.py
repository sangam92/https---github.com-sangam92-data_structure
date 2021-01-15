"""
Nesting Depth of paranthesis
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        
        if s=="":
            return 0
        count=0
        dep_count=0
        for i in s:
            if i=="(" :
                
                count=count+1
            if i == ")":
                count =count-1
            dep_count=max(dep_count,count)
            
        return dep_count
                    
s=Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))

