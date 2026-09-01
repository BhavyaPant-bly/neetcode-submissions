class Solution:
    def cal_square(self,n: int) -> int:
        sq=0
        while n:
            c=n%10
            sq+=c*c
            n//=10
        return sq

    def isHappy(self, n: int) -> bool:
        present=set()
        while True:
            sq=self.cal_square(n)
            if sq == 1:
                return True
            elif sq in present:
                return False
            present.add(sq)
            n=sq
        return True

        