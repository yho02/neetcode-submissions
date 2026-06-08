class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1  # fix 1: use indices, not characters

        while left < right:
            if not s[left].isalnum():   # fix 2: use elif chain so we
                left += 1               #   don't compare after skipping
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():  # fix 3: case-insensitive
                return False
            else:
                left += 1
                right -= 1

        return True
            