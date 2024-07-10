class Solution:
    def lengthOflastWord(self,s):
        words=s.strip().split()
        if not words:
            return 0
        return len(words[-1])
s = "Hello World"
solution = Solution()
print(solution.lengthOflastWord(s))