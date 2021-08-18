"""
1441. Build an Array With Stack Operations
"""

class Solution:
    def buildArray(self, target, n: int):
        stack=[]
        for i in range(1,n+1):
            if i in target:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")
            if(i==(target[-1])):
                break

        return stack

s=Solution()
print(s.buildArray([1,3],3))
