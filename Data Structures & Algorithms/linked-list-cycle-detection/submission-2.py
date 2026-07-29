class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # As long as fast and fast.next are valid, we can safely move 2 steps
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if fast == slow:          # Cycle detected!
                return True
                
        return False                  # fast reached the end, so no cycle exists