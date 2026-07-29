class Node:
    def __init__(self,key:int, val:int, next: None, prev: None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head=None
        self.tail=None
        self.capacity=capacity
        self.cache={}

    def get(self, key: int) -> int:
        return self.update(key)

    def update(self, key:int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        if self.head == self.tail or node == self.tail:
            return node.val
        elif node == self.head:
            self.head=self.head.next
            self.head.prev=None
        else:
            # detach node
            node.prev.next=node.next
            node.next.prev=node.prev
        # add node as recently visited
        node.next=None
        self.tail.next=node
        node.prev=self.tail
        self.tail=node
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val=value
            self.update(key)
        else:
            node=None
            if len(self.cache)==self.capacity:
               node=self.head
               self.head=self.head.next
               node.next=None
               if self.head:          # If there's still a node left, sever the backlink
                    self.head.prev = None
               else:                  # If the cache is now completely empty (capacity == 1)
                    self.tail = None
               del self.cache[node.key]
            if self.head== None:
                node = Node(key,value,None,None)
                self.tail=self.head = node
            else:
                node = Node(key,value,None,self.tail)
                self.tail.next=node
                self.tail=node
            self.cache[key]=node

        
