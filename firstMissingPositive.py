class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        
        for num in nums:
            num = abs(num)
            if 1 <= num <= n and nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
        
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
nums = [1, 2, 0]
solution = Solution()
print(solution.firstMissingPositive(nums))