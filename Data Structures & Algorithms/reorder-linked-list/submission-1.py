# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorder(self,head: Optional[ListNode],original: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return original
        ans=self.reorder(head.next,original)
        if ans == None:
            return None
        temp=ans.next
        ans.next=head
        head.next=temp
        if (temp.next == head):
            temp.next = None
            return None
        return temp
    def reorderList(self, head: Optional[ListNode]) -> None:
       if head.next != None:
        self.reorder(head,head)
        