class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # caviats: these is purely from memory 
        # keep the char with the most appearance 
        # most appearance - k = needed to be replace 
        # bigger than 0 ok
        # smaller no ok 
        # shift the window - one by one i think
        l = 0 
        mp = {}
        res = 0 
        max_ref = 0 
        # keep track of the highest character, this changes as the window shifted 
        # 
        for r in range (len(s)):
            if s[r] in mp:
                mp[s[r]] += 1
            else:
                mp[s[r]] = 1
            if max_ref<  mp[s[r]]:
                    max_ref =  mp[s[r]]
            while (r-l+1) - max_ref > k:
                if mp[s[l]] > 1: 
                    mp[s[l]] -= 1
                else: 
                    mp.pop(s[l], None)        
                l += 1
            res = max(res, r-l+1)
        return res