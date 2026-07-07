class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {},{}
        for c in range(len(s)):
            countS[s[c]] = countS.get(s[c], 0) +1
            countT[t[c]] = countT.get(t[c], 0) +1
        print(countS, countT)
        return countS == countT
            