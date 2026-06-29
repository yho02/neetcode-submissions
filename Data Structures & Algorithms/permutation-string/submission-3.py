class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        ref = {}
        for char in s1:
            if char in ref:
                ref[char] += 1
            else: 
                ref[char] = 1
        print(ref)
        mp = {}
        for r in range(len(s2)):
            if s2[r] in mp:
                mp[s2[r]] += 1
            else:
                mp[s2[r]] = 1
            print(mp)
            if r == l+len(s1) - 1:
                if ref == mp:
                    return True
                else: 
                    if mp[s2[l]] == 1:
                        mp.pop(s2[l],None)
                    else: 
                        mp[s2[l]] -= 1
                    l += 1
        
        return False 



            