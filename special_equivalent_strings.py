"""
893. Groups of Special-Equivalent Strings

"""

class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        l=[]
        for s in A:
            even=""
            odd=""
            for i in range(len(s)):
                if i%2!=0:
                    odd+=s[i]
                    
                else:
                    even+=s[i]
                    
            odd = ''.join(sorted(odd))
            even = ''.join(sorted(even))
            l.append(str(odd)+str(even))
            print(odd)
            print(even)
            print(l)


s=Solution()
s.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])





