class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):

            if prices[buy] > prices[sell]:
                buy = sell
            else:
                max_profit = max((prices[sell] - prices[buy]), max_profit)
            sell += 1

        return max_profit