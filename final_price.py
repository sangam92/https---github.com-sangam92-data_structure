"""
1475. Final Prices With a Special Discount in a Shop

"""
class Solution:
    def finalPrices(self, prices):
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if price >= prices[j]:
                    prices[i] -= prices[j]
                    break
        
        return prices

s=Solution()
print(s.finalPrices([8,4,6,2,3]))
        
