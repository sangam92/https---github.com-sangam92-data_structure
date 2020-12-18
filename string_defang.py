##defanf IP address

## 1.1.1.1 -> 1[.]1[.]1[.]1


class Solution:
    def defangIPaddr(self, address):

        address = address.replace('.','[.]')
        return address

s1= Solution()

new_address=s1.defangIPaddr('1.1.1.1')

print(new_address)
