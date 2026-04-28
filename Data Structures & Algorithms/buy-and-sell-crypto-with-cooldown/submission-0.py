class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = -prices[
            0
        ]
        sell = 0
        cooldown = 0

        for i in range(1, len(prices)):
            new_buy =  max(buy, cooldown - prices[i])
            new_sell = buy + prices[i]
            new_cooldown = max(cooldown, sell)

            buy, sell, cooldown = new_buy, new_sell, new_cooldown

        return max(sell, cooldown)

