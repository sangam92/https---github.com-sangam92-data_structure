"""
8. String to integer

"""
def bit_test(s):
    if int(s) < -2 ** 31:
        return -2 ** 31
    if int(s) > 2 ** 31:
        return 2 ** 31
    return s
def conv_string(s):
    res1=""
    res1=''.join(s)
    return res1

class Solution:
    def myAtoi(self, s: str) -> int:
        res=[]
        numbers = ['1','2','3','4','5','6','7','8','9','0','-']
        if len(s)> 200 or len(s) < 0:
            return 0
        #elif int(s) > (2**31)-1 or int(s) < -(2**31):
        #    return -(2**31)

        else:
            #print("length is ok")
            str1=s.strip(" ")

            if str1[1] not in numbers:
                #print("checking",str1[1])
                return 0
            else:
                for i in str1:
                    if i in numbers:
                        res.append(i)
                        #print("appending")
                        res2=conv_string(res)
                        bit_test(res2)
                        #if int(res1) > (2**31)-1 or int(res1) < -(2**31):
                        #    return -(2**31)

                    else:
                        #print("break")

                        break


            return res2



s1=Solution()
print(s1.myAtoi("-91283472332"))
