class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 1
        l = 0 
        max_f = 1
        for r in range(len(s)):
            if s[r] in mp:
                mp[s[r]] += 1
                if max_f < mp[s[r]]:
                    max_f = mp[s[r]]
            else:
                mp[s[r]] = 1
            if (r-l+1) - max_f <= k:
                res = max(res, (r-l+1))
            else:
                mp[s[l]] -= 1
                l += 1 
        return res