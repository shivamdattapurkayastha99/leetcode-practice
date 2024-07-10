class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            palindrome_odd = expand_around_center(i, i)
            palindrome_even = expand_around_center(i, i + 1)

            longest = max(longest, palindrome_odd, palindrome_even, key=len)

        return longest
