"""
给定一个数组 prices，其中 prices[i] 表示第 i 天的股票价格。
你只能选择某一天买入这只股票，并选择一个未来的不同日期卖出。
请计算你能获得的最大利润。
如果你无法获得任何利润，返回 0

输入：
prices = [7,1,5,3,6,4]
输出：
5

输入：
prices = [7,6,4,3,1]
输出：
0
"""
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)
        return profit
