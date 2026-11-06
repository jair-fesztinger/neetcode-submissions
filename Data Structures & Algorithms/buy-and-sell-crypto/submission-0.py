class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        min_price = None

        for i in range(len(prices)):
            #base case 
            if i == 0:
                min_price = prices[i]

            elif min_price > prices[i]:
                min_price = prices[i]

            elif min_price < prices[i]:
                gain = prices[i] - min_price
                profit.append(gain)
        if profit:
            return max(profit)
        else:
            return 0
    