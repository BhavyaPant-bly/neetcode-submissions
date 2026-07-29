class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size=0
        self.arr=[-1]*capacity

    def get(self, i: int) -> int:
        if(self.size<=i):
          return -1
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if(self.size<=i):
          return
        self.arr[i]=n


    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()
        self.arr[self.size]=n
        self.size+=1

    def popback(self) -> int:
        self.size-=1
        return self.arr[self.size]

    def resize(self) -> None:
        self.arr=self.arr+[0]*self.capacity
        self.capacity=self.capacity*2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity