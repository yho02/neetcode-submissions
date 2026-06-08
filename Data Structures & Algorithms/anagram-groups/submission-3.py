class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            sorted_letters = "".join(sorted(str))
            if sorted_letters in anagrams.keys():
                anagrams[sorted_letters].append(str)
            else:
                anagrams[sorted_letters] =[str]
        return list(anagrams.values())
        