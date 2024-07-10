class Solution:
    def canCompleteCircuit(self,gas,cost):
        total_gas=sum(gas)
        total_cost=sum(cost)
        if total_gas<total_cost:
            return -1
        n=len(gas)
        tank=0
        start_index=0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_index = i + 1
                tank = 0
        return start_index if start_index < n else -1
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
solution = Solution()
print(solution.canCompleteCircuit(gas, cost))