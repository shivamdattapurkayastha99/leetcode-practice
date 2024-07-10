import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if t < 0 or k < 1 or not nums:
            return False

        sorted_list = []
        for i, num in enumerate(nums):
            pos = bisect.bisect_left(sorted_list, num)
            
            if pos < len(sorted_list) and sorted_list[pos] - num <= t:
                return True
            if pos > 0 and num - sorted_list[pos - 1] <= t:
                return True

            bisect.insort(sorted_list, num)
            
            if len(sorted_list) > k:
                sorted_list.pop(bisect.bisect_left(sorted_list, nums[i - k]))

        return False
nums = [1, 2, 3, 1]
k = 3
t = 0
solution = Solution()
print(solution.containsNearbyAlmostDuplicate(nums, k, t))