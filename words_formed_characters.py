"""
1160. Find Words That Can Be Formed by Characters

"""

class Solution:
    def countCharacters(self, words, chars: str) -> int:
        res=0
        count=0
        for i in words:
            
            res=res+count
            count=0
            chars_temp=chars
        


            for j in i:
                if j not in chars_temp:
                    count=0
                    break
                else:   
                    count+=1
                    chars_temp=chars_temp.replace(j,'',1)
        return res

s=Solution()
print(s.countCharacters(["hello","world","leetcode"],"welldonehoneyr"))
