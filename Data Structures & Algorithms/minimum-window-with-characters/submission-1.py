class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        countT = {}
        window = {}
        res = [-1,-1]
        resLen = float ("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have, need = 0, len(countT)

        if t == "":
            return ""

        for r in range (len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            # check if s[r] is one of the char of t
            # if they have the same count
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                # have that char check out 
                    have += 1
            # once all char is checked out
            # start to shift left at most at possble
            while have == need:
                # update the shortest length
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l,r]            
            
                # move left 
                window[s[l]] -= 1

                # this means if left move over one of the required char of t
                # subtract have 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l:r+1] if resLen != float ("infinity") else ""
