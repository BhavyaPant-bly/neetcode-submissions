class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Map to store: { Old_Node : New_Node_Copy }
        old_to_new = {}
        
        # Pass 1: Create all the new nodes (without wiring pointers yet)
        temp = head
        while temp:
            old_to_new[temp] = Node(temp.val)
            temp = temp.next
            
        # Pass 2: Wire up the next and random pointers
        temp = head
        while temp:
            # old_to_new[temp] is our copied node
            # We look up its next and random nodes in our map
            old_to_new[temp].next = old_to_new.get(temp.next)
            old_to_new[temp].random = old_to_new.get(temp.random)
            temp = temp.next
            
        # Return the copy of the head node
        return old_to_new[head]