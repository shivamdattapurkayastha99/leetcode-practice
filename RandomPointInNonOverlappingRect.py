import random

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.ranges = []
        total_area = 0
        
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_area += area
            self.ranges.append((total_area, (x1, y1, x2, y2)))

    def pick(self):
        rand_area = random.randint(1, self.ranges[-1][0])
        left, right = 0, len(self.ranges) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if self.ranges[mid][0] < rand_area:
                left = mid + 1
            else:
                right = mid
        
        x1, y1, x2, y2 = self.ranges[left][1]
        return [random.randint(x1, x2), random.randint(y1, y2)]
