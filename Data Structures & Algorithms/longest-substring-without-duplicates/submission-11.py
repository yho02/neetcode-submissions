class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        duplicates = []
        max_count = 0
        for c in range(len(s)):
            if s[c] not in duplicates:
                count += 1
                duplicates.append(s[c])
                print(duplicates)
                print(count)
            else:
                if max_count < count:
                    max_count = count
                duplicates = duplicates[duplicates.index(s[c])+1:]
                duplicates.append(s[c])
                count = len(duplicates)
        if count > max_count:
            max_count = count
        return max_count



