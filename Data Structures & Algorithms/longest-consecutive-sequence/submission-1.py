class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # why use hash set?
        max_length = []
        current_arr = []
        lookup = set(nums)
        for num in lookup:
            if num-1 not in lookup:
                # begining of the sequence:
                current_arr.append(num)
                while num+1 in lookup:
                    current_arr.append(num+1)
                    num += 1
                if len(current_arr) > len(max_length):
                    max_length = current_arr.copy()
                current_arr = []
        return len(max_length)

