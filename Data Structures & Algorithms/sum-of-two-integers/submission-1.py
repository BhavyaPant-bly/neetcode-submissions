class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask != 0:
            x = (a ^ b) & mask
            y = (a & b) << 1
            a = x
            b = y
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)