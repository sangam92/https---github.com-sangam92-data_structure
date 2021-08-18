class Solution:
    def removeDuplicates(self, s: str):
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

s=Solution()
print(s.removeDuplicates("abbaca"))