"""
13. Roman to Integer

"""
dictionary={
        'I':1,
        'V':4,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000


    }

dictionary1={
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900
    }




class Solution:
 
    def romanToInt(self, s: str) -> int:
        sum = 0
        i=0
        while (i < len(s)):
            #print(s[i])
            #print(s[i])
            for j in range(len(s)-1):
                char1=(s[j]+s[j+1])
                print(char1)
                if char1 in dictionary1.keys():
                     sum = sum + dictionary1[char1]
                     i =i+2
                else:
            
                    sum = sum + dictionary[s[i]]

                    i=i+1        
        return sum
s= Solution()
print(s.romanToInt("MCMXCIV"))