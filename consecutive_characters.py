"""
1446. Consecutive Characters

"""
class Solution:
    def maxPower(self, s: str) -> int:
        max_val=1

        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count=count+1
            else:
                max_val=max(max_val,count)
                
                count=1
        return max(max_val,count)

s=Solution()
print(s.maxPower("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"))