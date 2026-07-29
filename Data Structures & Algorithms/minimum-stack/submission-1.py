class MinStack:

    def __init__(self):
        self.min_arr=[]
        self.arr=[]
        

    def push(self, val: int) -> None:
        if len(self.min_arr) == 0 or self.min_arr[-1]>= val:
            self.min_arr.append(val)
        self.arr.append(val)       

    def pop(self) -> None:
        if self.min_arr[-1]==self.arr[-1]:
            self.min_arr.pop()
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
