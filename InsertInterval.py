class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        
        result.append(newInterval)
        
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
intervals = [[1,3],[6,9]]
newInterval = [2,5]
solution = Solution()
print(solution.insert(intervals, newInterval))