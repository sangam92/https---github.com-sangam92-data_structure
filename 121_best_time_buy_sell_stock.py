class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy=prices[0]
        profit=0

        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy=prices[i]
            elif prices[i]-buy >profit:
                profit=prices[i]-buy

        return profit
    
s=Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
