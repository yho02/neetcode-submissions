class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        # you need i, n because:
        # you need n - the value to calculate target - n 
        # you need i - the index to put in the map
        for i,n in enumerate(nums):
            if target - n in prev:
                return [prev[target- n], i]
            else:
                prev[n] = i 