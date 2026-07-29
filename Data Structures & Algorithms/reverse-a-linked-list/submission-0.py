class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the link
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        return prev  
        