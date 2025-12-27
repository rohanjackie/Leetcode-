class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP




        # 1) Initialise a left and right pointer where    left = buy and  right = sell    -- we need to buy low and sell high so stop the left pointer where the buy price is lowest
        # 2) Have a variable remember the current max profit
