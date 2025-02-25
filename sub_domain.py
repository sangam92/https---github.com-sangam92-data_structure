"""
Sub Domain visit computation

"""

class Solution:
    def subdomainVisits(self, cpdomains):
        dic={}
        for i in cpdomains:
            dom_split=i.split(" ")
            count=dom_split[0]
            string_domain = dom_split[1].split(".")
            print(count,string_domain)
            for j in string_domain:
                if j not in dic:
                    dic[j]=count
                else:
                    dic[j].append(count)
        print(dic)
        

s=Solution()

s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])