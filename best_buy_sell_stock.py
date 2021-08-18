"""
121. Best Time to Buy and Sell Stock

"""

class Solution:
    def maxProfit(self, prices) -> int:
	    if not prices:
		    return 0
	    maxProfit = 0
	    minPurchase = prices[0]
	    for i in range(1, len(prices)):		
		    maxProfit = max(maxProfit, prices[i] - minPurchase)
		    minPurchase = min(minPurchase, prices[i])
	    return maxProfit

s=Solution()

print(s.maxProfit([7,1,5,3,6,4]))
