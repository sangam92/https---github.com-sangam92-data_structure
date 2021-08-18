
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char in ["(","{","["]:
                stack.append(char)
            
            else:
                if len(stack)==0:
                    return False
                currchar = stack.pop()
                if currchar =="(":
                    if char !=")":
                        return False
                if currchar == "{":
                    if char != "}":
                        return False
                if currchar == "[":
                    if char != "]":
                        return False
        if stack:
            return False
        else:
            return True
 

if __name__ == "__main__":
    exprs = "]"
    s=Solution()
    print(s.isValid(exprs))
