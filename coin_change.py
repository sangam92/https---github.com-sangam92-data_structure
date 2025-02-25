"""
coin change

"""

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        for i in range(len(coins)):

            for j in range(amount):

                if coins[i] > j:
                    coins[i][j] = coins[i-1][j]
                else:
                    coins[i][j] = min(coins[i-1][j],1+coins[i])