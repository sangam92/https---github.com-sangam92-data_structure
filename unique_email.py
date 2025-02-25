"""
Unique Email Address

"""

class Solution:
    def numUniqueEmails(self, emails) -> int:
        list1=[]
        for i in emails:
            k,j=i.split('@')
            k2= k.split('+')
            k1=k2[0].replace('.','')
            k1=k1+'@'+j
            list1.append(k1)
        
        return len(set(list1))
s=Solution()

print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))