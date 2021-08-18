"""
500. Keyboard Row

"""
class Solution:
    def findWords(self, words):
        list1=[]
        list2=[]
        for i in words:
            list1.clear()
            for j in i:
                if str(j).lower() in "qwertyuiop":
                    list1.append("qwertyuiop")
                elif str(j).lower() in "asdfghjkl":
                    list1.append("asdfghjkl")
                else:
                    list1.append("zxcvbnm")
           
            if len(set(list1))==1:
                list2.append(i)
                
        return list2

s=Solution()
print(s.findWords(["Hello","Alaska","Dad","Peace"]))