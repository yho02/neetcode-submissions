class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        pointer = l + (r - l) // 2
        while l <= r:
            value = nums[pointer]
            if value == target:
                return pointer
            elif value < target:
                l = pointer + 1
            elif value > target:
                r = pointer - 1
            
            pointer = l + (r - l) // 2
            
        return -1