# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            return list1 if list1 != None else list2
        list3=None

        while list1 and list2:
            if list1.val<list2.val:
                temp=list1
                list1=list1.next
            else:
                temp=list2
                list2=list2.next
            if list3 == None:
                list3 = temp
                tail = temp
            else:
                tail.next = temp
                tail=tail.next
        
        temp = list2 if list2 != None else list1
        while temp:
            tail.next=temp
            tail=temp
            temp=temp.next
        return list3