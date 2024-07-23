# 121. Best Time to Buy and Sell Stock (3/16/56529)
# Runtime: 689 ms (77.47%) Memory: 27.44 MB (17.08%) 

# [2,1,2,1,0,1,2]
#    L
#          R

# if num[R]-num[L] < 0, update L
# else if num[R]-num[L] > max, update max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 0
        maxProfit = 0

        for R in range(len(prices)):
            profit = prices[R] - prices[L]
            if profit < 0:
                L = R
            elif profit > maxProfit:
                maxProfit = profit    

        return maxProfit