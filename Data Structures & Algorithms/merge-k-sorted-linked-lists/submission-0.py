# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans,tail=None, None
        while True:
            cont=False
            for l in lists:
                cont|=(l!=None)
            if cont == False:
                break
            min_val=None
            min_ind=-1
            for ind,l in enumerate(lists):
                if l!=None and (min_val==None or l.val < min_val.val):
                    min_val=l
                    min_ind=ind
            lists[min_ind]=lists[min_ind].next
            min_val.next=None
            if ans==None:
                ans=min_val
                tail=min_val
            else:
                tail.next=min_val
                tail=tail.next
        return ans
                