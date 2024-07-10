class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        current_max = current_min = global_max = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max
            
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            global_max = max(global_max, current_max)
        
        return global_max
nums = [2, 3, -2, 4]
solution = Solution()
print(solution.maxProduct(nums))