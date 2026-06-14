class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # why use hash set?
        max_count = 0
        current_count = 0
        lookup = set(nums)
        for num in lookup:
            if num-1 not in lookup:
                # begining of the sequence:
                current_count += 1
                while num+1 in lookup:
                    current_count += 1
                    num += 1
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
        return max_count

