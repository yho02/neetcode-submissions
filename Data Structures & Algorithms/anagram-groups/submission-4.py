class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in mp:
                mp[sorted_str].append(str)
            else:
                mp[sorted_str] = [str]
        return list(mp.values())