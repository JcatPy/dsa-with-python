def maxProfit(self, prices):
    max_profit = 0
    min_price = float('inf')
    for i in prices:
        if min_price > i:
            min_price = i
        else:
            max_profit = max(max_profit, i - min_price)
    return max_profit