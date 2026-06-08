class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set two pointers
        left, right = 0, len(s)-1
        while left < right:
            #skip non-alphanumeric char
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            # run through the whole string
            #if they not the same, return false
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        # return true if all char are the same
        return True
        