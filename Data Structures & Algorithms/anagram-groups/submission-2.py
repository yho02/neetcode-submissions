class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sorted_letters = "".join(sorted(string))
            if sorted_letters in anagrams:
                anagrams[sorted_letters].append(string)
            else:
                anagrams[sorted_letters] = [string]
        return list(anagrams.values())
        