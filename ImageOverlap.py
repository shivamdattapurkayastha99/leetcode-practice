class Solution:
    def largestOverlap(self, A: list[list[int]], B: list[list[int]]) -> int:
        def shift_and_count(x_shift, y_shift, M, R):
            count = 0
            for r in range(len(M)):
                for c in range(len(M[0])):
                    if 0 <= r + y_shift < len(M) and 0 <= c + x_shift < len(M[0]):
                        if M[r + y_shift][c + x_shift] == 1 and R[r][c] == 1:
                            count += 1
            return count
        
        max_overlaps = 0
        for y_shift in range(-len(A) + 1, len(A)):
            for x_shift in range(-len(A[0]) + 1, len(A[0])):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))
                
        return max_overlaps
A = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
B = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
solution = Solution()
print(solution.largestOverlap(A, B)) 