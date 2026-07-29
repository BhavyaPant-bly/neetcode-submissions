            # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        l3=None
        tail=None

        while l1 and l2:
            sum_val=l1.val+l2.val+c
            c=sum_val//10
            node = ListNode(sum_val%10,None)

            if  not l3:
                l3=node
                tail=node
            else:
                tail.next=node
                tail=node
            l1=l1.next
            l2=l2.next

        l=l1 if l1 else l2

        while l:
            sum_val=l.val+c
            c=sum_val//10
            node = ListNode(sum_val%10,None)
            tail.next=node
            tail=node
            l=l.next
        if c:
           node = ListNode(c,None)
           tail.next=node
           tail=node 
        return l3
        