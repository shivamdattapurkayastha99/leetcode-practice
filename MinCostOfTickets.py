class Solution:
    def mincostTickets(self, days, costs) -> int:
        dp = [0] * (days[-1] + 1)
        day_set = set(days)
        
        for i in range(1, len(dp)):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                one_day_pass = dp[i - 1] + costs[0]
                seven_day_pass = dp[max(0, i - 7)] + costs[1]
                thirty_day_pass = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(one_day_pass, seven_day_pass, thirty_day_pass)
        
        return dp[-1]
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
solution = Solution()
print(solution.mincostTickets(days, costs)) 