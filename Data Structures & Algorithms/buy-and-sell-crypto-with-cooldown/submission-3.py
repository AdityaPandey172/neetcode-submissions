class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold  = -prices[0]
        sold = 0
        rest = 0
        
        for p in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - p)
            sold = prev_hold + p
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
        