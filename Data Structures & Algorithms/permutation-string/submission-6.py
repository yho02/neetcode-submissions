class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        mp = {}
        frequency = {}
        for char in s1:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        for r in range(len(s2)):
            if s2[r] in mp:
                mp[s2[r]] += 1
            else:
                mp[s2[r]] = 1        
            if r-l+1 == len(s1):
                print(mp)
                print(frequency)
                if mp == frequency:
                    return True
                else:
                    if mp[s2[l]] == 1:
                        mp.pop(s2[l],None)
                    else:
                        mp[s2[l]] -= 1   
                    l += 1     
        return False 


