"""
1395 .count no of teams

"""

class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        g = [0] * n # <- Greater count
        s = [0] * n # <- Smaller count
        res = 0 # <- number of teams
        
        # For each soldier, we search the next greater and smaller
        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[j] > rating[i]: 
                    g[i] += 1
                else:
                    s[i] += 1
        for i in range(n - 2):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    res += g[j]
                else:
                    res += s[j]
        
        return res


s=Solution()

print(s.numTeams([2,5,3,4,1]))
        