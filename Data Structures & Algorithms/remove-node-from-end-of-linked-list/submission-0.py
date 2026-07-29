# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.counter=0
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            self.counter = n
            return None
        head.next=self.removeNthFromEnd(head.next,n)
        if self.counter == 1:
            head=head.next
        self.counter-=1
        return head
        
        
        