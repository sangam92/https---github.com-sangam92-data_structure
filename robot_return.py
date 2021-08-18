"""
657 . Robot return to origin

"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l=r=u=d=0
        for i in moves:
            if i=='L':
                l=l+1
            elif i =='R':
                r=r+1
            elif i=='U':
                u=u+1
            elif i=='D':
                d=d+1
            else:
                print("Wrong Input")
        if l==r and u==d:
            return True
        else:
            return False
s=Solution()
print(s.judgeCircle("UD"))