class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
       self.head= None  

    
    def get(self, index: int) -> int:
        curr=self.head
        i=0
        for _ in range(index):
            if (curr is None):
                return -1
            curr=curr.next
        return -1 if curr is None else curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next=self.head
        self.head=node

    def insertTail(self, val: int) -> None:
        node=self.head
        tail=Node(val)
        if self.head is None:
            self.head=tail
            return
        
        while(node.next):
            node=node.next
        node.next=tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head=self.head.next
            return True
        temp = self.head
        i=0
        while i < index-1:
            if temp.next is None:
                return False
            temp=temp.next
            i+=1
        if temp.next is None: 
            return False
        temp.next=temp.next.next
        return True
        

    def getValues(self) -> List[int]:
        if self.head is None:
            return []
        arr = []
        temp = self.head
        while(temp != None):
            arr.append(temp.val)
            temp=temp.next
        return arr
