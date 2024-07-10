from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A) -> str:
        max_time = -1
        
        for perm in permutations(A):
            hours = perm[0] * 10 + perm[1]
            minutes = perm[2] * 10 + perm[3]
            
            if hours < 24 and minutes < 60:
                max_time = max(max_time, hours * 60 + minutes)
        
        if max_time == -1:
            return ""
        
        max_hours = max_time // 60
        max_minutes = max_time % 60
        return f"{max_hours:02}:{max_minutes:02}"
A = [1, 2, 3, 4]
solution = Solution()
print(solution.largestTimeFromDigits(A))