class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit=0
        buy = prices[0]
        MAX=0
        for i in range(1,len(prices)):

            if MAX < prices[i]-buy:
                MAX=MAX+ (prices[i]-buy)
                buy=prices[i]
        return MAX
    
s=Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))
