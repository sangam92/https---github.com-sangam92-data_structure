"""
Merge Two Sorted List

"""

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        while l1 or l2:
            if l1:
                arr.append(l1.val)
                l1 = l1.next
            if l2:
                arr.append(l2.val)
                l2 = l2.next
        arr.sort()
        if len(arr)>0:
            l3 = ListNode(arr[0], None)
            itr = l3
            for i in arr[1:]:
                node = ListNode(i, None)
                itr.next = node
                itr = itr.next
            return l3
        return None

            
        
     
s=Solution()
print(s.mergeTwoLists([1,2,4],[1,3,4]))