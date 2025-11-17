
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Track minimum price so far
            if price < min_price:
                min_price = price
            # Track maximum profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
