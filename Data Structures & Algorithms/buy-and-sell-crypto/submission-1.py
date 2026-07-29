class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)-1
        max_price=0
        max_val=0
        
        while n>=0:
            if max_val == 0:
                max_val=prices[n]
            else:
                if prices[n]> max_val:
                    max_val=prices[n]
                else:
                    diff = max_val -prices[n]
                    if diff > max_price:
                        max_price= diff
            n-=1
        return max_price

        