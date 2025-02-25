"""
ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def insert(self,val):
        if self.head==None:
            self.head=ListNode(val)
        else:
            newnode=ListNode(val)
            newnode.next = self.head
            self.head = newnode


    def addtwonumbers(self,l1,l2):
        add_l1=[]
        add_l2=[]
        while(l1 is not None):

            add_l1.append(l1)
            l1 = l1.next
            add_l2.append(l2)
            l2 = l2.next
        s1 =[str(i) for i in add_l1]
        res1= int("".join(s1))
        s2 =[str(i) for i in add_l2]
        res2= int("".join(s2))

        final_sum = sum(res1,res2)

        return final_sum

if __name__ =="__main__":
    l1=Solution()
    l2=Solution()
    l1.insert(2)
    l1.insert(4)
    l1.insert(3)

    l2.insert(5)
    l2.insert(6)
    l2.insert(4)
    final=l1.addtwonumbers(l1,l2)
    print(final)
