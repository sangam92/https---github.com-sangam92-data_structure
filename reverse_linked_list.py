"""
Reverse Linked List

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node=head
        res=[]
        while node is not None:
            res.append(node.val)
            node=node.next
        
        res=res[::-1]
    
        i=1
        curr = ListNode(res[0])
        head = curr
        # iterating over input list
        for i in res[1:]:
          temp = ListNode(i)
          curr.next = temp
          curr = temp

        return head

head=ListNode(10)
head.next=ListNode(11)
head.next.next=ListNode(12)
s=Solution()
print(s.reverseList(head))      